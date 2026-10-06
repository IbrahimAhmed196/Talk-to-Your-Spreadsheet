"""Talk to Your Spreadsheet: Streamlit frontend.

Run from this folder: streamlit run app.py
Set BACKEND_URL below to the deployed backend address.
"""
import html
import inspect
import time
from pathlib import Path

import pandas as pd
import plotly.io as pio
import requests
import streamlit as st
from PIL import Image

APP_DIR = Path(__file__).parent
LOGO_PATH = APP_DIR / "assets" / "logo.png"
ICON_PATH = APP_DIR / "assets" / "icon.png"

INK, GREEN, BLUE = "#0C2033", "#04A36D", "#0061D9"
REQUEST_HEADERS = {"ngrok-skip-browser-warning": "true"}
BACKEND_URL = "YOUR_BACKEND_URL".rstrip("/")    # Put the ngrok url from the backend
CHAT_HISTORY_LIMIT = 30

st.set_page_config(
    page_title="Talk to Your Spreadsheet",
    page_icon=Image.open(ICON_PATH) if ICON_PATH.exists() else "📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------- #
# Compatibility helpers (Streamlit renamed use_container_width to width="stretch")
# --------------------------------------------------------------------------- #
def _version():
    parts = st.__version__.split(".")
    return tuple(int(p) for p in parts[:2] if p.isdigit())

def stretch():
    return {"width": "stretch"} if _version() >= (1, 50) else {"use_container_width": True}

def keyed_container(key):
    """A container that gets a CSS class (st-key-<key>) on Streamlit versions that support keys."""
    if "key" in inspect.signature(st.container).parameters:
        return st.container(key=key)
    return st.container()

def column_letter(position):
    letters = ""
    position += 1
    while position:
        position, remainder = divmod(position - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters

# --------------------------------------------------------------------------- #
# Styling
# --------------------------------------------------------------------------- #
STYLE = f"""
<style>
@font-face {{ font-family: "Outfit"; font-weight: 400; font-display: swap; src: url("app/static/outfit-400.woff2") format("woff2"); }}
@font-face {{ font-family: "Outfit"; font-weight: 500; font-display: swap; src: url("app/static/outfit-500.woff2") format("woff2"); }}
@font-face {{ font-family: "Outfit"; font-weight: 600; font-display: swap; src: url("app/static/outfit-600.woff2") format("woff2"); }}
@font-face {{ font-family: "Outfit"; font-weight: 700; font-display: swap; src: url("app/static/outfit-700.woff2") format("woff2"); }}

:root {{ --ink: {INK}; --green: {GREEN}; --blue: {BLUE}; --mint: #E8F5EF; --paper: #F3F7F9; --rule: #D9E2EA; --muted: #5B6B7B; }}

.stApp, .stApp p, .stApp label, .stApp li, .stApp input, .stApp textarea, .stApp button,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stCaptionContainer"], .stApp [data-testid="stMetricValue"],
.stApp [data-baseweb="tab"], .stApp [data-baseweb="select"] {{
  font-family: "Outfit", system-ui, -apple-system, "Segoe UI", sans-serif;
}}
.stApp code, .stApp pre, .stApp [data-testid="stCode"] * {{
  font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, Consolas, monospace;
}}

.block-container {{ max-width: 980px; padding-top: 2.2rem; padding-bottom: 6rem; }}
h1, h2, h3 {{ color: var(--ink); letter-spacing: -0.015em; }}

/* sidebar */
[data-testid="stSidebar"] {{ background: var(--paper); border-right: 1px solid var(--rule); }}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{ padding-top: 1.2rem; }}
[data-testid="stSidebar"] h3 {{ font-size: 1.02rem; font-weight: 600; margin: 1.1rem 0 .4rem; }}
[data-testid="stSidebar"] [data-testid="stExpander"] {{ background: #fff; border: 1px solid var(--rule); border-radius: 10px; }}

/* connection pill */
.pill {{ display: inline-flex; align-items: center; gap: .45rem; padding: .22rem .7rem; border-radius: 999px;
         font-size: .86rem; font-weight: 500; border: 1px solid var(--rule); background: #fff; color: var(--ink); }}
.pill .dot {{ width: .5rem; height: .5rem; border-radius: 50%; background: #9AA8B5; }}
.pill.ok {{ border-color: #B5E3D0; background: var(--mint); }}
.pill.ok .dot {{ background: var(--green); }}
.pill.bad {{ border-color: #F3C9C4; background: #FDF1EF; }}
.pill.bad .dot {{ background: #D6453A; }}

/* page head */
.page-head h1 {{ font-size: 2rem; font-weight: 700; margin: 0 0 .25rem; padding: 0; }}
.page-head p {{ color: var(--muted); font-size: 1.05rem; margin: 0 0 1.4rem; max-width: 62ch; }}

/* numbered setup steps (this really is a sequence) */
.steps {{ counter-reset: step; list-style: none; padding: 0; margin: 1.2rem 0 0; max-width: 64ch; }}
.steps li {{ counter-increment: step; position: relative; padding: 0 0 1.1rem 3rem; font-size: 1.04rem; line-height: 1.45; }}
.steps li::before {{ content: counter(step); position: absolute; left: 0; top: -.1rem; width: 2rem; height: 2rem; border-radius: 50%;
                     background: var(--mint); color: #05704B; font-weight: 600; display: grid; place-items: center; }}
.steps li:not(:last-child)::after {{ content: ""; position: absolute; left: 1rem; top: 2rem; bottom: .15rem; width: 1px; background: var(--rule); }}
.steps code {{ background: var(--paper); border: 1px solid var(--rule); border-radius: 6px; padding: .05rem .4rem; font-size: .9em; }}

/* chat */
[data-testid="stChatMessage"] {{ background: transparent; padding: .6rem 0; }}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{ background: var(--paper); border-radius: 12px; padding: .6rem .9rem; }}
[data-testid="stChatInput"] {{ border-radius: 14px; border-color: var(--rule); }}
.meta {{ color: var(--muted); font-size: .88rem; margin: 0 0 .35rem; }}
.tag {{ display: inline-block; font-weight: 600; font-size: .82rem; padding: .08rem .55rem; border-radius: 6px; margin-right: .5rem; }}
.meta .detail {{ margin-right: .9rem; }}
.tag.data {{ background: #E5EEFC; color: #0A4BB0; }}
.tag.formula {{ background: var(--mint); color: #05704B; }}
.tag.chat {{ background: #EEF1F4; color: var(--ink); }}

/* formula bar */
[class*="st-key-formula_bar"] {{ border: 1px solid var(--rule); border-radius: 10px; background: #fff; display: flex; flex-direction: row;
                                 align-items: stretch; gap: 0; overflow: hidden; margin: .3rem 0 .6rem; }}
[class*="st-key-formula_bar"]::before {{ content: "fx"; display: grid; place-items: center; padding: 0 1rem; background: var(--paper);
                                         border-right: 1px solid var(--rule); color: #05704B; font-style: italic; font-weight: 600; font-size: 1.05rem; }}
[class*="st-key-formula_bar"] > div {{ flex: 1; min-width: 0; }}
[class*="st-key-formula_bar"] [data-testid="stCode"] {{ background: transparent; }}
[class*="st-key-formula_bar"] pre {{ background: transparent !important; font-size: 1.05rem; }}

/* inputs need a visible edge on the white expander surface */
[data-testid="stSidebar"] [data-baseweb="input"], [data-testid="stSidebar"] [data-baseweb="select"] > div {{ border: 1px solid #B9C7D3; background: #fff; border-radius: 8px; }}

/* starter questions and buttons */
[class*="st-key-starters"] button {{ text-align: left; justify-content: flex-start; border-radius: 10px; border: 1px solid var(--rule);
                                      background: #fff; font-weight: 500; min-height: 3rem; }}
[class*="st-key-starters"] button div {{ justify-content: flex-start; }}
[class*="st-key-starters"] button p {{ text-align: left; }}
[class*="st-key-starters"] button:hover {{ border-color: var(--green); background: var(--mint); color: var(--ink); }}
.stButton button, .stDownloadButton button {{ border-radius: 9px; font-weight: 500; }}

[data-testid="stExpander"] {{ border-radius: 10px; border-color: var(--rule); }}
[data-testid="stMetric"] {{ background: var(--mint); border-radius: 12px; padding: .9rem 1.1rem; }}
footer {{ visibility: hidden; }}
</style>
"""
st.markdown(STYLE, unsafe_allow_html=True)

# --------------------------------------------------------------------------- #
# State
# --------------------------------------------------------------------------- #
DEFAULTS = {
    "connected": False,
    "backend_info": None,
    "backend_error": None,
    "session_id": None,
    "filename": None,
    "workbook_info": None,
    "skipped_sheets": [],
    "history": [],
    "queued_question": None,
}
for key, default in DEFAULTS.items():
    st.session_state.setdefault(key, default)

def api_error(response):
    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text
    return detail if isinstance(detail, str) else str(detail)

def check_backend():
    st.session_state.backend_info = None
    st.session_state.backend_error = None
    try:
        response = requests.get(f"{BACKEND_URL}/health", headers=REQUEST_HEADERS, timeout=10)
        if response.status_code == 200:
            st.session_state.connected = True
            st.session_state.backend_info = response.json()
        else:
            st.session_state.connected = False
            st.session_state.backend_error = "The service is temporarily unavailable."
    except requests.RequestException:
        st.session_state.connected = False
        st.session_state.backend_error = "The service is temporarily unavailable."

if st.session_state.backend_info is None and st.session_state.backend_error is None:
    check_backend()

def reset_workbook_state():
    st.session_state.session_id = None
    st.session_state.filename = None
    st.session_state.workbook_info = None
    st.session_state.skipped_sheets = []
    st.session_state.history = []

def upload_workbook(uploaded):
    reset_workbook_state()
    try:
        with st.spinner("Reading the workbook..."):
            response = requests.post(
                f"{BACKEND_URL}/upload",
                files={"file": (uploaded.name, uploaded.getvalue())},
                headers=REQUEST_HEADERS,
                timeout=60,
            )
    except requests.RequestException as error:
        st.session_state.connected = False
        return f"Upload failed: {error}"

    if response.status_code != 200:
        return api_error(response)

    data = response.json()
    st.session_state.session_id = data["session_id"]
    st.session_state.filename = data["filename"]
    st.session_state.workbook_info = data["sheets"]
    st.session_state.skipped_sheets = data.get("skipped_sheets", [])
    return None

def clear_conversation():
    st.session_state.history = []
    st.session_state.queued_question = None
    if st.session_state.session_id and st.session_state.connected:
        try:
            requests.post(
                f"{BACKEND_URL}/reset/{st.session_state.session_id}",
                headers=REQUEST_HEADERS, timeout=15,
            )
        except requests.RequestException:
            pass   # the local chat is cleared either way

def queue_question(text):
    st.session_state.queued_question = text

# --------------------------------------------------------------------------- #
# Sidebar
# --------------------------------------------------------------------------- #
with st.sidebar:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), **stretch())
    else:
        st.markdown("## Talk to Your Spreadsheet")

    connected = st.session_state.connected
    if not connected and st.session_state.backend_error:
        st.error(st.session_state.backend_error)

    st.markdown("### Workbook")
    uploaded_file = st.file_uploader("Excel workbook (.xlsx)", type=["xlsx"], label_visibility="collapsed")
    if st.button("Upload workbook", type="primary", disabled=not connected or uploaded_file is None, **stretch()):
        upload_error = upload_workbook(uploaded_file)
        if upload_error:
            st.error(upload_error)

    workbook_info = st.session_state.workbook_info
    if workbook_info:
        st.markdown(f"**{html.escape(st.session_state.filename)}**")
        st.caption(", ".join(
            f"{name} ({info['rows']:,} rows)" for name, info in workbook_info.items()
        ))
        if st.session_state.skipped_sheets:
            st.caption("Skipped empty sheets: " + ", ".join(st.session_state.skipped_sheets))

    sheet_name = None
    if workbook_info:
        sheet_names = list(workbook_info)
        choice = st.selectbox("Worksheet", ["All sheets"] + sheet_names)
        sheet_name = None if choice == "All sheets" else choice
        if sheet_name is None and len(sheet_names) > 1:
            st.caption("Formula requests use the first worksheet unless you select one.")

    if st.session_state.history:
        st.button("Clear conversation", on_click=clear_conversation, **stretch())


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
PLOTLY_DEFAULTS = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A",
                   "#19D3F3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"]
BRAND_COLORS = [GREEN, BLUE, "#7BD3B5", "#7AA7F0", INK, "#B7C4D1"]

def recolor(color):
    """Plotly Express writes its default palette into every trace; swap it for the brand palette."""
    if isinstance(color, str) and color.upper() in PLOTLY_DEFAULTS:
        return BRAND_COLORS[PLOTLY_DEFAULTS.index(color.upper()) % len(BRAND_COLORS)]
    return color

def style_figure(fig):
    fig.update_layout(
        template="plotly_white",
        colorway=BRAND_COLORS,
        font=dict(family="Outfit, system-ui, sans-serif", color=INK),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=8, r=8, t=56, b=8),
    )
    for trace in fig.data:
        marker = getattr(trace, "marker", None)
        if marker is not None and isinstance(getattr(marker, "color", None), str):
            marker.color = recolor(marker.color)
        line = getattr(trace, "line", None)
        if line is not None and isinstance(getattr(line, "color", None), str):
            line.color = recolor(line.color)
    return fig

def format_scalar(value):
    if isinstance(value, float):
        return f"{value:,.0f}" if value.is_integer() else f"{value:,.4g}" if abs(value) < 1 else f"{value:,.2f}"
    if isinstance(value, int) and not isinstance(value, bool):
        return f"{value:,}"
    return str(value)

def display_result(result, index):
    kind = result.get("kind")

    if kind == "table":
        frame = pd.DataFrame(result["rows"], columns=result["columns"])
        st.dataframe(frame, hide_index=True, **stretch())
        left, right = st.columns([3, 1])
        with left:
            if result["truncated"]:
                st.caption(f"Showing {len(frame):,} of {result['total_rows']:,} rows.")
            else:
                st.caption(f"{len(frame):,} rows")
        with right:
            st.download_button(
                "Download CSV", frame.to_csv(index=False).encode("utf-8"),
                file_name="result.csv", mime="text/csv", key=f"download_{index}", **stretch(),
            )

    elif kind == "scalar":
        st.metric("Result", format_scalar(result["value"]))

    elif kind == "object":
        value = result["value"]
        if isinstance(value, dict):
            try:
                st.dataframe(pd.DataFrame(list(value.items()), columns=["Item", "Value"]), hide_index=True, **stretch())
            except (ValueError, TypeError):
                st.json(value)
        else:
            st.write(value)

    elif kind == "list":
        st.write(result["value"])
        if result.get("truncated"):
            st.caption("Only the first values are shown.")

    else:
        st.json(result)

def meta_line(kind, seconds, extra=""):
    labels = {"data": "Analysis", "formula": "Excel formula", "chat": "Chat"}
    label = labels.get(kind, "Response")
    css = kind if kind in labels else "chat"
    parts = [f"{seconds:.1f} s"] if seconds is not None else []
    if extra:
        parts.append(extra)
    details = "".join(f'<span class="detail">{html.escape(p)}</span>' for p in parts)
    st.markdown(f'<p class="meta"><span class="tag {css}">{label}</span>{details}</p>', unsafe_allow_html=True)

def render_data_response(data, index, seconds):
    extra = "Built on the previous result" if data.get("source") == "last_result" else (
        f"Sheet: {data['sheet_name']}" if data.get("sheet_name") else "")
    meta_line("data", seconds, extra)

    if data.get("explanation"):
        st.write(data["explanation"])

    if data.get("result") is not None:
        display_result(data["result"], index)

    if data.get("figure") is not None:
        figure = style_figure(pio.from_json(data["figure"], skip_invalid=True))
        st.plotly_chart(figure, key=f"chart_{index}", **stretch())

    with st.expander("How this was worked out"):
        plan_tab, code_tab, route_tab = st.tabs(["Plan", "Python", "Routing"])
        with plan_tab:
            plan = data.get("plan", {})
            st.markdown(f"**{plan.get('objective', '')}**")
            for number, step in enumerate(plan.get("steps", []), start=1):
                st.markdown(f"{number}. {step}")
            if plan.get("columns"):
                st.caption("Columns used: " + ", ".join(plan["columns"]))
            if plan.get("derived_columns"):
                st.caption("New columns created: " + ", ".join(plan["derived_columns"]))
        with code_tab:
            st.code(data.get("code", ""), language="python")
            attempts = data.get("attempts", 1)
            st.caption("Ran on the first try." if attempts == 1 else f"Ran after {attempts} attempts (the code was repaired once).")
        with route_tab:
            if data.get("resolved_question") != data.get("question"):
                st.markdown("**Question as understood**")
                st.write(data["resolved_question"])
            st.json(data.get("router", {}))

def render_formula_response(data, index, seconds):
    answer = data["result"]
    meta_line("formula", seconds, f"Sheet: {data.get('sheet_name', '')}")

    with keyed_container(f"formula_bar_{index}"):
        st.code(answer["formula"], language="text")
    st.write(answer["explanation"])

    mapping = answer.get("column_mapping", {})
    if mapping:
        st.markdown("**Columns it uses:** " + ", ".join(f"**{letter}** {header}" for letter, header in mapping.items()))

    if data.get("use_rag") and data.get("retrieved"):
        with st.expander("Excel documentation used"):
            for doc in data["retrieved"]:
                st.markdown(f"**{doc['title']}**")
                st.code(doc["text"], language="text")
                source = doc.get("source", "")
                if source.startswith("http"):
                    st.caption(f"[Microsoft documentation]({source})")
                elif source:
                    st.caption(source)

def render_chat_response(data, seconds):
    meta_line("chat", seconds)
    st.write(data.get("result", ""))

def render_turn(turn, index):
    if turn.get("error"):
        st.error(turn["error"])
        st.caption("Try rephrasing the question, naming the column exactly, or choosing a worksheet in the sidebar.")
        return

    data = turn["response"]
    seconds = data.get("elapsed", turn.get("seconds"))
    if data["mode"] == "formula":
        render_formula_response(data, index, seconds)
    elif data["mode"] == "chat":
        render_chat_response(data, seconds)
    else:
        render_data_response(data, index, seconds)

def assistant_avatar():
    return str(ICON_PATH) if ICON_PATH.exists() else None

def user_avatar():
    return ":material/person:" if _version() >= (1, 36) else None

# --------------------------------------------------------------------------- #
# Backend call
# --------------------------------------------------------------------------- #
def ask_backend(question):
    payload = {
        "session_id": st.session_state.session_id,
        "question": question,
        "mode": "auto",
        "sheet_name": sheet_name,
        "use_rag": True,
    }
    started = time.perf_counter()
    try:
        response = requests.post(
            f"{BACKEND_URL}/ask", json=payload, headers=REQUEST_HEADERS, timeout=300
        )
    except requests.Timeout:
        return {"error": "The request took longer than 5 minutes. Try a simpler question."}
    except requests.RequestException:
        st.session_state.connected = False
        st.session_state.backend_error = "Lost the connection to the backend."
        return {"error": "The service is temporarily unavailable. Please try again shortly."}

    seconds = time.perf_counter() - started
    if response.status_code == 200:
        return {"response": response.json(), "seconds": seconds}
    if response.status_code == 404:
        st.session_state.session_id = None
        return {"error": "The workbook session expired (the backend was restarted). Upload your workbook again."}
    return {"error": api_error(response)}

def tidy_preview(rows):
    """Dates arrive as ISO timestamps; show midnight timestamps as plain dates."""
    frame = pd.DataFrame(rows)
    for column in frame.columns:
        frame[column] = frame[column].map(
            lambda v: v[:-9] if isinstance(v, str) and v.endswith("T00:00:00") else v
        )
    return frame

# --------------------------------------------------------------------------- #
# Starter questions built from the actual columns
# --------------------------------------------------------------------------- #
def starter_questions(sheet):
    names = sheet["column_names"]
    kinds = sheet.get("column_kinds", {})
    unique = sheet.get("column_unique", {})
    rows = max(sheet.get("rows", 0), 1)
    numbers = [c for c in names if kinds.get(c) == "number"]
    # a grouping column repeats: a few distinct values, far fewer than the number of rows
    groupers = [c for c in names if kinds.get(c) == "text" and 1 < unique.get(c, 0) <= min(25, max(2, rows // 2))]
    dates = [c for c in names if kinds.get(c) == "date"]
    analysis, formulas = [], []

    if numbers and groupers:
        analysis.append(f"Average {numbers[0]} by {groupers[0]}")
        analysis.append(f"Total {numbers[-1]} by {groupers[0]} as a bar chart")
    if numbers and dates:
        analysis.append(f"Plot {numbers[0]} over {dates[0]} as a line chart")
    if numbers:
        analysis.append(f"Show the distribution of {numbers[0]}")
        formulas.append(f"Write an Excel formula for the total of {numbers[0]}")
    if len(numbers) >= 2:
        analysis.append(f"How are {numbers[0]} and {numbers[1]} related?")
        formulas.append(f"Write an Excel formula for {numbers[0]} minus {numbers[1]} in each row")
    if not analysis:
        analysis.append("Summarize this sheet")

    picks = analysis[:3] + formulas[:1]
    return picks[:4]

# --------------------------------------------------------------------------- #
# Main page
# --------------------------------------------------------------------------- #
pending_question = st.session_state.pop("queued_question", None)
ready = st.session_state.connected and st.session_state.session_id is not None

if not st.session_state.connected:
    head_left, head_right = st.columns([1, 6], vertical_alignment="center") if _version() >= (1, 36) else st.columns([1, 6])
    with head_left:
        if ICON_PATH.exists():
            st.image(str(ICON_PATH), width=84)
    with head_right:
        st.markdown(
            '<div class="page-head"><h1>Service unavailable</h1>'
            "<p>The assistant cannot connect right now. Please try again shortly.</p></div>",
            unsafe_allow_html=True,
        )
    if st.button("Retry connection", type="primary"):
        check_backend()
        st.rerun()

elif not st.session_state.workbook_info:
    st.markdown(
        '<div class="page-head"><h1>Upload a workbook</h1>'
        "<p>Choose an .xlsx file in the sidebar. Row 1 of every sheet should hold the column headers.</p></div>",
        unsafe_allow_html=True,
    )
    left, right = st.columns(2)
    with left:
        st.markdown("**Ask about your data**")
        st.markdown("- What is the average salary by department?\n- Plot monthly revenue as a line chart\n- Which five customers spent the most?")
    with right:
        st.markdown("**Get a formula for Excel**")
        st.markdown("- Profit margin for each row\n- Total sales for the North region\n- Flag duplicate order IDs")

else:
    info = st.session_state.workbook_info
    st.markdown(
        f'<div class="page-head"><h1>{html.escape(st.session_state.filename)}</h1>'
        "<p>Ask a question in plain language. Charts and tables appear here, and formulas come ready to paste.</p></div>",
        unsafe_allow_html=True,
    )

    with st.expander("Preview the workbook", expanded=not st.session_state.history):
        tabs = st.tabs(list(info))
        for tab, (name, sheet) in zip(tabs, info.items()):
            with tab:
                letters = ", ".join(
                    f"**{column_letter(i)}** {column}" for i, column in enumerate(sheet["column_names"])
                )
                st.caption(f"{sheet['rows']:,} rows. Excel column letters: ")
                st.markdown(letters)
                if sheet.get("preview"):
                    st.dataframe(tidy_preview(sheet["preview"]), hide_index=True, **stretch())

    if not st.session_state.history and not pending_question:
        first_sheet = info[sheet_name] if sheet_name in info else next(iter(info.values()))
        st.markdown("**Try one of these**")
        with keyed_container("starters"):
            picks = starter_questions(first_sheet)
            columns = st.columns(2)
            for position, text in enumerate(picks):
                with columns[position % 2]:
                    st.button(text, key=f"starter_{position}", on_click=queue_question, args=(text,), **stretch())

for index, turn in enumerate(st.session_state.history):
    with st.chat_message("user", avatar=user_avatar()):
        st.write(turn["question"])
    with st.chat_message("assistant", avatar=assistant_avatar()):
        render_turn(turn, index)

if not st.session_state.connected:
    placeholder = "Service unavailable"
elif not ready:
    placeholder = "Upload a workbook to start"
else:
    placeholder = "Ask about your spreadsheet..."

typed_question = st.chat_input(placeholder, disabled=not ready)
question = typed_question or pending_question

if question and ready:
    with st.chat_message("user", avatar=user_avatar()):
        st.write(question)
    with st.chat_message("assistant", avatar=assistant_avatar()):
        with st.spinner("Working on it..."):
            outcome = ask_backend(question)
        turn = {"question": question, **outcome}
        st.session_state.history = (st.session_state.history + [turn])[-CHAT_HISTORY_LIMIT:]
        render_turn(turn, len(st.session_state.history) - 1)

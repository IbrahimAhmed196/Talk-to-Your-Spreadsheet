# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        | Ibrahim Ahmed Badr Eldeen            |
| Project Name     | Talk to Your Spreadsheet             |
| GitHub Username  | IbrahimAhmed196                      |
| Internship Batch | August–October 2026                  |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en)                         |

---

# 📖 Project Overview

**Talk to Your Spreadsheet** is an AI-powered Excel assistant that allows users to upload Excel workbooks and interact with their data using natural language.

Instead of manually writing Pandas code, creating charts, or searching for the correct Excel formula, users can simply ask questions such as:

- "Calculate the average Revenue by Region."
- "Now visualize those averages."
- "Which Order_ID values are duplicated?"
- "Give me an Excel formula to calculate Profit Margin."

The system automatically determines whether the request is:

- a spreadsheet analysis request,
- a visualization request,
- an Excel formula request,
- or a normal conversational message.

For spreadsheet analysis, an LLM creates a structured plan and generates Python code using Pandas, NumPy, and Plotly. The generated code is then executed on the uploaded data.

For Excel formula generation, the system uses **Retrieval-Augmented Generation (RAG)** with Excel documentation stored in a FAISS vector index. Relevant documentation is retrieved automatically before generating the formula.

The application also maintains short conversation memory, allowing follow-up requests such as:

```text
Calculate the average Revenue by Region.
Now visualize those averages.
```
---

# ✨ Features

- Upload Excel `.xlsx` workbooks.
- Support for multiple worksheets.
- Select a specific worksheet or analyze all available sheets.
- Natural-language spreadsheet analysis.
- Automatic generation of Pandas and NumPy code.
- Interactive Plotly visualizations.
- Combined analysis and visualization requests.
- Automatic chart generation based on the user's request.
- Context-aware routing between:
  - Data analysis
  - Excel formulas
  - General conversation
- Conversation memory for follow-up requests.
- Reuse of previous analytical results.
- Automatic Excel formula generation.
- Retrieval-Augmented Generation using Excel documentation.
- FAISS vector search for relevant Excel functions and formula examples.
- Structured LLM outputs using LangChain.
- LCEL chains for routing, planning, formula generation, code generation, and repair.
- Separate general-purpose and code-specialized LLMs.
- Automatic code-repair attempt if generated analysis code fails.
- Multi-sheet awareness using exact worksheet names.
- Expandable UI sections showing:
  - Routing decision
  - Resolved question
  - Analysis plan
  - Generated Python code
  - Retrieved Excel documentation
- Casual conversation support such as:
  - "Hi"
  - "Thanks"
  - "What can you do?"

---

# 🛠️ Technologies Used

## Large Language Models

- **Qwen/Qwen2.5-7B-Instruct**
  - Intent routing
  - Analysis planning
  - Excel formula generation
  - General chat

- **Qwen/Qwen2.5-Coder-7B-Instruct**
  - Pandas code generation
  - NumPy operations
  - Plotly visualization code
  - Code repair

## LangChain

- PromptTemplate
- RunnableLambda
- LCEL chains
- ResponseSchema
- StructuredOutputParser

## Retrieval-Augmented Generation

- Sentence Transformers
- `sentence-transformers/all-MiniLM-L6-v2`
- FAISS
- Excel function documentation
- Markdown-based knowledge base

## Data Analysis

- Pandas
- NumPy
- SciPy
- Statsmodels

## Visualization

- Plotly
- Plotly Express

## Backend

- FastAPI
- Uvicorn
- Pydantic
- Python Multipart

## Frontend

- Streamlit
- Requests
- Plotly
- Pandas

## Spreadsheet Processing

- OpenPyXL

## Model Optimization

- Hugging Face Transformers
- Accelerate
- BitsAndBytes
- 4-bit NF4 quantization

---

# ⚙️ Installation

The project currently uses two components:

- A **backend notebook** that runs the LLMs, RAG pipeline, FastAPI server, and spreadsheet processing.
- A **local Streamlit frontend** that communicates with the backend through an ngrok URL.

## 1. Clone the Repository

```bash
git clone https://github.com/IbrahimAhmed196/Talk-to-Your-Spreadsheet.git
cd Talk-to-Your-Spreadsheet
```

---

## 2. Set Up the Backend on Kaggle

Upload the backend notebook to [Kaggle](https://www.kaggle.com/).

For the current project setup, configure the notebook with:

- **Accelerator:** GPU T4 x2
- **Internet:** On
- **Persistence:** Optional

Internet access is required to download the Hugging Face models and create the ngrok tunnel.

### Required Files

The backend also requires the Excel documentation knowledge base:

```text
excel_functions.md
```

Add the file to the notebook either by uploading it as a Kaggle dataset or by making it available in the notebook environment.

The file is used to build the FAISS vector index for Excel formula generation.

---

## 3. Add the ngrok Token

The backend uses **ngrok** to expose the FastAPI server so that the local Streamlit frontend can communicate with it.

Create an account at:

```text
https://ngrok.com/
```

Copy your ngrok authentication token.

In Kaggle, open:

```text
Add-ons → Secrets
```

Create a secret named:

```text
NGROK_TOKEN
```

and store your ngrok token as its value.

The notebook reads this secret automatically when starting the backend.

---

## 4. Run the Backend Notebook

Run the notebook cells from top to bottom.

The notebook will:

1. Install the required Python packages.
2. Load the quantized language models.
3. Load the embedding model.
4. Read the Excel documentation.
5. Create the FAISS vector index.
6. Start the FastAPI server.
7. Create an ngrok tunnel.

The main models currently used are:

```text
Qwen/Qwen2.5-7B-Instruct
Qwen/Qwen2.5-Coder-7B-Instruct
```

Both models are loaded using 4-bit quantization to reduce GPU memory usage.

When the backend is ready, the notebook will print a public URL similar to:

```text
https://example.ngrok-free.app
```

Keep the notebook running while using the application.

> The ngrok URL may change whenever the backend session is restarted.

---

## 5. Configure the Frontend Backend URL

Open:

```text
frontend/app.py
```

Find:

```python
BACKEND_URL = "YOUR_BACKEND_URL"
```

Replace it with the ngrok URL printed by the backend notebook:

```python
BACKEND_URL = "https://example.ngrok-free.app"
```

The backend URL is stored in the application code and is not entered by the end user through the interface.

---

## 6. Create the Frontend Environment

Open a terminal inside the project directory and create a Python virtual environment:

```powershell
py -m venv .venv
```

Install the frontend dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r frontend\requirements.txt
```

If the virtual environment is already located in the project root and you are currently inside the `frontend` folder, use:

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## 7. Run the Streamlit Frontend

From the `frontend` directory, run:

```powershell
..\.venv\Scripts\python.exe -m streamlit run app.py
```

If the virtual environment is inside the `frontend` directory instead, use:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit will normally open automatically in the browser at:

```text
http://localhost:8501
```

---

# 🚀 Usage

# 1. Upload a Workbook

Upload an Excel `.xlsx` workbook through the Streamlit interface.

The application automatically detects all non-empty worksheets.

For example:

```text
Orders
People
Returns
```

The user can select a specific worksheet or choose:

```text
All Sheets
```

## 2. Ask Analysis Questions

Examples:

```text
Calculate the average Revenue by Region.
```

```text
What are the top 5 products by total Sales?
```

```text
Which Order_ID values are duplicated?
```

```text
Calculate the correlation between Sales and Profit.
```

## 3. Generate Visualizations

Examples:

```text
Visualize total Sales by Product.
```

```text
Show Revenue over time.
```

```text
Show Sales versus Profit as a scatter plot.
```

The system generates Plotly code and displays the resulting interactive chart.

## 4. Use Follow-Up Questions

The system maintains recent conversation context.

Example:

```text
Calculate the average Sales by Category.
```

Then:

```text
Now visualize those averages.
```

The second request can operate directly on the previous analytical result.

## 5. Generate Excel Formulas

Formula-related requests automatically use the Excel documentation RAG pipeline.

Examples:

```text
Give me an Excel formula to calculate Profit divided by Sales for each row.
```

```text
Give me an Excel formula to calculate the number of days between Order Date and Ship Date.
```

```text
Give me an Excel formula to flag an order as Review if Sales is greater than 1000 and Profit is negative.
```

The generated formula can then be copied directly into Excel and filled down the column.

Example generated formula:

```excel
=IFERROR(V2/S2,0)
```

Another example:

```excel
=IF(AND(S2>1000,V2<0),"Review","OK")
```

## 6. General Conversation

The assistant can also handle messages that do not require spreadsheet processing.

Examples:

```text
Hi
```

```text
Thanks!
```

```text
What can you do?
```

These messages are routed to the general chat pipeline rather than the spreadsheet analysis or formula pipelines.


---

# 📸 Demo

[▶ Watch the Project Demo](https://drive.google.com/file/d/1p4PrGFsfP8pbu9KsaGZSmjc87KKsmYLb/view?usp=sharing)

---

# 📈 Results

The project successfully demonstrates an end-to-end LLM-powered spreadsheet assistant.

The implemented system can:

- Correctly route spreadsheet analysis requests.
- Correctly identify Excel formula requests.
- Correctly detect casual conversation.
- Generate executable Pandas code from natural-language requests.
- Perform exact calculations using the uploaded spreadsheet rather than relying on LLM arithmetic.
- Generate interactive Plotly visualizations.
- Maintain short conversation history.
- Resolve follow-up requests.
- Reuse previous analysis results.
- Generate Excel formulas using retrieved documentation.
- Work with multiple worksheets.
- Provide transparency by exposing the generated plan and Python code.

During testing, the **Qwen2.5-Coder-7B-Instruct** model produced significantly more reliable spreadsheet-analysis code than the smaller 3B version.

For example, the system successfully handled requests such as:

```text
Calculate the average Salary by Department.
```

and generated:

```python
result = df.groupby('Department')['Salary'].mean()
```

It also correctly understood:

```text
Hi
```

as a chat request rather than incorrectly treating it as spreadsheet analysis.

A follow-up request such as:

```text
Now visualize those averages.
```

was correctly connected to the previous analytical result and used to generate an interactive Plotly chart.

The formula pipeline also successfully generated spreadsheet formulas such as:

```excel
=B2-C2
```

while retrieving relevant Excel documentation through the RAG system.

---

# 🔮 Future Improvements

- Improve relational operations between multiple worksheets.
- Support automatic joins between sheets using common keys such as `Order ID` or `Customer ID`.
- Add CSV support.
- Allow generated formulas to be inserted directly into the workbook.
- Allow analytical results to be written back into the workbook.
- Add downloadable modified workbooks.
- Improve long-term conversation memory.
- Add persistent user sessions.
- Add stronger sandboxing for generated Python code.
- Add authentication and multi-user support.
- Expand the Excel documentation knowledge base.
- Improve retrieval using hybrid search or reranking.
- Add automated formula validation using a spreadsheet engine.
- Add automated unit and integration tests.
- Add persistent storage instead of keeping sessions only in memory.
- Deploy the backend and frontend as a complete production application.

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.

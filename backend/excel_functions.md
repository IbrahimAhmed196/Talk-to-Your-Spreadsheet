# Excel functions and formula recipes

Cleaned reference for Talk to Your Spreadsheet. Contains 47 functions and 5 project-authored recipes. Explanations and examples are edited for this project; Microsoft documentation links are retained for reference. Examples are not copied Microsoft test cases.

Conventions: English function names, comma separators, and straight double quotes. Square brackets and ... in Syntax denote optional or repeated arguments; never paste them into a formula. Row 1 is the header and row 2 is the first data row. Column letters and final row 100 are illustrative; substitute the uploaded sheet's actual columns and last data row. $ fixes a reference when a formula is filled down. Put summary results outside their input range to avoid circular references. Usage describes the example, not every possible use of the function.

Formula examples were checked structurally, not evaluated in Excel. Percentage results need Percentage cell formatting. Check the target Excel version before choosing newer functions.

## SUM

Purpose: Adds its arguments

Syntax: `=SUM(number1, [number2], ...)`

Arguments: number1: first number or range; number2: optional additional number or range.

Example (project-authored): `=SUM(H2:H100)`

Use when: grand total; total sales; add a column

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Text and blank cells in referenced ranges are ignored; error cells propagate.

Source: https://support.microsoft.com/en-us/excel/functions/sum-function

## SUMIF

Purpose: Adds the cells specified by a given criteria

Syntax: `=SUMIF(range, criteria, [sum_range])`

Arguments: range: cells to test; criteria: condition; sum_range: cells to add, defaulting to range.

Example (project-authored): `=SUMIF(C2:C100,"North",H2:H100)`

Use when: sum one category; total sales for one region or condition

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Use matching range sizes. Quote text or comparison criteria; use ">"&J2 for a threshold stored in J2.

Source: https://support.microsoft.com/en-us/excel/functions/sumif-function

## SUMIFS

Purpose: Adds the cells in a range that meet multiple criteria

Syntax: `=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

Arguments: sum_range: cells to add; criteria_range1: cells to test; criteria1: condition; additional pairs: optional conditions.

Example (project-authored): `=SUMIFS(H2:H100,C2:C100,"North",D2:D100,"Toys")`

Use when: sum with two or more conditions; sales for a category in a region

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: All ranges must have the same dimensions. Conditions are combined with AND; sum_range comes first.

Source: https://support.microsoft.com/en-us/excel/functions/sumifs-function

## SUMPRODUCT

Purpose: Returns the sum of the products of corresponding array components

Syntax: `=SUMPRODUCT(array1, [array2], ...)`

Arguments: array1: first range or array; array2: optional additional array multiplied element by element.

Example (project-authored): `=SUMPRODUCT(F2:F100,G2:G100)`

Use when: total quantity times unit price; weighted sums

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: All arrays must have the same dimensions. Prefer bounded ranges to whole columns.

Source: https://support.microsoft.com/en-us/excel/functions/sumproduct-function

## AVERAGE

Purpose: Returns the average of its arguments

Syntax: `=AVERAGE(number1, [number2], ...)`

Arguments: number1: first number or range; number2: optional additional number or range.

Example (project-authored): `=AVERAGE(H2:H100)`

Use when: average sales; arithmetic mean

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Referenced blanks and text are ignored; zeros are included. No numeric values gives #DIV/0!.

Source: https://support.microsoft.com/en-us/excel/functions/average-function

## AVERAGEIF

Purpose: Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria

Syntax: `=AVERAGEIF(range, criteria, [average_range])`

Arguments: range: cells to test; criteria: condition; average_range: cells to average, defaulting to range.

Example (project-authored): `=AVERAGEIF(C2:C100,"North",H2:H100)`

Use when: average for one category or condition

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Use aligned ranges. No matching numeric values gives #DIV/0!.

Source: https://support.microsoft.com/en-us/excel/functions/averageif-function

## AVERAGEIFS

Purpose: Returns the average (arithmetic mean) of all cells that meet multiple criteria

Syntax: `=AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

Arguments: average_range: cells to average; criteria_range1: cells to test; criteria1: condition; additional pairs: optional conditions.

Example (project-authored): `=AVERAGEIFS(H2:H100,C2:C100,"North",D2:D100,"Toys")`

Use when: average with several filters

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: All ranges must have the same dimensions. Conditions use AND. No matching numeric values gives #DIV/0!.

Source: https://support.microsoft.com/en-us/excel/functions/averageifs-function

## COUNT

Purpose: Counts how many numbers are in the list of arguments

Syntax: `=COUNT(value1, [value2], ...)`

Arguments: value1: first value or range; value2: optional additional value or range.

Example (project-authored): `=COUNT(H2:H100)`

Use when: count numeric cells

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: In referenced ranges, counts numbers and Excel dates; ignores text and blanks.

Source: https://support.microsoft.com/en-us/excel/functions/count-function

## COUNTA

Purpose: Counts how many values are in the list of arguments

Syntax: `=COUNTA(value1, [value2], ...)`

Arguments: value1: first value or range; value2: optional additional value or range.

Example (project-authored): `=COUNTA(A2:A100)`

Use when: count non-empty cells; number of populated rows

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Counts text, errors, and formulas returning an empty string. It is not a reliable count of visibly nonblank cells.

Source: https://support.microsoft.com/en-us/excel/functions/counta-function

## COUNTBLANK

Purpose: Counts the number of blank cells within a range

Syntax: `=COUNTBLANK(range)`

Arguments: range: cells to check for blanks.

Example (project-authored): `=COUNTBLANK(I2:I100)`

Use when: count missing values or blank cells

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Counts empty cells and formulas returning an empty string; does not count zero.

Source: https://support.microsoft.com/en-us/excel/functions/countblank-function

## COUNTIF

Purpose: Counts the number of cells within a range that meet the given criteria

Syntax: `=COUNTIF(range, criteria)`

Arguments: range: cells to test; criteria: number, text, reference, or comparison condition.

Example (project-authored): `=COUNTIF(H2:H100,">500")`

Use when: count matching rows; how many values exceed a threshold

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Text matching is case-insensitive. * matches any text, ? one character, and ~ escapes either wildcard.

Source: https://support.microsoft.com/en-us/excel/get-started/use-the-countif-function-in-microsoft-excel

## COUNTIFS

Purpose: Counts the number of cells within a range that meet multiple criteria

Syntax: `=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

Arguments: criteria_range1: cells to test; criteria1: condition; additional pairs: optional conditions.

Example (project-authored): `=COUNTIFS(C2:C100,"North",H2:H100,">500")`

Use when: count rows satisfying multiple conditions

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: All criteria ranges must have the same dimensions. Conditions are combined with AND.

Source: https://support.microsoft.com/en-us/excel/functions/countifs-function

## MAX

Purpose: Returns the maximum value in a list of arguments

Syntax: `=MAX(number1, [number2], ...)`

Arguments: number1: first number or range; number2: optional additional number or range.

Example (project-authored): `=MAX(H2:H100)`

Use when: highest number; largest sale

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Referenced blanks and text are ignored; returns 0 if there are no numbers.

Source: https://support.microsoft.com/en-us/excel/functions/max-function

## MIN

Purpose: Returns the minimum value in a list of arguments

Syntax: `=MIN(number1, [number2], ...)`

Arguments: number1: first number or range; number2: optional additional number or range.

Example (project-authored): `=MIN(H2:H100)`

Use when: lowest number; smallest sale

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Referenced blanks and text are ignored; returns 0 if there are no numbers.

Source: https://support.microsoft.com/en-us/excel/functions/min-function

## MAXIFS

Purpose: Returns the maximum value among cells specified by a given set of conditions or criteria

Syntax: `=MAXIFS(max_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

Arguments: max_range: cells containing candidate values; criteria_range1: cells to test; criteria1: condition; additional pairs: optional conditions.

Example (project-authored): `=MAXIFS(H2:H100,C2:C100,"North")`

Use when: largest value for a matching group

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2019 and later, including Microsoft 365; avoid perpetual Excel 2016.

Note: All ranges must have the same dimensions. Returns 0 when no cells match.

Source: https://support.microsoft.com/en-us/excel/functions/maxifs-function

## MINIFS

Purpose: Returns the minimum value among cells specified by a given set of conditions or criteria

Syntax: `=MINIFS(min_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

Arguments: min_range: cells containing candidate values; criteria_range1: cells to test; criteria1: condition; additional pairs: optional conditions.

Example (project-authored): `=MINIFS(H2:H100,C2:C100,"North")`

Use when: smallest value for a matching group

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2019 and later, including Microsoft 365; avoid perpetual Excel 2016.

Note: All ranges must have the same dimensions. Returns 0 when no cells match.

Source: https://support.microsoft.com/en-us/excel/functions/minifs-function

## LARGE

Purpose: Returns the k-th largest value in a data set

Syntax: `=LARGE(array, k)`

Arguments: array: numeric data; k: rank from largest, where 1 means the largest.

Example (project-authored): `=LARGE(H2:H100,3)`

Use when: second or third largest value; top value at a rank

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: k must be between 1 and the count of numeric values; otherwise #NUM! is returned.

Source: https://support.microsoft.com/en-us/excel/functions/large-function

## SMALL

Purpose: Returns the k-th smallest value in a data set

Syntax: `=SMALL(array, k)`

Arguments: array: numeric data; k: rank from smallest, where 1 means the smallest.

Example (project-authored): `=SMALL(H2:H100,3)`

Use when: second or third smallest value

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: k must be between 1 and the count of numeric values; otherwise #NUM! is returned.

Source: https://support.microsoft.com/en-us/excel/functions/small-function

## RANK.EQ

Purpose: Returns the rank of a number in a list of numbers

Syntax: `=RANK.EQ(number, ref, [order])`

Arguments: number: value to rank; ref: comparison range; order: 0 or omitted for descending, nonzero for ascending.

Example (project-authored): `=RANK.EQ(H2,$H$2:$H$100,0)`

Use when: rank sales; rank each row against a fixed range

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Ties receive the same rank, leaving gaps in later ranks. Keep the comparison range fixed when filling down.

Source: https://support.microsoft.com/en-us/excel/functions/rank-eq-function

## IF

Purpose: Specifies a logical test to perform

Syntax: `=IF(logical_test, value_if_true, [value_if_false])`

Arguments: logical_test: condition; value_if_true: result when true; value_if_false: optional result when false.

Example (project-authored): `=IF(H2>500,"High","Low")`

Use when: label or flag rows according to a condition

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Quote text results. Use AND or OR inside logical_test for multiple conditions.

Source: https://support.microsoft.com/en-us/excel/functions/if-function

## IFS

Purpose: Checks whether one or more conditions are met and returns a value that corresponds to the first TRUE condition

Syntax: `=IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2], ...)`

Arguments: logical_test1: first condition; value_if_true1: its result; additional pairs: later conditions and their results.

Example (project-authored): `=IFS(H2>=1000,"High",H2>=500,"Medium",TRUE,"Low")`

Use when: classify values into multiple bands or grades

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2019 and later, including Microsoft 365; avoid perpetual Excel 2016.

Note: The first true condition wins. A final TRUE condition supplies a fallback; otherwise no match returns #N/A.

Source: https://support.microsoft.com/en-us/excel/functions/ifs-function

## AND

Purpose: Returns TRUE if all of its arguments are TRUE

Syntax: `=AND(logical1, [logical2], ...)`

Arguments: logical1: first condition; logical2: optional additional condition.

Example (project-authored): `=AND(F2>10,G2<50)`

Use when: require all conditions to be true

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Often used inside IF: =IF(AND(F2>10,G2<50),"Yes","No").

Source: https://support.microsoft.com/en-us/excel/functions/and-function

## OR

Purpose: Returns TRUE if any argument is TRUE

Syntax: `=OR(logical1, [logical2], ...)`

Arguments: logical1: first condition; logical2: optional additional condition.

Example (project-authored): `=OR(F2>10,G2<50)`

Use when: require at least one condition to be true

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Often used inside IF: =IF(OR(F2>10,G2<50),"Yes","No").

Source: https://support.microsoft.com/en-us/excel/functions/or-function

## IFERROR

Purpose: Returns a value you specify if a formula evaluates to an error; otherwise, returns the result of the formula

Syntax: `=IFERROR(value, value_if_error)`

Arguments: value: expression to evaluate; value_if_error: fallback for any Excel formula error.

Example (project-authored): `=IFERROR(H2/I2,0)`

Use when: return a fallback for errors; avoid division-by-zero errors

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: The fallback 0 is a chosen policy, not a computed value. Use IFNA if only missing matches should be handled.

Source: https://support.microsoft.com/en-us/excel/functions/iferror-function

## IFNA

Purpose: Returns the value you specify if the expression resolves to #N/A, otherwise returns the result of the expression

Syntax: `=IFNA(value, value_if_na)`

Arguments: value: expression to evaluate; value_if_na: fallback only for #N/A.

Example (project-authored): `=IFNA(MATCH(A2,$K$2:$K$100,0),"Not found")`

Use when: return a fallback for a not-found lookup

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Other errors, including #DIV/0! and #VALUE!, are not replaced.

Source: https://support.microsoft.com/en-us/excel/functions/ifna-function

## VLOOKUP

Purpose: Looks in the first column of an array and moves across the row to return the value of a cell

Syntax: `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`

Arguments: lookup_value: search key; table_array: lookup table; col_index_num: return column counted from 1; range_lookup: FALSE for exact, TRUE or omitted for approximate.

Example (project-authored): `=VLOOKUP(A2,$K$2:$M$100,2,FALSE)`

Use when: look up an ID in the first column of a table

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Searches only the first table column and returns to its right. Use FALSE for unsorted exact lookups; TRUE requires ascending keys.

Source: https://support.microsoft.com/en-us/excel/functions/vlookup-function

## XLOOKUP

Purpose: Searches a range or an array, and returns an item corresponding to the first match it finds. If a match doesn't exist, then XLOOKUP can return the closest (approximate) match

Syntax: `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`

Arguments: lookup_value: search key; lookup_array: search range; return_array: result range; if_not_found: optional fallback; match_mode: optional match type; search_mode: optional search direction.

Example (project-authored): `=XLOOKUP(A2,$K$2:$K$100,$L$2:$L$100,"Not found")`

Use when: find a matching ID and return a value from another column

Usage: One result per row; fill down with relative row references.

Compatibility: Microsoft 365, Excel 2021, or Excel 2024; unavailable in perpetual Excel 2016/2019.

Note: Defaults to an exact first match. Search and return ranges must align. Use INDEX with MATCH for older Excel.

Source: https://support.microsoft.com/en-us/excel/functions/xlookup-function

## INDEX

Purpose: Uses an index to choose a value from a reference or array

Syntax: `=INDEX(array, row_num, [column_num])`

Arguments: array: source range; row_num: row position; column_num: optional column position. This entry covers the array form.

Example (project-authored): `=INDEX($H$2:$H$100,3)`

Use when: return a value at a given position or combine with MATCH

Usage: Single summary cell; do not fill down.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: A row position is relative to the range: position 3 in H2:H100 returns H4.

Source: https://support.microsoft.com/en-us/excel/functions/index-function

## MATCH

Purpose: Looks up values in a reference or array

Syntax: `=MATCH(lookup_value, lookup_array, [match_type])`

Arguments: lookup_value: search key; lookup_array: one row or column; match_type: 0 for exact, 1 or omitted for approximate ascending, -1 for approximate descending.

Example (project-authored): `=MATCH(A2,$K$2:$K$100,0)`

Use when: find the position of an exact match

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Returns a position, not the cell value. Approximate modes require sorting; use 0 for unsorted IDs.

Source: https://support.microsoft.com/en-us/excel/functions/match-function

## ROUND

Purpose: Rounds a number to a specified number of digits

Syntax: `=ROUND(number, num_digits)`

Arguments: number: value to round; num_digits: decimal places, with 0 for integers and negative values for tens or hundreds.

Example (project-authored): `=ROUND(H2,2)`

Use when: round decimal places

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Source: https://support.microsoft.com/en-us/excel/functions/round-function

## ROUNDUP

Purpose: Rounds a number up, away from zero

Syntax: `=ROUNDUP(number, num_digits)`

Arguments: number: value to round; num_digits: decimal places, with 0 for integers and negative values for tens or hundreds.

Example (project-authored): `=ROUNDUP(H2,0)`

Use when: always round away from zero

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Away from zero also applies to negatives: =ROUNDUP(-3.2,0) returns -4.

Source: https://support.microsoft.com/en-us/excel/functions/roundup-function

## ROUNDDOWN

Purpose: Rounds a number down, toward zero

Syntax: `=ROUNDDOWN(number, num_digits)`

Arguments: number: value to round; num_digits: decimal places, with 0 for integers and negative values for tens or hundreds.

Example (project-authored): `=ROUNDDOWN(H2,0)`

Use when: always round toward zero

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Toward zero also applies to negatives: =ROUNDDOWN(-3.2,0) returns -3.

Source: https://support.microsoft.com/en-us/excel/functions/rounddown-function

## TRIM

Purpose: Removes spaces from text

Syntax: `=TRIM(text)`

Arguments: text: text value or cell to clean.

Example (project-authored): `=TRIM(E2)`

Use when: remove leading, trailing, and repeated ordinary spaces

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Removes leading/trailing ordinary spaces and reduces repeated spaces to one; does not remove nonbreaking spaces (character 160).

Source: https://support.microsoft.com/en-us/excel/functions/trim-function

## UPPER

Purpose: Converts text to uppercase

Syntax: `=UPPER(text)`

Arguments: text: text value or cell to convert.

Example (project-authored): `=UPPER(E2)`

Use when: convert text to uppercase

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Source: https://support.microsoft.com/en-us/excel/functions/upper-function

## LOWER

Purpose: Converts text to lowercase

Syntax: `=LOWER(text)`

Arguments: text: text value or cell to convert.

Example (project-authored): `=LOWER(E2)`

Use when: convert text to lowercase

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Source: https://support.microsoft.com/en-us/excel/functions/lower-function

## PROPER

Purpose: Capitalizes the first letter in each word of a text value

Syntax: `=PROPER(text)`

Arguments: text: text value or cell to convert.

Example (project-authored): `=PROPER(E2)`

Use when: capitalize the first letter in each word

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Also lowercases other letters; can alter acronyms and intentional capitalization.

Source: https://support.microsoft.com/en-us/excel/functions/proper-function

## CONCAT

Purpose: Combines the text from multiple ranges and/or strings, but it doesn't provide the delimiter or IgnoreEmpty arguments

Syntax: `=CONCAT(text1, [text2], ...)`

Arguments: text1: first text value or range; text2: optional additional text value or range.

Example (project-authored): `=CONCAT(C2," - ",D2)`

Use when: join text from several cells

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2019 and later, including Microsoft 365; avoid perpetual Excel 2016.

Note: No automatic separator; insert literal separators explicitly. Older Excel can use =C2&" - "&D2.

Source: https://support.microsoft.com/en-us/excel/functions/concat-function

## TEXTJOIN

Purpose: Combines the text from multiple ranges and/or strings

Syntax: `=TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)`

Arguments: delimiter: separator text; ignore_empty: TRUE to skip empty cells; text1: first text value or range; text2: optional additional text.

Example (project-authored): `=TEXTJOIN(", ",TRUE,C2:E2)`

Use when: join text using a delimiter while optionally ignoring blanks

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2019 and later, including Microsoft 365; avoid perpetual Excel 2016.

Note: ignore_empty=TRUE skips empty cells. Supply delimiters in straight double quotes.

Source: https://support.microsoft.com/en-us/excel/functions/textjoin-function

## TEXT

Purpose: Formats a number and converts it to text

Syntax: `=TEXT(value, format_text)`

Arguments: value: number or Excel date; format_text: quoted Excel number-format code.

Example (project-authored): `=TEXT(B2,"yyyy-mm")`

Use when: format a date or number as text

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: The result is text, not a numeric value. For numeric calculations, retain the original value and apply cell formatting.

Source: https://support.microsoft.com/en-us/excel/functions/text-function

## YEAR

Purpose: Converts a serial number to a year

Syntax: `=YEAR(serial_number)`

Arguments: serial_number: valid Excel date value or reference.

Example (project-authored): `=YEAR(B2)`

Use when: extract the year from a date

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: B2 must contain a real Excel date, not ambiguous text.

Source: https://support.microsoft.com/en-us/excel/functions/year-function

## MONTH

Purpose: Converts a serial number to a month

Syntax: `=MONTH(serial_number)`

Arguments: serial_number: valid Excel date value or reference.

Example (project-authored): `=MONTH(B2)`

Use when: extract the month number from a date

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Returns a number from 1 to 12. B2 must contain a real Excel date.

Source: https://support.microsoft.com/en-us/excel/functions/month-function

## DAY

Purpose: Converts a serial number to a day of the month

Syntax: `=DAY(serial_number)`

Arguments: serial_number: valid Excel date value or reference.

Example (project-authored): `=DAY(B2)`

Use when: extract the day of the month from a date

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Returns a number from 1 to 31. B2 must contain a real Excel date.

Source: https://support.microsoft.com/en-us/excel/functions/day-function

## TODAY

Purpose: Returns the serial number of today's date

Syntax: `=TODAY()`

Arguments: No arguments.

Example (project-authored): `=TODAY()`

Use when: use the current date

Usage: Single current-date cell; may also be used inside a per-row formula.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: Updates when Excel recalculates. Returns a date serial; apply a date format.

Source: https://support.microsoft.com/en-us/excel/functions/today-function

## DATEDIF

Purpose: Calculates the number of days, months, or years between two dates. This function is useful in formulas where you need to calculate an age

Syntax: `=DATEDIF(start_date, end_date, unit)`

Arguments: start_date: earlier date; end_date: later date; unit: "d" for days, "m" for complete months, "y" for complete years.

Example (project-authored): `=DATEDIF(B2,TODAY(),"d")`

Use when: calculate age or elapsed days, months, or years

Usage: One result per row; fill down with relative row references.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: start_date later than end_date returns #NUM!. Avoid unit "md" due to known limitations. For elapsed days, subtraction is simpler.

Source: https://support.microsoft.com/en-us/excel/functions/datedif-function

## FILTER

Purpose: Filters a range of data based on criteria you define

Syntax: `=FILTER(array, include, [if_empty])`

Arguments: array: source data; include: Boolean mask matching the relevant height or width; if_empty: optional result when no rows match.

Example (project-authored): `=FILTER(A2:I100,C2:C100="North","No matches")`

Use when: return only rows matching a condition

Usage: Dynamic array result; enter once and let the result spill.

Compatibility: Microsoft 365, Excel 2021, or Excel 2024; unavailable in perpetual Excel 2016/2019.

Note: Enter once outside an Excel Table with empty space for results; do not fill down. Blocked output gives #SPILL!.

Source: https://support.microsoft.com/en-us/excel/functions/filter-function

## UNIQUE

Purpose: Returns a list of unique values in a list or range

Syntax: `=UNIQUE(array, [by_col], [exactly_once])`

Arguments: array: source data; by_col: FALSE or omitted to compare rows; exactly_once: TRUE for values occurring once, FALSE or omitted for distinct values.

Example (project-authored): `=UNIQUE(C2:C100)`

Use when: list distinct values or eliminate duplicates from a result

Usage: Dynamic array result; enter once and let the result spill.

Compatibility: Microsoft 365, Excel 2021, or Excel 2024; unavailable in perpetual Excel 2016/2019.

Note: Enter once outside an Excel Table with empty space; do not fill down. exactly_once=TRUE differs from a distinct-value list.

Source: https://support.microsoft.com/en-us/excel/functions/unique-function

## SORT

Purpose: Sorts the contents of a range or array

Syntax: `=SORT(array, [sort_index], [sort_order], [by_col])`

Arguments: array: source data; sort_index: sort column or row, default 1; sort_order: 1 ascending or -1 descending; by_col: FALSE or omitted to sort rows.

Example (project-authored): `=SORT(H2:H100,1,-1)`

Use when: sort an array in ascending or descending order

Usage: Dynamic array result; enter once and let the result spill.

Compatibility: Microsoft 365, Excel 2021, or Excel 2024; unavailable in perpetual Excel 2016/2019.

Note: Enter once outside an Excel Table with empty space; do not fill down. Sort all columns together to preserve row relationships.

Source: https://support.microsoft.com/en-us/excel/functions/sort-function

## Recipe: Profit and margin

Purpose: Profit is revenue minus cost. Profit margin is profit divided by revenue, not cost.

Profit formula: `=H2-I2`

Margin formula: `=IF(H2=0,"",(H2-I2)/H2)`

Use when: profit; gross profit; profit margin; revenue minus cost

Usage: One result per row; fill down from row 2.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: H2 is revenue and I2 is cost. Margin is undefined when revenue is zero, so this example returns blank. Format margin as Percentage; do not multiply by 100.

Source: project-authored recipe.

## Recipe: Percentage of total

Purpose: Calculate each row's share of a fixed total.

Formula pattern: `=IF(SUM($H$2:$H$100)=0,"",H2/SUM($H$2:$H$100))`

Use when: share of total; contribution percentage; proportion of sales

Usage: One result per row; fill down from row 2.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: H2 is the row value. The denominator remains fixed when filled down. A zero total returns blank. Format as Percentage.

Source: project-authored recipe.

## Recipe: Percentage change

Purpose: Calculate relative growth or decline from an old value to a new value.

Formula pattern: `=IF(H2=0,"",(H3-H2)/H2)`

Use when: percentage change; growth rate; increase or decrease from the previous period

Usage: One result per newer period; fill down from row 3.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: H2 is old and H3 is new. Enter for the newer period (row 3) and fill down from there. Zero baseline returns blank. Format as Percentage; negative baselines require an agreed interpretation.

Source: project-authored recipe.

## Recipe: Running total

Purpose: Create a cumulative sum from the first data row through the current row.

Formula pattern: `=SUM($H$2:H2)`

Use when: running total; cumulative sales; cumulative sum

Usage: One result per row; fill down from row 2.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: The first reference is fixed and the final row expands when filled down. Row order determines the cumulative sequence.

Source: project-authored recipe.

## Recipe: Flag duplicates

Purpose: Flag later occurrences of an ID while leaving its first occurrence unmarked.

Formula pattern: `=IF(A2="","",IF(COUNTIF($A$2:A2,A2)>1,"Duplicate",""))`

Use when: duplicate ID; repeated record; mark duplicates after the first occurrence

Usage: One result per row; fill down from row 2.

Compatibility: Excel 2016 and later, including Microsoft 365.

Note: A2 is an ID. Blank IDs remain unmarked. This example assumes IDs do not contain wildcard characters * or ?; COUNTIF text matching is case-insensitive.

Source: project-authored recipe.

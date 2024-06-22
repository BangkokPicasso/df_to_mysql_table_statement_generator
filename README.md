# df_to_mysql_table_statement_generator
Converting a Pandas DataFrame into a MySQL `CREATE TABLE` statement.

The script inspects the DataFrame's columns and their respective data types to construct the appropriate SQL data types for each column.

## Features

- Automatically detects column data types from a Pandas DataFrame.
- Converts these data types to their MySQL equivalents.
- Generates a `CREATE TABLE` statement with appropriate column names and data types.
- Handles common data types including integers, floats, booleans, and strings.

## How to Use
1. **Install Required Libraries**: Ensure you have `pandas` installed.
   ```sh
     pip install pandas
    ```
2. Replace the example DataFrame (data dictionary) with your actual data.
3. Run the script:
   ```sh
     python df_to_mysql_table_statement_generator.py
    ```
4. Copy the generated SQL statement from the console output.
5. Paste the SQL statement into your MySQL client (e.g., MySQL Workbench, command line interface).
6. Execute the SQL statement to create the table in your MySQL database.
   
## Example
Here is an example DataFrame used in the script:
   ```
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'height': [5.5, 6.0, 5.8],
    'is_member': [True, False, True]
}

   ```
When you run the script, it generates the following SQL statement:
   ```example DataFrame
CREATE TABLE quality_dashboard.t02r_sampling (
    id INT,
    name VARCHAR(40),
    age INT,
    height FLOAT,
    is_member BOOLEAN
);

   ```

## Related Repositories
* [Excel_to_MySQL_Importer](https://github.com/BangkokPicasso/Excel_to_MySQL_Importer): a Python script to import data from an Excel file into a MySQL database
* [export_mysql_data_to_xlsx](https://github.com/BangkokPicasso/export_mysql_data_to_xlsx): Export MySQL Data to Excel
  
## Prerequisites
* Python 3.x
* Necessary Python libraries: pandas


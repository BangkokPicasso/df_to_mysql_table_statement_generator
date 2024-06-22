import pandas as pd

# Example DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'height': [5.5, 6.0, 5.8],
    'is_member': [True, False, True]
}
# SQL statement to create MySQL table
df = pd.DataFrame(data)

def main():
    # SQL statement to create MySQL table
    table_name = 'quality_dashboard.t02r_sampling'
    create_table_sql = f"CREATE TABLE {table_name} ("

    # Get column names and data types
    for col_name, dtype in df.dtypes.items():
        sql_type = ''
        if dtype == 'int64':
            sql_type = 'INT'
        elif dtype == 'float64':
            sql_type = 'FLOAT'
        elif dtype == 'bool':
            sql_type = 'BOOLEAN'
        else:
            sql_type = 'VARCHAR(40)'  # Assuming other columns are string type, adjust size as needed
        # Use lowercase column names
        create_table_sql += f"{col_name.lower()} {sql_type}, "

    # Remove the last comma and space
    create_table_sql = create_table_sql[:-2]

    # Add the closing bracket for the table
    create_table_sql += ");"

    print(create_table_sql)

if __name__ == '__main__':
    main()

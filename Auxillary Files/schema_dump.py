from sqlalchemy import create_engine, inspect

# Use your database connection string
engine = create_engine('mysql+mysqlconnector://server2:T3t0npack@192.168.1.28/school10?charset=utf8mb4&collation=utf8mb4_general_ci')

inspector = inspect(engine)

# Get table names
tables = inspector.get_table_names()

for table_name in tables:
    columns = inspector.get_columns(table_name)
    print(f"\nTable: {table_name}")
    for column in columns:
        print(f"  {column['name']}: {column['type']}")
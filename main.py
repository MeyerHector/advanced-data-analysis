import psycopg2
import pandas as pd
data = 'employeeData.csv'
df = pd.read_csv(data)
print(df.head())
try:
    # Conectar a la base de datos PostgreSQL
    connection = psycopg2.connect(
        dbname="CompanyData",
        user="meyer",
        password="000000",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()
    
    # Ejecutar una consulta
    create_table_query = '''
        DROP TABLE IF EXISTS EmployeePerformance;

        CREATE TABLE EmployeePerformance (
            id SERIAL PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            department TEXT NOT NULL,
            performance_score DECIMAL(3, 1) NOT NULL,
            years_with_company INTEGER NOT NULL,
            salary DECIMAL(6, 2) NOT NULL
        );
    '''
    cursor.execute(create_table_query)
    
    for index, row in df.iterrows():
        insert_query = '''
        INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (
            row['employee_id'],
            row['department'],
            row['performance_score'],
            row['years_with_company'],
            row['salary']
        ))

    # Obtener el resultado
    connection.commit()

    print("Tabla de rendimiento de empleados creada exitosamente.")

except Exception as e:
    print(f"Error al conectar a PostgreSQL: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada.")

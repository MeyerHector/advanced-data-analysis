import psycopg2

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
    DROP TABLE IF EXISTS employeeperformance;
    
    CREATE TABLE EmployeePerformance (
        id SERIAL PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        department TEXT NOT NULL,
        performance_score DECIMAL(2, 1) NOT NULL,
        years_with_company INTEGER NOT NULL,
        salary DECIMAL(10, 2) NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    
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

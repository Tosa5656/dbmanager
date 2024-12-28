import sqlite3

class tableElement:
    def __init__(self, name, element_type, additional):
        self.name = name
        self.element_type = element_type
        self.additional = additional

class dbmngr:
    def __init__(self):
        pass
        
    def connect(self, db):
        self.db = db
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
    
    def create_table(self, table_name, elements):
        columns = []
        
        for element in elements:
            column_def = f"{element.name} {element.element_type}"
            
            if element.additional:
                column_def += f" {element.additional}"
                
            columns.append(column_def)
        
        query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
        self.cursor.execute(query)

    
    def test(self):
        self.cursor.execute("""CREATE TABLE people
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT, 
                age INTEGER)
            """)
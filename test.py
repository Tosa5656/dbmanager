from dbmanager import dbmanager

if __name__ == "__main__":
    db = dbmanager.dbmngr()
    db.connect("test/test.db")
    db.create_table("test",{dbmanager.tableElement("id", "INTEGER", "PRIMARY KEY AUTOINCREMENT"), dbmanager.tableElement("name", "TEXT", "")})
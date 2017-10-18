import pyodbc


class MsAccessConnector(object):
    connection = None
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Distr\tmp.accdb;'
    )

    @classmethod
    def get_connection(cls, New=False):
        if New or not cls.connection:
            try:
                cls.connection = pyodbc.connect(cls.conn_str)
            except Exception as e:
                print(e)
            return cls.connection

    @classmethod
    def exec_q(cls, q_text):
        conn = cls.get_connection()
        try:
            cursor = conn.cursor()
        except:
            conn = cls.get_connection(New=True)
            cursor = conn.cursor()
        cursor.execute(q_text)
        rez = cursor.fetchall()
        conn.commit()
        cursor.close()
        return rez



def read_streets():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Distr\tmp.accdb;'
    )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    crsr.execute("SELECT distinct Street FROM otsaldk")
    row = crsr.fetchall()
    crsr.close()
    cnxn.close()
    for k in row:
        if k[0]:
            yield k


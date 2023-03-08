import pymysql
import config
import json

con = pymysql.connect(host=config.HOST, user=config.USER, 
    password=config.PASSWORD, database=config.DB)

with con.cursor() as cur:
    cur = con.cursor()

    def all():
        cur.execute("SELECT * FROM routes")
        rows = cur.fetchall()
        return rows
    
    def get_row(id):
        cur.execute("SELECT * FROM routes WHERE id=%s",id)
        row = cur.fetchone()
        return [row[2],row[0],json.loads(row[1])]
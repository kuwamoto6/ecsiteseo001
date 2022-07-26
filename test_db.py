import psycopg2

# 接続情報
dsn = "dbname=de5m80kjjkv3cj host=ec2-34-233-115-14.compute-1.amazonaws.com user=abiiwxvsfsgqub password=f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956"

conn = psycopg2.connect(dsn)  # コネクション
cur = conn.cursor()  # カーサー

cur.execute("select version()") # クエリの実行
print(cur.fetchone()) 

cur.execute("INSERT INTO aequalis (day) VALUES ('2022/07/26')")
cur.execute("INSERT INTO aequalis (rakuten) VALUES ('テスト')")
cur.execute("INSERT INTO aequalis (amazon) VALUES ('テスト')")
cur.execute("INSERT INTO aequalis (yahoo) VALUES ('テスト')")
conn.commit()

# コネクション等は閉じる。
cur.close()
conn.close()
import os
import psycopg2

DATABASE_URL = os.environ.get('postgres://abiiwxvsfsgqub:f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956@ec2-34-233-115-14.compute-1.amazonaws.com:5432/de5m80kjjkv3cj')

day = '2022/07/22'
rakuten = 'テスト'

with psycopg2.connect(DATABASE_URL) as conn:
    with conn.cursor() as curs:
        curs.execute(
            "INSERT INTO aequalis(day, rakuten) VALUES(%s, %s)", (day, rakuten))
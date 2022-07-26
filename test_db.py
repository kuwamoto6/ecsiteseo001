import psycopg2

db = PostgreConnect (
        'ec2-34-233-115-14.compute-1.amazonaws.com',#Host
        'de5m80kjjkv3cj',#Database
        'public',#schema
        'abiiwxvsfsgqub',#User
        'f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956',#Password
        port=5432#Port
        )

#指定テーブルへの列追加
db.add_column('aequalis',['day 2022/07/26','rakuten test'])
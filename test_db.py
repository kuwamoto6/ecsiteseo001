import psycopg2

connector =  psycopg2.connect('postgres://abiiwxvsfsgqub:f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956@ec2-34-233-115-14.compute-1.amazonaws.com:5432/de5m80kjjkv3cj'.format( 
                user='abiiwxvsfsgqub',        #ユーザ
                password='f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956',  #パスワード
                host='ec2-34-233-115-14.compute-1.amazonaws.com',       #ホスト名
                port='5432',            #ポート
                dbname='de5m80kjjkv3cj'))    #データベース名

cursor = connector.cursor()

#指定テーブルへの列追加
cursor.add_column('aequalis',['day 2022/07/26','rakuten test'])
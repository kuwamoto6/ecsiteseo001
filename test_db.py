import psycopg2
 
class PostgreConnect:
    '''
    ostgreSQのヘルパークラス
    Parameters
    '''
    GET_TABLE_LIST_QUERY = "SELECT t.* FROM (SELECT TABLENAME,SCHEMANAME,'table' as TYPE from PG_TABLES UNION SELECT VIEWNAME,SCHEMANAME,'view' as TYPE from PG_VIEWS) t WHERE TABLENAME LIKE LOWER('{0}') and SCHEMANAME like LOWER('{1}') and TYPE like LOWER('{2}')"
    GET_COLUMN_LIST_QUERY = "SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME like LOWER('{0}') and TABLE_SCHEMA like LOWER('{1}') ORDER BY ORDINAL_POSITION"
    GET_ALTER_TABLE_QUERY = "ALTER TABLE {0} ADD {1}"
    GET_RENAME_TABLE_QUERY = "alter table {0} rename to {1}"
    
    def __init__(self,host,dbname,scheme,user,password,port=5432):
        '''
        DBの接続情報を保持する
        Parameters
        ----------
        host : str
        　  ホスト名
        dbname : str
            DB名
        scheme : str
            スキーマ名
        user : str
            ユーザー名
        password : str
            パスワード
        port : integer
            ポート
        '''
        self.host = 'ec2-34-233-115-14.compute-1.amazonaws.com'
        self.dbname = 'de5m80kjjkv3cj'
        self.scheme ='public' 
        self.user = 'abiiwxvsfsgqub'
        self.password = 'f73007982168170d1171b2f3bc07a95e5d7dc50df1e321168badcd8f86ceb956'
        self.port = 5432
    
    def __connect(self):
        return psycopg2.connect("host='{0}' port={1} dbname={2} user={3} password='{4}'".format(self.host,self.port,self.dbname,self.user,self.password))
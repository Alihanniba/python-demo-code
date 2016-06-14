# _*_ coding:utf-8 _*_
# python operate mysql database
import /MySQL-python-1.2.3/MySQLdb

#数据库名称
DATABASE_NAME = ''
#host = 'localhost' or '127.0.0.1'
HOST = ''
#端口号
POST = ''
#用户名称
USER_NAME = ''
#数据库密码
PASSWORD = ''
#数据库编码
CHAR_SET = ''

#初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'video-in'
    global HOST
    HOST = 'localhost'
    global POST
    POST = '3306'
    global USER_NAME
    USER_NAME = 'root'
    global PASSWORD
    PASSWORD = '123456'
    global CHAR_SET
    CHAR_SET = 'utf8'

#获取数据库连接
def get_conn():
    init()
    return MySQLdb.connect(host = HOST,user = USER_NAME,passwd = PASSWORD,db = DATABASE_NAME,charset = CHAR_SET)

#获取curdor
def get_cursor(conn):
    return conn.cursor()

#关闭连接
def conn_close(conn):
    if conn != None:
        conn.close()

#关闭cursor
def cursor_close(cursor,conn):
    if cursor !=None:
        cursor.close()

#关闭所有
def close(cursor,conn):
    cursor_close(cursor)
    conn_close(conn)

def query_table(table_name):
    if table_name != '':
        sql = 'select * from' + table_name
        conn = get_conn()
        cursor = get_cursor(conn)
        result = cursor.excute(sql)
        for row in cursor.fetchall():
            print(row)
            for r in row  #循环每一条数据
                print(r)
        close(cursor,conn)
    else:
        print('table name is empty!')

def main():
    query_table('dy592')

if __name__ == '__main__':
    main()













import pymysql
from os.path import abspath, dirname

# configparser库用来读取ini类型的配置文件
import configparser

# =======================读取db_config.ini文件设置=======================
# 配置文件的绝对路径
# base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = base_dir.replace('\\','/')
# file_path = base_dir + "/db_config.ini"
# print(file_path)
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"
print(file_path)

# 初始化
cf = configparser.ConfigParser()
# 读取配置文件
cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
db = cf.get("mysqlconf", "db_name")


# ======== MySql base operating ===================
class HandleMySql:
    """数据库处理类"""

    def __init__(self):
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    db=db,
                                    port=int(port),
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def get_value(self, sql, args=None, is_more=False):
        """
        获取数据库的值
        :param sql: sql语句
        :param args: 其他参数
        :param is_more: 是否显示全部，默认显示一套条数据
        :return: 字典为item的列表数据
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    handle_sql = HandleMySql()
    sql = "select * from lh_sq_gg_notice where title = 88 and content = 88;"
    single_data = handle_sql.get_value(sql, is_more=True)
    print(single_data)

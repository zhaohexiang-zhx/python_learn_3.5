#!/usr/bin/env python
# coding=utf-8

import MySQLdb, time, traceback, logging

class DBOperateAction:
    def __init__(self, dbhost, dbaccount, dbpasswd, dbname, port=3306, charset="utf8"):
        self.dbhost = dbhost
        self.dbaccount = dbaccount
        self.dbpasswd = dbpasswd[::-1]
        self.dbname = dbname
        self.port = port
        self.charset = charset
        self.db_conn = ""
        self.db_cursor = ""


    def connect(self):
        try:
            self.db_conn = MySQLdb.connect(host=self.dbhost, user=self.dbaccount,
                                           passwd=self.dbpasswd, db=self.dbname,
                                           port=self.port, charset=self.charset,
                                           connect_timeout=5)
            self.db_cursor = self.db_conn.cursor()
            return True
        except MySQLdb.OperationalError:
            logging.error("Connect to "+self.dbhost+" Failed")
            logging.exception("exception message:")
            return False

    def re_connect(self):
        logging.error("connect to mysql server failed, reconnect")
        try:
            self.db_conn = MySQLdb.connect(host=self.dbhost, user=self.dbaccount,
                                           passwd=self.dbpasswd, db=self.dbname,
                                           port=self.port, charset=self.charset,
                                           connect_timeout=5)
            self.db_cursor = self.db_conn.cursor()
            return True
        except MySQLdb.OperationalError:
            logging.error("Reconnect MySQL Failed")
            return False

    def get_all_result(self, sql):
        try:
            # logging.info("Execute sql: "+sql[:500])
            logging.info("Execute sql: "+sql)
            self.db_cursor.execute(sql)
            self.db_conn.commit()
            result = self.db_cursor.fetchall()
            return result
        except MySQLdb.OperationalError:
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    self.db_cursor.execute(sql)
                    self.db_conn.commit()
                    result = self.db_cursor.fetchone()
                    logging.warn("Reconnct to "+self.dbhost+" successfuly")
                    return result
            return False

    def close_connection(self):
        self.db_conn.close()

if __name__=="__main__":
    host = "127.0.0.1"
    db_account = "root"
    db_passwd = "123456"
    db_name = "test"



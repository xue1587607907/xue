from Utils.Utils import Utilsaa


class DBApi:
    @classmethod
    def select_by_area_name(cls, area_name):
        conn = Utilsaa.get_conn()
        cursor = Utilsaa.get_cursor(conn)
        sql = "select area_id from t_area where area_name='%s'" %(area_name)
        cursor.execute(sql)
        rows = cursor.fetchall()
        Utilsaa.close(cursor, conn)
        return rows[0][0]

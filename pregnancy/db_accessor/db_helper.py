from django.db import connection


def call_proc(proc_name, *args):
    cursor = connection.cursor()
    ret = None
    try:
        cursor.callproc(proc_name, args )
        desc = cursor.description
        ret = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
    except BaseException as ex:
        print('[ERROR] {}'.format(ex))
    finally:
        cursor.close()
        return ret

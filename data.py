import sqlite3


def create():
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        "id"    TEXT,
                        "tg"    TEXT,
                        "chanel"    TEXT
                        )
                        """)
    connect.commit()


def put_info(lst_info):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("INSERT OR IGNORE INTO users VALUES(?, ?, ?);", lst_info)
    connect.commit()


def get_info(wh, info):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    print(info)
    try:
        query = f"SELECT * FROM users WHERE {wh} = ?"
        cursor.execute(query, (info,))
        q = cursor.fetchone()
        print(q)
        if len(q) == 0:
            return f"В базе не найдено ничего по {wh} {info}"
        else:
            res = "Найдено: " + str(q[0]) + " " + str(q[1]) + " " + str(q[2])
            print(res)
            return res

    except:
        return f"В базе не найдено ничего по {wh} {info}"

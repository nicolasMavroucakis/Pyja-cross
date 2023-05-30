import pymysql as mysql

connection = None
cursor = None

def connect():
    global connection
    connection = mysql.connect(user="root", password="mysqlguilherme",host="localhost",database="db_pii")
    global cursor
    cursor = connection.cursor()


def updateUserTime(userInfo, userTime, gameType):

    userId = userInfo["user_id"]

    print("userId: ", type(userId))
    print("userTime: ", type(userTime))
    print("gameType: ", type(gameType))

    check = "SELECT * FROM times WHERE user_id=%s AND game=%s"
    insert = "INSERT INTO times(user_id, time, game) VALUES(%s,%s,%s)"
    update = "UPDATE times SET time=%s WHERE user_id=%s AND game=%s"

    cursor.execute(check, (userId, gameType))
    res = cursor.fetchall()

    if len(res) == 0:
        cursor.execute(insert, (userId, userTime, gameType))
        connection.commit()
    else:
        __user_id, user_time, __gameMode = res[0]
        if userTime < user_time:
            cursor.execute(update, (userTime, userId, gameType))
            connection.commit() 

def getTimes(gameType):
    """
    SELECT * 
    FROM times
    WHERE game = 0
    INNER JOIN users
    ON times.user_id = users.user_id
    """
    sql = "SELECT * FROM times INNER JOIN users USING (user_id) WHERE game = %s ORDER BY time"
    cursor.execute(sql,(gameType))

    res = cursor.fetchall()
    return res

# def getUserId(userRa):
    query = (f"SELECT * FROM users WHERE user_ra='{userRa}'")
    cursor.execute(query)

    res = cursor.fetchall()
    if len(res) > 0:
        user_id, __user_ra, __user_password = res[0]
    else:
        insertSql = "INSERT INTO users(user_ra,user_passwor)"
        insert = (f"INSERT INTO users(user_ra,user_password) VALUES({userRa},'Teste')")
        connection.commit()
        query = (f"SELECT * FROM users WHERE user_ra={userRa}")
        cursor.execute(insert)

        cursor.execute(insert)
        res = cursor.fetchall()
        print(res)
        user_id, __user_ra, __user_password = res[0]

    return user_id

def login(ra, password):
    sql = "SELECT * FROM users WHERE user_ra = %s AND user_password = %s"
    cursor.execute(sql, (ra, password))

    res = cursor.fetchone()

    if res:
        result = {
            "user_id": res[0],
            "user_ra": res[1],
            "user_name": res[3],
            "auth": True
        }

    else:
        result = {
            "auth": False
        }

    return result

def signup(ra, password, name):
    querySql = "SELECT * FROM users WHERE user_ra = %s"
    insertSql = "INSERT INTO users(user_ra, user_password, user_name) VALUES (%s, %s, %s)"

    cursor.execute(querySql,(ra))
    res = cursor.fetchone()

    if res:
        result = { "approved": False }
    else:
        cursor.execute(insertSql,(ra, password, name))
        connection.commit()

        userId = cursor.lastrowid

        result = { "approved": True, "user_id": userId }

    return result
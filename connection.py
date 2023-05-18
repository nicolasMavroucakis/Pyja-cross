import mysql.connector as mysql

connection = None
cursor = None

def connect():
    global connection
    connection = mysql.connect(user="root", password="mysqlguilherme",host="localhost",database="db_pii")
    global cursor
    cursor = connection.cursor()


def updateUserTime(userId, userTime, gameType):

    check = (f"SELECT * FROM times WHERE user_id={userId} AND game={gameType}")
    insert = (f"INSERT INTO times(user_id, time, game) VALUES({userId},{userTime},{gameType})")
    update = (f"UPDATE times SET time={userTime} WHERE user_id={userId} AND game={gameType}")

    cursor.execute(check)
    res = cursor.fetchall()

    if len(res) == 0:
        cursor.execute(insert)
        connection.commit()
    else:
        __user_id, user_time = res[0]
        if userTime > user_time:
            cursor.execute(update)
            connection.commit() 

def getTimes(gameType):
    query = (f"SELECT * FROM times WHERE game={gameType}")
    cursor.execute(query)

    res = cursor.fetchall()
    return res

def getUserId(userRa):
    query = (f"SELECT * FROM users WHERE user_ra='{userRa}'")
    cursor.execute(query)

    res = cursor.fetchall()
    user_id, user_ra, user_password = res[0]

    return user_id

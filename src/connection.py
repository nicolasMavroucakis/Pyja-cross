import pymysql as mysql

connection = None
cursor = None

def connect(): # Cria a conexão no banco de dados
    global connection
    connection = mysql.connect(user="root", password="mysqlguilherme",host="localhost",database="db_pii")
    global cursor
    cursor = connection.cursor()


def updateUserTime(userInfo, userTime, gameType): # Atualiza o tempo do jogador

    userId = userInfo["user_id"]

    # Prepara os comandos SQL
    check = "SELECT * FROM times WHERE user_id=%s AND game=%s"
    insert = "INSERT INTO times(user_id, time, game) VALUES(%s,%s,%s)"
    update = "UPDATE times SET time=%s WHERE user_id=%s AND game=%s"

    # Checa se já existe algum tempo do usuário
    cursor.execute(check, (userId, gameType))
    res = cursor.fetchall()

    if len(res) == 0: # Caso não tenha nenhum registro, este seá inserido
        cursor.execute(insert, (userId, userTime, gameType))
        connection.commit()
    else: # Caso já exista irá checar se o atual é melhor
        __user_id, user_time, __gameMode = res[0]
        if userTime < user_time: # Caso o atual seja melhor, irá atualizar
            cursor.execute(update, (userTime, userId, gameType))
            connection.commit() 

def getTimes(gameType): # Puxa os 10 melhores tempos da database
    sql = "SELECT * FROM times INNER JOIN users USING (user_id) WHERE game = %s ORDER BY time LIMIT 10"
    cursor.execute(sql,(gameType))

    res = cursor.fetchall()
    return res

def login(ra, password): # Faz o login da conta
    sql = "SELECT * FROM users WHERE user_ra = %s AND user_password = %s"
    cursor.execute(sql, (ra, password))

    res = cursor.fetchone()

    if res: # Caso encontre algum resultado
        # Tabela com as informações importantes
        result = {
            "user_id": res[0],
            "user_ra": res[1],
            "user_name": res[3],
            "auth": True
        }

    else: # Caso não encontre nenhum resultado
        # Tabela com as informações importantes
        result = {
            "auth": False
        }

    return result

def signup(ra, password, name): # Faz o cadastro
    querySql = "SELECT * FROM users WHERE user_ra = %s"
    insertSql = "INSERT INTO users(user_ra, user_password, user_name) VALUES (%s, %s, %s)"

    # Checa se existe algum registro no RA indicado
    cursor.execute(querySql,(ra))
    res = cursor.fetchone()

    if res: # Caso exita, não irá aprovar o login
        result = { "approved": False }
    else: # Caso não exita, irá criar o login
        cursor.execute(insertSql,(ra, password, name))
        connection.commit()

        userId = cursor.lastrowid # Pega o ID do usuário

        result = { "approved": True, "user_id": userId }

    return result
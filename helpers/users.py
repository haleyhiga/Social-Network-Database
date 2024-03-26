import db

def list_users():
    # list all users
    con = db.getDatabase()
    cur = con.cursor()

    users = cur.execute("SELECT * FROM users")
    users = users.fetchall()
    if users:
        print("-->", "ALL USERS:")
        for user in users:
            print("\tID:",user[0],"EMAIL:",user[1])
    else:
        print("-->", "There are no users.")

    con.close()
    

def add_user(email):
    con = db.getDatabase()
    cur = con.cursor()

    #print(cur.execute("SELECT * FROM users").fetchall())

    error = True
    for i in email:
        if i == "@":
            error = False
    
    msg = email[-4:]
    
    if msg == ".com" and not error:
        info = cur.execute("SELECT email FROM users WHERE email = ?", (email,))
        info = info.fetchone()
        if info is None:
            cur.execute("INSERT INTO users(email) VALUES(?)", (email,))
            print("-->","Successfully created user with", email)
        else:
            print("-->", "User already exists.")

    else:
        print("-->","You have provided an invalid email address.")

    #print(cur.execute("SELECT * FROM users").fetchall())

    con.commit()
    con.close()

def delete_user(email):
    con = db.getDatabase()
    cur = con.cursor()

    # deleting issue with deleting user
    cur.execute("SELECT email FROM users WHERE email = ?", (email,))
    if cur.fetchone() == None:
        print("-->","User does not exist.")
    else:
        cur.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        user_id = cur.fetchone()[0]
        cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        print("-->",email,"with id",user_id,"has been deleted.")

    con.commit()
    con.close()
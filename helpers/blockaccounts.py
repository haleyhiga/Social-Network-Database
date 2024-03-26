import db

def list_blocked_accounts(username):
    con = db.getDatabase()
    cur = con.cursor()

    users = cur.execute("SELECT blocked_username FROM blocked_accounts WHERE username = ?", (username,))
    users = users.fetchall()
    if users:
        print("-->", username, "has blocked these accounts:")
        #print(users)
        for user in users:
            print("\t| "+user[0])
    else:
        print("-->", username,"has not blocked anyone.")

    con.commit() # added commit
    con.close()

def block_account(username, blocked_username):
    con = db.getDatabase()
    cur = con.cursor()

    info = cur.execute("SELECT username FROM accounts WHERE username = ?", (blocked_username,))
    info = info.fetchone()
    if info is None:
        print("-->","The blocked account is invalid.")
        con.close()
        return
    
    info = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    info = info.fetchone()
    if info is None:
        print("Given username does not exist.")
    else:
        cur.execute("INSERT INTO blocked_accounts (username, blocked_username) VALUES(?, ?)", (username, blocked_username,))
        print("-->",username,"has blocked",blocked_username)
    
    con.commit()
    con.close()

def remove_blocked_account(username, blocked_username):
    con = db.getDatabase()
    cur = con.cursor()

    info = cur.execute("SELECT username, blocked_username FROM blocked_accounts WHERE username = ? AND blocked_username = ?", (username,blocked_username,))
    info = info.fetchone()
    if info is None:
        print("-->",username,"has not blocked",blocked_username+".")
    else:
        cur.execute("DELETE FROM blocked_accounts WHERE username = ? AND blocked_username = ?", (username, blocked_username,))
        print("-->",username,"has unblocked",blocked_username+".")

    con.commit()
    con.close()
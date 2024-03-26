import db
import sqlite3


# list all the accounts
def list_accounts():
    con = db.getDatabase()
    cur = con.cursor()

    accounts = cur.execute("SELECT * FROM accounts")
    accounts = accounts.fetchall()
    #print(accounts)
    if accounts:
        print("-->", "ALL ACCOUNTS:")
        for acc in accounts:
            print("\tID:",acc[0],"USERNAME:",acc[2])
    else:
        print("-->", "There are no accounts.")

    con.close()


def add_account(email, username):
    con = db.getDatabase()
    cur = con.cursor()
    
    error = False

    special_chars = "!@#$%^&*()-+=\|[{}]:;'\"<>,?/"

    # check if username contains special characters
    for char in username:
        if char in special_chars:
            error = True

    if not error and len(username) <= 15:
        if email:
            # fetch the user_id from users table
            user_info = cur.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            user_id = user_info.fetchone()
            if user_id:
                user_id = user_id[0] # return first element of the tuple, NOT an object
                # check if the username is used
                existing_username = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
                existing_username = existing_username.fetchone()
                if existing_username:
                    print("-->","This username already exists.")
                else:
                    cur.execute("INSERT INTO accounts (user_id, username) VALUES(?, ?)", (user_id, username,))
                    print("-->","Successfully created account", username)
            else:
                print("-->","No user found with this email.")
        else:
            print("-->","Please provide both email and username.")
    else:
        print("-->","Please create user first.")

    con.commit()
    con.close()

def delete_account(username):
    con = db.getDatabase()
    cur = con.cursor()

    info = cur.execute("SELECT * FROM accounts WHERE username = ?", (username,))
    if info.fetchone() is None:
        print("-->","Account does not exist.")

    else:
        cur.execute("DELETE FROM accounts WHERE username = ?", (username,))

    con.commit()
    con.close()
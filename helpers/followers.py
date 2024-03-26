import db


def list_followers(username):
    con = db.getDatabase()
    cur = con.cursor()

    followers = cur.execute("SELECT follower_username FROM followers WHERE username = ?", (username,))
    followers = followers.fetchall()
    #print(followers)
    if followers:
        print("--> " +username+ "'s followers: ")
        #print(followers)
        for follower in followers:
            print("\t| "+follower[0])
    else:
        print("-->", username,"has no followers.")

    con.commit()
    con.close()

def add_follower(username, follower_username):
    con = db.getDatabase()
    cur = con.cursor()

    # follower_username
    info = cur.execute("SELECT * FROM accounts WHERE username = ?", (follower_username,))
    info = info.fetchone()

    # USER BLOCKS USER2
    # USER2 CANNOT FOLLOWER USER

    blocked = cur.execute("SELECT * FROM blocked_accounts WHERE username = ?", (follower_username,))
    blocked = blocked.fetchall()

    if len(blocked) != 0:
        blocked = blocked[0]
    for user in blocked:
        if user == username:
            print(username, "has blocked", follower_username, "unable to follow account.")
            con.close()
            return

    #print(info)
    if info is None:
        print("The follower account is invalid.")
        return

    # person who's followed
    account_info = cur.execute("SELECT * FROM accounts WHERE username = ?", (username,))
    account_info = account_info.fetchone()

    if account_info is None:
        print("The account is invalid.")
    else:
        #print(account_info)
        #print(username)
        #print(follower_username)
        already_followed = cur.execute("SELECT * FROM followers WHERE username = ? AND follower_username = ?", (username, follower_username,)).fetchone()
        if already_followed:
            print("-->", username,"already follows", follower_username)
        else:
            cur.execute("INSERT INTO followers (username, follower_username) VALUES (?, ?)", (username, follower_username,))
            print("-->",username,"has followed", follower_username)

    con.commit()
    con.close()

def remove_follower(username, follower_username):
    con = db.getDatabase()
    cur = con.cursor()

    # check if follower exists
    info = cur.execute("SELECT * FROM followers WHERE username = ? AND follower_username = ?", (username, follower_username,))
    info = info.fetchone()
    if info is None:
        print("-->","Follower does not exist")
    else:
        cur.execute("DELETE FROM followers WHERE username = ?", (username,))
        print("-->",username,"has unfollowed", follower_username)

    con.commit()
    con.close()


def show_mutual_followers():
    con = db.getDatabase()
    cur = con.cursor()

    # get the mutual_follows
    
    mutual_follows = cur.execute("SELECT f1.username, f1.follower_username FROM followers AS f1 INNER JOIN followers AS f2 ON f1.username = f2.follower_username AND f1.follower_username = f2.username WHERE f1.username < f1.follower_username")
    mutual_follows = mutual_follows.fetchall()
    #print(mutual_follows)
    if mutual_follows:
        print("\n-->", "MUTUAL FOLLOWS:\n")
        for pair in mutual_follows:
            print("\t|" ,pair[0], "and", pair[1] )
    else:
        print("-->","No mutual follows available.")

    con.commit()
    con.close()


def display_followers_leaderboard():
    con = db.getDatabase()
    cur = con.cursor()

    most_followers = cur.execute("SELECT follower_username, COUNT(*) AS follower_count FROM followers GROUP BY follower_username ORDER BY follower_count DESC LIMIT 10;")
    most_followers = most_followers.fetchall()
    if most_followers:
        print("\n-->", "FOLLOWERS LEADERBOARD:\n")
        for person in most_followers:
            print("\t|" ,person[0], "--> Follower Count:", person[1])
    else:
        print("-->","No follows available.")

    con.commit()
    con.close()
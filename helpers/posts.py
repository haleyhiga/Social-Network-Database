import db
import datetime

def send_post(username, message):
    con = db.getDatabase()
    cur = con.cursor()

    info = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    info = info.fetchone()
    #print(info)
    if info:
        cur.execute("INSERT INTO posts (username, post_message) VALUES(?,?)", (username, message,))
        #post_id = cur.execute("SELECT post_id FROM posts WHERE username = ? ORDER BY post_id DESC LIMIT 1", (username,)).fetchone()
        #cur.execute("INSERT INTO likes_dislikes (post_id, username, likes, dislikes) VALUES(?,?,?,?)", (post_id[0], username, 0, 0))
        print("-->",username,"has posted", message)
    else:
        print("-->","Given username does not exist.")

    con.commit()
    con.close()

def edit_post(username, post_id, message):
    con = db.getDatabase()
    cur = con.cursor()

    post = cur.execute("SELECT * FROM posts WHERE post_id = ? AND username = ?", (post_id, username,))
    post = post.fetchall()
    if post:
        old_message = post[0][2]
        if old_message == message:
            print("EDIT POST: id",post_id,"with user",username,"is the same.")
        else:
            cur.execute("UPDATE posts SET post_message = ?, time_editted = CURRENT_TIMESTAMP WHERE username = ? AND post_id = ?", (message, username, post_id,))
            print("EDIT POST: id",post_id,"with user",username,"has been updated from: '"+ old_message+"' to '"+message+"'")
    else:
        print("EDIT POST: id",post_id,"with user",username,"does not exist.")

    con.commit()
    con.close()

def list_posts(username):
    con = db.getDatabase()
    cur = con.cursor()

    posts = cur.execute("SELECT * FROM posts WHERE username = ?", (username,))
    posts = posts.fetchall()
    if posts:
        print("-->", username,"has made these posts:")
        see_feed(username, 0)
    else:
        print("-->", username,"has made no posts.")

    con.close()
    
def most_liked_posts():
    con = db.getDatabase()
    cur = con.cursor()

    posts = cur.execute('''
SELECT p.username, p.post_id
FROM posts AS p
JOIN likes_dislikes l ON l.post_id = p.post_id AND l.liked = 1
GROUP BY l.post_id
ORDER BY COUNT(l.liked) DESC LIMIT 10       
''')

    posts = posts.fetchall()
    if posts:
        print("\n-->", "TOP 10 LIKED POSTS:\n")
        for user in posts:
            see_feed(user[0], user[1])
    else:
        print("-->", "There are no posts.")

    con.close()

def most_disliked_posts():
    con = db.getDatabase()
    cur = con.cursor()

    posts = cur.execute('''
SELECT p.username, p.post_id
FROM posts AS p
JOIN likes_dislikes l ON l.post_id = p.post_id AND l.liked = 0
GROUP BY l.post_id
ORDER BY COUNT(l.liked) DESC
LIMIT 10            
''')
    
    posts = posts.fetchall()
    if posts:
        print("\n-->", "TOP 10 DISLIKED POSTS:\n")
        for user in posts:
            see_feed(user[0], user[1])
    else:
        print("-->", "There are no posts.")

    con.close()

def best_ten_posts_of_day():
    con = db.getDatabase()
    cur = con.cursor()

    posts = cur.execute('''
SELECT p.username, p.time_published, p.post_id
FROM posts AS p
JOIN likes_dislikes l ON l.post_id = p.post_id AND l.liked = 1
JOIN likes_dislikes d ON d.post_id = l.post_id AND d.liked = 0
GROUP BY l.post_id
ORDER BY COUNT(l.liked) DESC, COUNT(d.liked) DESC LIMIT 10
''')

    # CHANGE QUERY TO THE DAY
    posts = posts.fetchall()
    if posts:
        print("\n-->", "TOP 10 POSTS OF THE DAY:\n")
        for user in posts:
            time = user[1]
            year = int(time[:4])
            month = int(time[5:7])
            day = int(time[8:10])
            today = datetime.datetime.now()
            if today.year == year and today.month == month and today.day == day:
                see_feed(user[0], user[2])
    else:
        print("-->", "There are no posts of the day.")

    con.close()

def feed(username):
    con = db.getDatabase()
    cur = con.cursor()
    original_user = cur.execute("SELECT username FROM posts WHERE username = ?", (username,))
    original_user = original_user.fetchone()
    if original_user is None:
        print("-->",username,"does not exist.")
        return
    users = cur.execute("SELECT follower_username FROM followers WHERE username = ?", (username,))
    users = users.fetchall()
    if users == []:
        print(username, "does not follow anyone.")
        con.close()
        return
    for user in users[0]:
        see_feed(user, 0)
    
    con.commit()
    con.close()


def see_feed(username, post_id):
    con = db.getDatabase()
    cur = con.cursor()
    info = ""

    if post_id != 0:
        info = cur.execute('''
        WITH getPosts AS (
            SELECT p.*, COUNT(l.liked) AS liked
            FROM posts p
            LEFT OUTER JOIN likes_dislikes l ON l.post_id = p.post_id AND l.liked = 1
            WHERE p.username = ? AND p.post_id = ?
            GROUP BY l.liked
        )
        SELECT p.*, COUNT(d.liked) AS disliked
        FROM getPosts p
        LEFT OUTER JOIN likes_dislikes d ON d.post_id = p.post_id AND d.liked = 0
        WHERE p.username = ? AND p.post_id = ?
        GROUP BY d.liked
    ''', (username, post_id, username, post_id,))
        info = info.fetchall()
    else:
        info = cur.execute('''
    SELECT p.*, COUNT(likes.liked), COUNT(dislikes.liked)
    FROM likes_dislikes likes
    LEFT OUTER JOIN posts p ON p.post_id = likes.post_id
    LEFT OUTER JOIN likes_dislikes dislikes ON dislikes.post_id = likes.post_id AND dislikes.liked = 0
    WHERE likes.liked = 1 AND p.username = ?''', (username,))
        info = info.fetchall()
        if info[0][0] is None:
            info = cur.execute('''
    SELECT p.*, COUNT(likes.liked), COUNT(dislikes.liked)
    FROM likes_dislikes dislikes
    LEFT OUTER JOIN posts p ON p.post_id = dislikes.post_id
    LEFT OUTER JOIN likes_dislikes likes ON likes.post_id = dislikes.post_id AND likes.liked = 1
    WHERE dislikes.liked = 0 AND p.username = ?''', (username,))
            info = info.fetchall()
    #print(info)
    if len(info) == 0:
        con.close()
        return

    if info[0][0]:
        for post in info:
            post_id = str(post[1])
            message = post[2]
            published = post[3]
            time = datetime.datetime.strptime(published, '%Y-%m-%d %H:%M:%S')
            
            zero = ""
            if time.month < 10:
                zero = "0"
            zero1 = ""
            if time.day < 10:
                zero1 = "0"
            zero2 = ""
            if time.hour < 10:
                zero2 = "0"
            zero3 = ""
            if time.minute < 10:
                zero3 = "0"
            zero4 = ""
            if time.second < 10:
                zero4 = "0"
            published = zero + str(time.month) + "/" + zero1 + str(time.day) + "/" + str(time.year) + " " + zero2 + str(time.hour) + ":" + zero3 +  str(time.minute) + ":" + zero4 +  str(time.second) + " "
            editted = post[4]
            time2 = datetime.datetime.strptime(editted, '%Y-%m-%d %H:%M:%S')
            
            if time == time2:
                editted = ""
            else:
                zero = ""
                if time2.month < 10:
                    zero = "0"
                zero1 = ""
                if time2.day < 10:
                    zero1 = "0"
                zero2 = ""
                if time2.hour < 10:
                    zero2 = "0"
                zero3 = ""
                if time2.minute < 10:
                    zero3 = "0"
                zero4 = ""
                if time2.second < 10:
                    zero4 = "0"
                editted = "Editted at " + zero + str(time2.month) + "/" + zero1 + str(time2.day) + "/" + str(time2.year) + " " + zero2 + str(time2.hour) + ":" + zero3 +  str(time2.minute) + ":" + zero4 +  str(time2.second) + " "
            
            likes = post[5]
            likes = "👍: " + str(likes)
            dislikes = post[6]
            dislikes = "👎: " + str(dislikes)

            columns = 4
            spacing = columns*2
            spacing += columns+1

            column1 = len(post_id)+4
            column2 = len(username)+4
            if len(likes) > column2:
                column2 = len(likes)+4
            column3 = len(published)+4
            column4 = len(editted)+4

            if time == time2:
                line = "+"+column1*"-"+"+"+column2*"-"+"+"+column3*"-"+column4*"-"+"+"
                print(line)
                print("|  "+post_id+"  |"+"  "+username+"  "+"|  "+published+"  "+"  "+"  |")
                print(line)
                msg_line = "|"+column1*" "+"|  "+message
                print(msg_line+((len(line)-len(msg_line)-1)*" ")+"|")
                print("+"+column1*"-"+"+"+column2*"-"+"-"+column3*"-"+column4*"-"+"+")
                row3 = "|"+column1*" "+"|  "+likes+"  "+dislikes
                print(row3 + (len(line) - len(row3)-3)*" " + "|")
                print("+"+column1*"-"+"+"+column2*"-"+"-"+column3*"-"+column4*"-"+"+")
            else:
                line = "+"+column1*"-"+"+"+column2*"-"+"+"+column3*"-"+"+"+column4*"-"+"+"
                print(line)
                print("|  "+post_id+"  |"+"  "+username+"  "+"|  "+published+"  "+"|  "+editted+"  |")
                print(line)
                msg_line = "|"+column1*" "+"|  "+message
                print(msg_line+(len(line)-len(msg_line)-1)*" " +"|")
                print("+"+column1*"-"+"+"+column2*"-"+"-"+column3*"-"+column4*"-"+"-"+"+")
                row3 = "|"+column1*" "+"|  "+likes+"  "+dislikes
                print(row3 + (len(line) - len(row3)-3)*" " + "|")
                print("+"+column1*"-"+"+"+column2*"-"+"-"+column3*"-"+column4*"-"+"-"+"+")
    else:
        print("\t"+username,"has no posts.")
        '''
            +------+------------+---------------+----------------+
            |  ID  |  Username  |  Date Posted  |  Date Editted  |
            +------+---------------------------------------------+
            |      |  Message                                    |
            +------+---------------------------------------------+
            |      |  Likes     |  Dislikes     |                |
            +------+---------------------------------------------+
        '''

    con.commit()
    con.close()





def add_like(username, post_id):
    post_id = int(post_id)
    con = db.getDatabase()
    cur = con.cursor()

    # check if user exists
    user = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    user = user.fetchone()
    #print("\nUSER:",user,"\n")
    if user is None:
        print("-->", username, "does not exist.")
        con.close()
        return

    get_post_likes = cur.execute("SELECT liked FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
    get_post_likes = get_post_likes.fetchone()

    get_post = cur.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
    get_post = get_post.fetchone()

    # check if none
    if get_post is None:
        print("-->", username, "post id", post_id,"does not exist.")
        con.close()
        return

    # check if already liked
    if get_post_likes is not None:
        if get_post_likes[0] == 1:
            print("-->", username, "has already liked post id", post_id)
            con.close()
            return
        elif get_post_likes[0] == 0:
            # change liked to true
            cur.execute("UPDATE likes_dislikes SET liked = 1 WHERE post_id = ? AND username = ?", (post_id,username,))
            print("-->", username, "has liked post id", post_id)
            con.commit()
            con.close()
            return
    else: # if it is none
        cur.execute("INSERT INTO likes_dislikes (post_id, username, liked) VALUES(?, ?, ?)", (post_id, username, 1,))
        print("-->", username, "liked post id", post_id)

    con.commit()
    con.close()

def remove_like(username, post_id):

    con = db.getDatabase()
    cur = con.cursor()
    post_id = int(post_id)

    # check if user exists
    user = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    user = user.fetchone()
    #print("\nUSER:",user,"\n")
    if user is None:
        print("-->", username, "does not exist.")
        con.close()
        return

    get_post_likes = cur.execute("SELECT liked FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
    get_post_likes = get_post_likes.fetchone()

    get_post = cur.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
    get_post = get_post.fetchone()

    # check if none
    if get_post is None:
        print("-->", username, "post id", post_id,"does not exist.")
        con.close()
        return
    # check if already liked
    if get_post_likes is not None:
        if get_post_likes[0] == 1: # if it is liked
            cur.execute("DELETE FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
            print("-->", username + ", your like has been removed from post id", post_id)
        elif get_post_likes[0] == 0: # if it is disliked
            print("-->", username + ", you have already disliked post id", post_id)
    else: # if it is none
        print("-->", username + ", you have not liked post id", post_id)

    con.commit()
    con.close()

def add_dislike(username, post_id):
    #print("\n", "ADD DISLIKE SEEN:", username, post_id,"\n")
    post_id = int(post_id)
    con = db.getDatabase()
    cur = con.cursor()

    # check if user exists
    user = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    user = user.fetchone()
    #print("\nUSER:",user,"\n")
    if user is None:
        print("-->", username, "does not exist.")
        con.close()
        return
    
    get_post_likes = cur.execute("SELECT liked FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
    get_post_likes = get_post_likes.fetchone()

    get_post = cur.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
    get_post = get_post.fetchone()

    # check if none
    if get_post is None:
        print("-->", username, "post id", post_id,"does not exist.")
        con.close()
        return
    # check if already liked
    if get_post_likes is not None:
        if get_post_likes[0] == 1:
            cur.execute("UPDATE likes_dislikes SET liked = 0 WHERE post_id = ? AND username = ?", (post_id,username,))
            print("-->", username, "has disliked post id", post_id)
            con.commit()
            con.close()
            return
        elif get_post_likes[0] == 0: # if it is disliked
            # print that it has already been disliked
            print("-->", username, "has already disliked post id", post_id)
            con.close()
            return
    else: # if it is none
        cur.execute("INSERT INTO likes_dislikes (post_id, username, liked) VALUES(?, ?, ?)", (post_id, username, 0,))
        print("-->", username, "disliked post id", post_id)

    con.commit()
    con.close()

def remove_dislike(username, post_id):
 
    con = db.getDatabase()
    cur = con.cursor()

    post_id = int(post_id)

    # check if user exists
    user = cur.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    user = user.fetchone()
    #print("\nUSER:",user,"\n")
    if user is None:
        print("-->", username, "does not exist.")
        con.close()
        return

    get_post_likes = cur.execute("SELECT liked FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
    get_post_likes = get_post_likes.fetchone()

    get_post = cur.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
    get_post = get_post.fetchone()

    # check if none
    if get_post is None:
        print("-->", username, "post id", post_id,"does not exist.")
        con.close()
        return
    # check if already liked
    if get_post_likes is not None:
        if get_post_likes[0] == 0: # if it is disliked
            cur.execute("DELETE FROM likes_dislikes WHERE post_id = ? AND username = ?", (post_id, username,))
            print("-->", username + ", your dislike has been removed from post id", post_id)
        elif get_post_likes[0] == 1: # if it is liked
            print("-->", username + ", you have already liked post id", post_id)
    else: # if it is none
        print("-->", username + ", you have not disliked post id", post_id)

    con.commit()
    con.close()
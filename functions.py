from helpers import accounts, blockaccounts, followers, posts, users

def Users(email, type):

    if type == "add":
        users.add_user(email)
    elif type == "delete":
        users.delete_user(email)
    elif type == "list":
        users.list_users()

def Accounts(email, username, type):

    if type == "add":
        accounts.add_account(email, username)
    elif type == "delete":
        accounts.delete_account(username)
    elif type == "list":
        accounts.list_accounts()

def Followers(username, follower_username, type):

    if type == "add":
        followers.add_follower(username, follower_username)
    elif type == "remove":
        followers.remove_follower(username, follower_username)
    elif type == "list":
        followers.list_followers(username)
    elif type == "show":
        followers.show_mutual_followers()
    elif type == "display":
        followers.display_followers_leaderboard()

def Posts(username, post_id, message, type):

    if type == "send":
        posts.send_post(username, message)
    elif type == "edit":
        posts.edit_post(username, post_id, message)
    elif type == "feed":
        posts.feed(username)
    elif type == "list":
        posts.list_posts(username)
    elif type == "liked":
        posts.most_liked_posts()
    elif type == "disliked":
        posts.most_disliked_posts()
    elif type == "best_ten":
        posts.best_ten_posts_of_day()


# ADDITIONAL FEATURES

def Mentions():
    pass

def Likes(username, post_id, type):

    if type == "add_like":
        posts.add_like(username, post_id)
    elif type == "remove_like":
        posts.remove_like(username, post_id)

def Dislikes(username, post_id, type):

    if type == "add_dislike":
        posts.add_dislike(username, post_id)
    elif type == "remove_dislike":
        posts.remove_dislike(username, post_id)


def BlockAccounts(username, blocked_username, type):

    if type == "add":
        blockaccounts.block_account(username, blocked_username)
    elif type == "remove":
        blockaccounts.remove_blocked_account(username, blocked_username)
    elif type == "list":
        blockaccounts.list_blocked_accounts(username)
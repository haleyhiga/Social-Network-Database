
import click
import db
import functions
import os

SOCIAL_NETWORK_NAME = "Turtle"
DB_FILE = SOCIAL_NETWORK_NAME + ".db"

@click.group()
def users():
    pass

@click.group()
def accounts():
    pass

@click.group()
def followers():
    pass

@click.group()
def posts():
    pass

@click.group()
def block_accounts():
    pass

@click.command()
def list_users():
    functions.Users("", "list")

@click.command()
@click.argument('email')
def add_user(email):
    functions.Users(email, "add")

@click.command()
@click.argument('email')
def delete_user(email):
    functions.Users(email, "delete")

@click.command()
@click.argument('email')
@click.argument('username')
def add_account(email, username):
    functions.Accounts(email, username, "add")

@click.command()
@click.argument('username')
def delete_account(username):
    functions.Accounts('', username, "delete")

@click.command()
def list_accounts():
    functions.Accounts("", "", "list")

@click.command()
@click.argument('username')
@click.argument('follower_username')
def add_follower(username, follower_username):
    functions.Followers(username, follower_username, "add")

@click.command()
@click.argument('username')
@click.argument('follower_username')
def remove_follower(username, follower_username):
    functions.Followers(username, follower_username, "remove")

@click.command()
@click.argument('username')
def list_followers(username):
    functions.Followers(username, "", "list")

@click.command()
def show_mutual_followers():
    functions.Followers("", "", "show")

@click.command()
def display_followers_leaderboard():
    functions.Followers("", "", "display")

@click.command()
@click.argument('username')
@click.argument('message')
def send_post(username, message):
    functions.Posts(username, 0, message, "send")

@click.command()
@click.argument('username')
@click.argument('post_id')
@click.argument('message')
def edit_post(username, post_id, message):
    functions.Posts(username, post_id, message, "edit")

@click.command()
@click.argument('username')
@click.argument('post_id')
def add_like(username, post_id):
    functions.Likes(username, post_id, "add_like")

@click.command()
@click.argument('username')
@click.argument('post_id')
def add_dislike(username, post_id):
    functions.Dislikes(username, post_id, "add_dislike")

@click.command()
@click.argument('username')
@click.argument('post_id')
def remove_like(username, post_id):
    functions.Likes(username, post_id, "remove_like")

@click.command()
@click.argument('username')
@click.argument('post_id')
def remove_dislike(username, post_id):
    functions.Dislikes(username, post_id, "remove_dislike")

@click.command()
@click.argument('username')
@click.argument('blocked_username')
def add_block_account(username, blocked_username):
    functions.BlockAccounts(username, blocked_username, "add")

@click.command()
@click.argument('username')
@click.argument('blocked_username')
def remove_block_account(username, blocked_username):
    functions.BlockAccounts(username, blocked_username, "remove")

@click.command()
@click.argument('username')
def list_blocked_accounts(username):
    functions.BlockAccounts(username, "", "list")

# NEEDED COMMANDS BELOW
@click.command()
@click.argument('username')
def feed(username):
    functions.Posts(username, 0, "", "feed")

@click.command()
@click.argument('username')
def list_my_posts(username):
    functions.Posts(username, 0, "", "list")

@click.command()
def top_liked_posts():
    functions.Posts("", 0, "", "liked")

@click.command()
def top_disliked_posts():
    functions.Posts("", 0, "", "disliked")

@click.command()
def top_ten_posts():
    functions.Posts("", 0, "", "best_ten")

#python3 ./main.py
if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        db.createDatabase()

    # users
    users.add_command(add_user)
    users.add_command(delete_user)
    users.add_command(list_users)

    # accounts
    accounts.add_command(add_account)
    accounts.add_command(delete_account)
    accounts.add_command(list_accounts)

    # followers
    followers.add_command(add_follower)
    followers.add_command(remove_follower)
    followers.add_command(list_followers)
    followers.add_command(show_mutual_followers)
    followers.add_command(display_followers_leaderboard)

    # posts
    posts.add_command(feed)
    posts.add_command(send_post)
    posts.add_command(edit_post)
    posts.add_command(list_my_posts)
    posts.add_command(top_liked_posts)
    posts.add_command(top_disliked_posts)
    posts.add_command(top_ten_posts)
    posts.add_command(add_like)
    posts.add_command(remove_like)
    posts.add_command(add_dislike)
    posts.add_command(remove_dislike)

    # block accounts
    block_accounts.add_command(add_block_account)
    block_accounts.add_command(remove_block_account)
    block_accounts.add_command(list_blocked_accounts)

    cli = click.CommandCollection(sources=[users, accounts, followers, posts, block_accounts])
    cli()
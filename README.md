# To Create The Database

> chmod u+x run.sh

> bash run.sh

# How It Works
> Once running run.sh in the bash, 
it creates the file information for:
add-users, add-accounts, add-posts and input (basic and interesting queries) from './format_bash.py'.
From here, it autogenerates random names and posts for the database to have. After this, it runs the add-users, add-accounts, add-posts and input files. These are the files where the unique commands are being called.

> Some of the interesting queries that we have introduced are:
- For the commands: top-disliked-posts, top-liked-posts and top-ten-posts, we have used a Common Table Expression for getting the correct count of likes and dislikes to display each post.

> Additional queries that we have included:
- Displaying followers leaderboard
- Displaying all mutual followers
- Displaying all accounts
- Displaying all users
- Displaying all followers
- Displaying all blocked accounts
- Displaying the posts made by user

> Additional features:
- Ability to like posts
- Ability to dislike posts
- Ability to block accounts

> Basic queries:
- Add-user
- Add-account
- Add-follower
- Delete-user
- Delete-account
- Remove-follower
- Send-post
- Edit-post

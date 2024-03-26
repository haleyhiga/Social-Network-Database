emails = ["russross@vim.com","curtislarsen@emacs.com","bartstander@thonny.com","loraklein@vscode.com", "mattkearl@vscode.com", "carolstander@thonny.com", "rennquinn@vim.com", "john.doe@example.com", "jane.smith@example.com", "bob.jones@example.com", "emily.wilson@example.com", "michael.brown@example.com", "sarah.williams@example.com", "david.taylor@example.com", "lisa.martin@example.com", "kevin.anderson@example.com", "amanda.thomas@example.com", "steve.jackson@example.com", "karen.white@example.com", "ryan.moore@example.com", "jessica.hall@example.com", "matthew.young@example.com", "ashley.lee@example.com", "daniel.clark@example.com", "melissa.roberts@example.com", "brian.harris@example.com", "laura.lewis@example.com", "chris.walker@example.com", "kimberly.hill@example.com", "james.allen@example.com", "tiffany.green@example.com", "adam.carter@example.com", "natalie.edwards@example.com", "robert.phillips@example.com", "stephanie.cook@example.com", "peter.rogers@example.com", "angela.bell@example.com", "mark.ward@example.com", "christina.wood@example.com", "patrick.collins@example.com", "heather.stewart@example.com", "justin.murphy@example.com", "katie.ross@example.com", "jonathan.howard@example.com", "jennifer.alexander@example.com", "nathan.nelson@example.com", "samantha.campbell@example.com", "dennis.richards@example.com", "brittany.ross@example.com", "gregory.harrison@example.com", "stephanie.brooks@example.com", "jeremy.bennett@example.com", "rebecca.wood@example.com", "scott.peterson@example.com", "erica.ramirez@example.com", "joshua.lee@example.com", "courtney.morgan@example.com", "olivia.garcia@example.com", "dylan.flores@example.com", "madison.young@example.com", "ethan.wilson@example.com", "hannah.gonzalez@example.com", "andrew.hall@example.com", "isabella.nelson@example.com", "jacob.richardson@example.com", "ava.carter@example.com", "william.mitchell@example.com", "sophia.perez@example.com", "noah.roberts@example.com", "mia.ramirez@example.com", "logan.cooper@example.com", "amelia.howard@example.com", "james.collins@example.com", "emma.kelly@example.com", "benjamin.bailey@example.com"]

# MAKE USERNAMES SMALLER
# "RizzRoss", "eMacsLover", "BigOLover", "HouseBuilder", "AppleVisionUser", "Sweetheart", "ACMLover"

usernames = ["RizzRoss", "eMacsLover", "BigOLover", "HouseBuilder", "AppleVisionUser", "Sweetheart", "ACMLover", 'AngelWarlock', 'AssassinTitan', 'BeastConqueror', 'BigOLover', 'BlazingAssassin', 'CelestialDestroyer', 'ChampionSamurai', 'ChaosGuardian', 'ConquerorDragon', 'CosmicHunter', 'CyborgAssassin', 'DemonWarrior', 'DestroyerSorcerer', 'DivinePirate', 'DragonSorcerer', 'EnigmaTitan', 'EternalChampion', 'FierceWarrior', 'FierySamurai', 'FrozenViking', 'GhostNinja', 'GladiatorGhost', 'GoldenLegend', 'BeastConqueror', 'BlazingAssassin', 'CelestialDestroyer', 'ChaosGuardian', 'CosmicHunter', 'CyborgAssassin', 'DemonWarrior', 'EnigmaTitan0', 'EternalChampion2','FierceWarrior4', 'FierySamurai','FrozenViking0', 'GhostNinja', 'GuardianPhoenix', 'HeroBeast', 'HunterGladiator', 'InfernoRogue432', 'InfernoRogue','InfinitePhantom', 'KnightRogue', 'LegendMage', 'LegendMage634', 'LunarAngel', 'MageWizard', 'MagicalConqueror', 'MasterAssassin', 'MightyCyborg', 'MysticWizard', 'NeonBeast','NinjaShogun5', 'NinjaShogun', 'PhantomGladiator', 'PhoenixMage34', 'PirateRogue', 'RadiantGhost123', 'RogueHunter421', 'SavageHero', 'SavageHero', 'TitanWizards', 'TitanWizard','Vpirate', 'PirateViking', 'Warunter', 'WarlockHunter', 'WarriorKnight']

for a in range(len(usernames)):
    for b in range(len(usernames)):
        if a > len(usernames)-1 or b > len(usernames)-1:
            break
        if usernames[a] == usernames[b]:
            usernames.pop(a)
    if a > len(usernames)-1 or b > len(usernames)-1:
        break

posts = [
    "Shine bright like a diamond",
    "Just finished an amazing book!",
    "Announced an upcoming project!",
    "Catching up with friends.",
    "#Coffee",
    "Thank you for all the support!",
    "New blog post is up! #LookNow",
    "Enjoying a beautiful sunset.",
    "Trying out a new recipe tonight.",
    "Just hit the gym. #fitnessgoals",
    "Looking forward to the weekend.",
    "Learning so much!",
    "Attended motivational seminar.",
    "#inspired",
    "Celebrating a milestone.",
    "Spent the day exploring a city.",
    "#travel",
    "#metime",
    "Setting goals for the future.",
    "Hitting the slopes for skiing.",
    "#winterfun",
    "Enjoying a lazy Sunday morning.",
    "Just adopted a new pet.",
    "Attended a lecture.",
    "#weekendvibes",
    "Taking a break from Turtle.",
    "Had a blast at the concert.",
    "Feeling inspired.",
    "Cooking up in the kitchen.",
    "Heading out for a hike.",
    "#volunteering #givingback",
    "#quiettime",
    "Adventure awaits!",
    "Feeling accomplished!",
    "Savoring the little moments.",
    "Grateful for all the followers.",
    "#lifelonglearner",
    "Trying out a new restaurant.",
    "#birthday",
    "Getting lost in a novel.",
    "#bookworm",
    "#WorkingOnSocialNetworksProject",
    "Feeling motivated.",
    "#culture",
    "Went to the art museum.",
    "#familytime",
    "#movienight",
    "#boardgames",
    "#party",
    "#CS4307",
    "Excited to meet new people!",
    "relaxing spa day!",
    "#selfcare",
    "#proud",
    "Exciting news.",
    "Heading to the beach.",
    "positive mindset",
    "beauty of nature.",
    "#blessed",
    "#entertainment",
    "#shopping",
    "#fitness",
    "weekend getaway.",
    "productive work session.",
    "cup of coffee.",
    "Feeling grateful.",
    "Starting a new chapter.",
    "#newbeginnings",
    "scenic hike in the mountains.",
    "#concert.",
    "passions for life!",
    "Spent the evening stargazing.",
    "#starrynight",
    "Power of kindness.",
    "night in the town.",
    "Feeling energized.",
    "Enjoying some quiet time.",
    "Year of growth.",
    "Computer science!",
    "Russ is amazing!",
    "#AtTheSmith",
    "#Zonos",
    "#UtahTech",
    "#TechRidge",
    "Invision!",
    "#Programming",
    "#ProgrammingCompetition",
    "#DistributedSystemsBestClass",
    "#Paxos",
    "#RPCChat",
    "#B-Tree",
    "#BaconNumber",
    "#Golden",
    "#ILoveSudoku",
    "#WordleIsAmazing",
    "#UndergraduateResearch"
    "#HaileyAndHaleyIsTheBest"
]

import random

def add_users():
    file = open('add-users.sh', 'w')

    command = "python3 ./main.py add-user"
    for user in emails:
        s = command + " " + user + "\n"
        file.write(s)

    file.close()

def add_accounts():
    file = open('add-accounts.sh', 'w')

    command = "python3 ./main.py add-account"
    for (email, user) in zip(emails, usernames):
        s = command + " " + email + " " + user + "\n"
        file.write(s)
    file.close()

def add_posts(posts_amount):
    file = open('add-posts.sh', 'w')

    command = "python3 ./main.py send-post"
    for user in usernames:
        rand = random.randint(0, len(posts)-1)
        s = command + " " + user + " " + "'" + posts[rand] + "'\n"
        posts_amount += 1
        file.write(s)
        rand = random.randint(0, len(posts)-1)
        s = command + " " + user + " " + "'" + posts[rand] + "'\n"
        posts_amount += 1
        file.write(s)

    file.close()
    return posts_amount

# OTHER COMMANDS
    
def other_commands(AMOUNT_OF_POSTS):
    file = open('input.sh', 'w')

    # Adding to the database
    add_block_account = "python3 ./main.py add-block-account"
    add_dislike = "python3 ./main.py add-dislike"
    add_follower = "python3 ./main.py add-follower"
    add_like = "python3 ./main.py add-like"

    # Posts
    edit_post = "python3 ./main.py edit-post"
    feed = "python3 ./main.py feed"

    # Listing
    followers_leaderboard = "python3 ./main.py display-followers-leaderboard"
    list_accounts = "python3 ./main.py list-accounts"
    list_blocked_accounts = "python3 ./main.py list-blocked-accounts"
    list_followers = "python3 ./main.py list-followers"
    list_my_posts = "python3 ./main.py list-my-posts"
    list_users = "python3 ./main.py list-users"
    show_mutual_followers = "python3 ./main.py show-mutual-followers"
    top_disliked_posts = "python3 ./main.py top-disliked-posts"
    top_liked_posts = "python3 ./main.py top-liked-posts"
    top_ten_posts = "python3 ./main.py top-ten-posts"

    # Deleting/Removing
    delete_account = "python3 ./main.py delete-account"
    delete_user = "python3 ./main.py delete-user"
    remove_block_account = "python3 ./main.py remove-block-account"
    remove_dislike = "python3 ./main.py remove-dislike"
    remove_follower = "python3 ./main.py remove-follower"
    remove_like = "python3 ./main.py remove-like"

    #
    # INITIALIZED COMMANDS ABOVE
    #

    #list_users
    s = list_users + "\n"
    file.write(s)

    #list_accounts
    s = list_accounts + "\n"
    file.write(s)
    
    #followers_leaderboard
    s = followers_leaderboard + "\n"
    file.write(s)
    
    #show_mutual_followers
    s = show_mutual_followers + "\n"
    file.write(s)
    
    #top_disliked_posts
    s = top_disliked_posts + "\n"
    file.write(s)
    
    #top_liked_posts
    s = top_liked_posts + "\n"
    file.write(s)

    #top_ten_posts
    s = top_ten_posts + "\n"
    file.write(s)

    #
    # COMMANDS THAT CHANGE DATABASE
    #
    
    MAX_COMMANDS = 10
    i = 0
    while i < MAX_COMMANDS:
        #random_user = random.randint(0, len(usernames)-1)
        #random_user2 = random.randint(0, len(usernames)-1)
        #random_email = random.randint(0, len(emails)-1)
        #random_post_id = random.randint(0, AMOUNT_OF_POSTS)
        #random_message = random.randint(0, len(posts)-1)
        
        random_user = random.randint(0, len(usernames)-1)
        random_user2 = random.randint(0, len(usernames)-1)
        #add_block_account (username, blocked_username)
        s = add_block_account + " " + usernames[random_user] + " " + usernames[random_user2] + "\n"
        file.write(s)
        
        j = 0
        while j < 5:
            random_user = random.randint(0, len(usernames)-1)
            random_post_id = random.randint(0, AMOUNT_OF_POSTS-1)
            #add_dislike (username, post_id)
            s = add_dislike + " " + usernames[random_user] + " " + str(random_post_id) + "\n"
            file.write(s)
            j += 1


        z = 0
        while z < 4:
            random_user = random.randint(0, len(usernames)-1)
            random_user2 = random.randint(0, len(usernames)-1)
            #add_follower (username, follower_username)s
            s = add_follower + " " + usernames[random_user] + " " + usernames[random_user2] + "\n"
            file.write(s)
            z += 1

        z = 0
        while z < 7:
            random_user = random.randint(0, len(usernames)-1)
            random_post_id = random.randint(0, AMOUNT_OF_POSTS-1)
            #add_like (username, post_id)
            s = add_like + " " + usernames[random_user] + " " + str(random_post_id) + "\n"
            file.write(s)
            z += 1
        
        random_user = random.randint(0, len(usernames)-1)
        random_post_id = random.randint(0, AMOUNT_OF_POSTS-1)
        random_message = random.randint(0, len(posts)-1)
        #edit_post (username, post_id, message)
        s = edit_post + " " + usernames[random_user] + " " + str(random_post_id) + " '" + posts[random_message] + "'\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        #feed (username)
        s = feed + " " + usernames[random_user] + "\n"
        file.write(s)

        random_user = random.randint(0, len(usernames)-1)
        #list_blocked_accounts (username)
        s = list_blocked_accounts + " " + usernames[random_user] + "\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        #list_followers (username)
        s = list_followers + " " + usernames[random_user] + "\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        #list_my_posts (username)
        s = list_my_posts + " " + usernames[random_user] + "\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        #delete_account (username)
        s = delete_account + " " + usernames[random_user] + "\n"
        file.write(s)
        
        random_email = random.randint(0, len(emails)-1)
        #delete_user (email)
        s = delete_user + " " + emails[random_email] + "\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        random_user2 = random.randint(0, len(usernames)-1)
        #remove_block_account (username, blocked_username)
        s = remove_block_account + " " + usernames[random_user] + " " + usernames[random_user2] + "\n"
        file.write(s)

        random_user = random.randint(0, len(usernames)-1)
        random_post_id = random.randint(0, AMOUNT_OF_POSTS-1)
        #remove_dislike (username, post_id)
        s = remove_dislike + " " + usernames[random_user] + " " + str(random_post_id) + "\n"
        file.write(s)

        random_user = random.randint(0, len(usernames)-1)
        random_user2 = random.randint(0, len(usernames)-1)
        #remove_follower (username, follower_username)
        s = remove_follower + " " + usernames[random_user] + " " + usernames[random_user2] + "\n"
        file.write(s)
        
        random_user = random.randint(0, len(usernames)-1)
        random_post_id = random.randint(0, AMOUNT_OF_POSTS-1)
        #remove_like (username, post_id)
        s = remove_like + " " + usernames[random_user] + " " + str(random_post_id) + "\n"
        file.write(s)

        i += 1
    
    #list_users
    s = list_users + "\n"
    file.write(s)

    #list_accounts
    s = list_accounts + "\n"
    file.write(s)
    
    #followers_leaderboard
    s = followers_leaderboard + "\n"
    file.write(s)
    
    #show_mutual_followers
    s = show_mutual_followers + "\n"
    file.write(s)
    
    #top_disliked_posts
    s = top_disliked_posts + "\n"
    file.write(s)
    
    #top_liked_posts
    s = top_liked_posts + "\n"
    file.write(s)

    #top_ten_posts
    s = top_ten_posts + "\n"
    file.write(s)

    #file.write("rm -f Turtle.db")
    file.close()

# chmod u+x add-users.sh
# bash add-users.sh

# chmod u+x add-accounts.sh
# bash add-accounts.sh
    
# chmod u+x add-posts.sh
# bash add-posts.sh
    
# chmod u+x input.sh
# bash input.sh

# python3 ./main.py

def main():
    add_users()
    add_accounts()
    amount = add_posts(0)
    other_commands(amount)

main()
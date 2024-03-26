rm -f Turtle.db

python3 ./format_bash.py
chmod u+x add-users.sh
chmod u+x add-accounts.sh
chmod u+x add-posts.sh
chmod u+x input.sh

bash add-users.sh
bash add-accounts.sh
bash add-posts.sh
bash input.sh

# chmod u+x run.sh
# bash run.sh
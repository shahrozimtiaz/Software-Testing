#make sure you run this from the same directory as manage.py

#update local database schema
rm -rf blog/migrations
rm db.sqlite3
echo "Deleting migrations and database"

#apply migrations
python3 manage.py makemigrations blog
python3 manage.py migrate

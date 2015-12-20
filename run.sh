#sudo pip install requirements.txt
echo "Updating software..."
git fetch origin
git merge origin/master

echo "Setting up database..."
python manage.py migrate

echo "Enjoy!"
python manage.py runserver 0.0.0.0:8000
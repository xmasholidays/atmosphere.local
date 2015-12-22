#!/bin/bash

echo -e "\x1B[1;97;44mSetting up the environment...\x1B[0m"
. env.sh
pip install -r requirements.txt --upgrade

echo -e "\x1B[1;97;44mUpdating software...\x1B[0m"
git fetch origin
git merge origin/master

echo -e "\x1B[1;97;44mSetting up database...\x1B[0m"
python manage.py migrate
python create_initial_data.py

echo -e "\x1B[1;97;44mEnjoy!\x1B[0m"
python worker.py &
sudo python manage.py runserver 0.0.0.0:$ATMLOCAL_PORT

killall python
killall mpg321
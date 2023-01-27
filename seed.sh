#!/bin/bash
rm -rf aethernetapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations aethernetapi
python manage.py migrate aethernetapi
python manage.py loaddata users
python manage.py loaddata sleep_cards
python manage.py loaddata dream_journals
python manage.py loaddata tags
python manage.py loaddata sc_tags

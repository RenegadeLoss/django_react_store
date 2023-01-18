set -o errexit

sudo apt-get install python3-setuptools

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
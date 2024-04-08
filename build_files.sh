ECHO "BUILD START"
python 3.9 -m pip install -r requirements.txt
python 3.9 manage.py collectstatic --noinput --clear
ECHO "BUILD END"
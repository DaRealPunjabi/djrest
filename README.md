# Installation & Setup

mkdir djrest<br>
cd djrest<br>
code .<br>

## Open terminal in vscode

python3 -m venv .venv<br>
. .venv/bin/activate<br>

pip freeze<br>
pip install --upgrade pip<br>
pip install django<br>
pip install djangorestframework<br>
pip install pyyaml<br>
pip install requests<br>
pip install django-cors-headers<br>

mkdir backend<br>
mkdir pyclient<br>

cd backend<br>
django-admin startproject esghome .<br>


cd /Users/shivjalli/projects/djrest<br>
python pyclient/basic001.py<br>
python pyclient/basic002.py<br>

cd /Users/shivjalli/projects/djrest/backend<br>
python manage.py runserver 8000<br>

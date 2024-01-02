Installation & Setup

mkdir djrest
cd djrest
code .

Open terminal in vscode

python3 -m venv .venv
. .venv/bin/activate

pip freeze
pip install --upgrade pip
pip install django
pip install djangorestframework
pip install pyyaml
pip install requests
pip install django-cors-headers

mkdir backend
mkdir pyclient

cd backend
django-admin startproject esghome .


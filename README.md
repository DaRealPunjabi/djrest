# Installation & Setup

mkdir djrest\s
cd djrest\s
code .\s

## Open terminal in vscode

python3 -m venv .venv\s
. .venv/bin/activate\s

pip freeze\s
pip install --upgrade pip\s
pip install django\s
pip install djangorestframework\s
pip install pyyaml\s
pip install requests\s
pip install django-cors-headers\s

mkdir backend\s
mkdir pyclient\s

cd backend\s
django-admin startproject esghome .\s


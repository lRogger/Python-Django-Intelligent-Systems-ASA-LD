# Instalation Dependences
pip install -r requirements.txt

# Configurate .env file
.env.example

# Install Tailwind
python manage.py tailwind install

# Deploy Project
py .\manage.py tailwind start
py .\manage.py runserver

# Databases
mysql
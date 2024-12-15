

	Zhanel Zhanibekova.

	This is a simple Django app used for connection to PostgreSQL 15

	1. You should have "myapp_person" table in a "newdb" database

	2. Write your own DB password and username (default one is "postgres") in a /postgresdb/postgresdb/settings.py -> DATABASES
	   Also you may change other values where inappropriate with your database.

	3. Make sure that you have installed PostgreSQL 15/16, Pgadmin 4, Python, Django, venv

	then you can run these commands to install dependencies:

	- python -m venv venv

	- venv\Scripts\activate

	- pip install django

	- pip install psycopg2


	to connect with db on windows, use with these commands:

	- python manage.py makemigrations
	
	- python manage.py migrate
	

	after migrating tables to database, you can run this project:
	
	- python manage.py runserver












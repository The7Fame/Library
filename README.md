# Simple Library on Django

U can: 
 
* Create Author
* Delete Author
* Create Book
* Delete Book
* Upload photo of Book or Author
* Change language (English or Russian)

## First off all

U should make:
1. Create a virtual environment:
   ```
   python -m venv venv
   ```
2. Write next commands:
   ```
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
3. Click on `http://127.0.0.1:8000` and write near this `/admin/`. Now u can create Book, Genge, Author
5. Open again `http://127.0.0.1:8000` to see your creation.

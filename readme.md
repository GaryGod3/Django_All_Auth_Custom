# A Basic Working AllAuth Site
This is a working Django project with a fully working set of AllAuth pages.

It features single homepage with a menu bar with the links that show on the index.html.

## Next Steps
Once you've cloned the repo into your own project folder
1. create a virtual env as .venv
2. activate it
3. install the required packages
4. make and migrate the database
5. create a superuser
6. rename ".env update and rename to .env" to .env
7. generate a secret key
8. edit the .env file and put the secret key in and the email server details if required
9. start the site.  Unless you want to modify manage.py to use load_dotenv() then just run in vscode rather than from the shell with _python manage.py runserver 0.0.0.0:8000_.  It works because of this, https://code.visualstudio.com/docs/python/environments, "The extension also loads an environment variable definitions file identified by the python.envFile setting. The default value of this setting is ${workspaceFolder}/.env."
10. test the site
11. make it yours

## Commands
My preferred Powershell commands for the above, run from the base project folder.

        python -m venv .venv
        .venv\Scripts\activate
        python.exe -m pip install --upgrade pip
        pip install -r requirements.txt
        cp '.env update and rename to .env' .env
        python -c "import secrets; print(secrets.token_urlsafe())"

Then edit the .env file and add the secret key output above, then run from vsCode.

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser

Then over to you.
# Learning GraphQL using Python SQL Alchemy
This repo mainly using [this guide](https://www.apollographql.com/blog/graphql/python/complete-api-guide/) as baseline

## Requirements
- flask 
- ariadne==0.17 *`*for graphql playground`*
- flask-sqlalchemy
- flask-cors
- psycopg2 `or another database driver`

## Step
1. Create new python virtual environment
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```
1. Installing dependancies
    ```bash
    pip install -r requirements.txt
    ```
1. Rename example.local.yml to .local.yml and change the `dsn` variable
2. Create database for this service
3. Generate the table using Python terminal

    ```python 
    #Generate table
    >>> from app import db, app
    >>> db.create_all()

    #Create object row
    >>> from datetime import datetime
    >>> from api.models import Post
    >>> current_date = datetime.today().date()
    >>> new_post = Post(title="A new morning", description="A description", created_at=current_date)
    >>> db.session.add(new_post)
    >>> db.session.commit()
    ```
1. Run the service by 
    ```bash 
    flask run
    ```
1. You can test playground in `localhost:5000/graphql`
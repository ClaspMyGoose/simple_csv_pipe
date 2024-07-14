
FROM python:latest 

RUN pip install pandas sqlalchemy python-dotenv psycopg2

WORKDIR /app 
COPY csv_ingest_db_load.py script.py


ADD /csvdata /app/csvdata

ENTRYPOINT [ "python", "script.py" ]
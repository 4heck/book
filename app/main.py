from app import app
import psycopg2
from app import db
import api

if __name__ == '__main__':
	app.run(debug=True)
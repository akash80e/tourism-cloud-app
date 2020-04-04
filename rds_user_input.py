# Author: Yashesh Savani
# Cloud Team 12
# Date Created: 29th-March-2020

from flask import Flask
from flask import request
import pymysql.cursors as cursors
import pymysql
import time
import logging
import datetime

# Ref: https://github.com/PyMySQL/PyMySQL

# def encrypt_password(password):
#     encrypted_password =

app = Flask(__name__)


@app.route('/userinsertion')
def user_insertion():

    email = str(request.args.get('email'))
    firstname = str(request.args.get('firstname')).capitalize()
    lastname = str(request.args.get('lastname')).capitalize()
    street_number = int(request.args.get('street_number'))
    street_name = str(request.args.get('street_name')).capitalize()
    apartment = int(request.args.get('apartment'))
    zipcode = str(request.args.get('zipcode')).upper()
    city = str(request.args.get('city')).capitalize()
    province = str(request.args.get('province')).upper()
    date_created = str(datetime.datetime.now())

    while True:
        # Connect to database
        conn = pymysql.connect(host='tourismdb.cefqm5hgun7y.us-east-1.rds.amazonaws.com', port=3306,
                                    user='admin', password='toor12345', db='tourist', charset="utf8mb4",
                                    cursorclass=cursors.DictCursor)
        if conn:
            try:
                cursor = conn.cursor()

                # Insert User data into table on registration
                insert_query = 'INSERT INTO Userdata (Email,Firstname,Lastname,Street_number,Street_name, \
                                Apartment,Zipcode,City,Province,Date_created) \
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                cursor.execute(insert_query, (email, firstname, lastname, int(
                    street_number), street_name, int(apartment), zipcode, city, province, date_created))
                conn.commit()

            finally:
                conn.close()
            break
        else:
            logging.log(
                msg='User registration failed\n Trying to reconnect...', level=logging.DEBUG)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)

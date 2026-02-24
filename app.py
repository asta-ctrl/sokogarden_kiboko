#creating a route for the sign up
from flask import *
import pymysql
from flask_cors import CORS
import os 
#creating flask application
app = Flask(__name__)
CORS(app)#Allow request from external origin
#WE NEED TO CONFIGURE OUR UPOAD FOLDER
app.config['UPLOAD_FOLDER'] = 'static/images'
@app.route('/api/signup',methods=['POST'])
def signup():
     #extracting the values posted in the request and store them in variable
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']    
    phone = request.form['phone']
     
    #connecting to the database
    connection =pymysql.connect(host='localhost',user='root',password='',database ='dailyyoughurts_kiboko')

    #initializing the connection
    cursor = connection.cursor()

    # do the sql querry to insert datain the four columns

    sql='INSERT INTO users (username,email,password,phone) VALUES(%s,%s,%s,%s)' 

    #Create data to replace the placeholders
    data = (username,email,password,phone)

    #execute the sql and the data together using a cursor
    cursor.execute(sql,data)

    #we need to commit/save changes
    connection.commit()

    return  jsonify({"success": "Thank you for joining"})

@app.route('/api/signin',methods=['POST'])
def signin():
     username = request.form['username']
     password = request.form['password']

     connection =pymysql.connect(host='localhost',user='root',password='',database ='dailyyoughurts_kiboko')
     
     cursor = connection.cursor(pymysql.cursors.DictCursor)
     
     sql = 'SELECT * FROM users WHERE username = %s AND password = %s'
    
     data = (username,password)
     
     cursor.execute(sql,data)

     count = cursor.rowcount
     if count == 0:
          return jsonify({"message": "login in failed"})
     else:
          user=cursor.fetchone()
          #removing the passkey
          user.pop('password')
          return jsonify({"message": "login successful", "user": user}) 
     # creating a route called api/add_product
@app.route('/api/add_product', methods=['POST'])#the rote name and the url path
#defining the function
def add_product():
     #Extracting the values posted in the request and store them in variable
     
     product_name=request.form['product_name']

     product_cost=request.form['product_cost']

     product_description=request.form['product_description']

     product_photo=request.files['product_photo']
      #get the filename of the photo
     filename = product_photo.filename
     
     #Specify the complete path to where thge image will be saved
     photo_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)

      #Save the path above taken by the photo
     product_photo.save(photo_path)


     #Establishing connection to the database
     connection =pymysql.connect(host='localhost',user='root',password='',database ='dailyyoughurts_kiboko')
     
     #Initializing the connection
     cursor = connection.cursor()
    
     # do the sql querry to insert datain the four columns
     sql = 'INSERT INTO product_details(product_name,product_description,product_cost, product_photo) VALUES(%s,%s,%s,%s)' 
     
     #Create data to replace the placeholders                                                                 
     data = ( product_name, product_description,product_cost, filename)
     
     #Execute the sql and the data together using a cursor
     cursor.execute(sql,data)
     
     #We are  saving the  changes
     connection.commit()
     
     #Returning a response to the user
     return jsonify({"message": "Product added successfully"})


#We are fetchings the products from the database(dailyyoughurts)
@app.route('/api/get_product_details', methods=['GET'])
def get_product_details():
     #we are connecting to the database
     connection =pymysql.connect(host='localhost',user='root',password='',database ='dailyyoughurts_kiboko')
     #creating cursor object to execute sql querries

     cursor = connection.cursor(pymysql.cursors.DictCursor)
     #sql querry to fetch all the products from the database
     sql = 'SELECT * FROM product_details'
     #executing the sql querry
     cursor.execute(sql)
     #Fetching all the products and storing them in a variable called product_detail
     product_details = cursor.fetchall()
     
     return jsonify(product_details)

# Mpesa Payment Route 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
        if request.method == 'POST':
            # Extract POST Values sent
            amount = request.form['amount']
            phone = request.form['phone']

            # Provide consumer_key and consumer_secret provided by safaricom
            consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
            consumer_secret = "amFbAoUByPV2rM5A"

            # Authenticate Yourself using above credentials to Safaricom Services, and Bearer Token this is used by safaricom for security identification purposes - Your are given Access
            api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
            # Provide your consumer_key and consumer_secret 
            response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
            # Get response as Dictionary
            data = response.json()
            # Retrieve the Provide Token

            #  GETTING THE PASSWORD
            timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')  # Current Time
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Passkey(Safaricom Provided)
            business_short_code = "174379"  # Test Paybile (Safaricom Provided)
            # Combine above 3 Strings to get data variableg
            data = business_short_code + passkey + timestamp
            # Encode to Base64
            encoded = base64.b64encode(data.encode())
            password = encoded.decode()

            # BODY OR PAYLOAD
            payload = {
                "BusinessShortCode": "174379",
                "Password":password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": "1",  # use 1 when testing
                "PartyA": phone,  # change to your number
                "PartyB": "174379",
                "PhoneNumber": phone,
                "CallBackURL": "https://coding.co.ke/api/confirm.php",
                "AccountReference": "SokoGarden Online",
                "TransactionDesc": "Payments for Products"
            }

            # POPULAING THE HTTP HEADER, PROVIDE THE TOKEN ISSUED EARLIER
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }

            # Specify STK Push  Trigger URL
            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  
            # Create a POST Request to above url, providing headers, payload 
            # Below triggers an STK Push to the phone number indicated in the payload and the amount.
            response = requests.post(url, json=payload, headers=headers)
            print(response.text) # 
            # Give a Response
            return jsonify({"message": "An MPESA Prompt has been sent to Your Phone, Please Check & Complete Payment"})
      
if __name__ == '__main__':
     app.run(debug=True)

   



    
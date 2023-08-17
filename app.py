from flask import Flask, render_template, request
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        name = data['name']
        database.write(f'\n ------------ NAME:{name}  EMAIL: {email} \n SUBJECT:{subject} \n MESSAGE: {message}')


def write_to_csv(data):
  with open('database2.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    name = data["name"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,name,subject,message])



@app.route('/', methods=['POST', 'GET'])
def submit_form():
    data = request.form.to_dict()
    write_to_file(data)
    write_to_csv(data)
    # write_to_file(data)
    return render_template('index.html')


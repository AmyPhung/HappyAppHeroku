from flask import Flask, redirect, url_for, request, render_template
from SendEmail import sendEmailTo
import json
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(emailaddress=None):
    if request.method == 'POST':
        email = request.form["emailaddress"]
        print(email)
        success_flag = sendEmailTo(email)
        print("it worked!")
        print(success_flag)
        if success_flag == True:
            return render_template('done.html')
        else:
            return render_template('error404.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

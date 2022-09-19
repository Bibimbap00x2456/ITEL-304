from flask import Flask, request
from datetime import datetime

app = Flask(__name__)







@app.route('/')
def home():
        return"""
            <html><body>
                <h2>Welcome to the Greeter</h2>
                <form action = "/meet">
                    What's your name? <input type ='text' name= 'username'><br>
                    Can you tell me something about yourself? <input type ='text' name='self'><br>
                    <input type = 'submit' value = 'Continue'>
                </form>
                </body></html>
                """

@app.route('/meet')
def meet ():
    username = request.args.get('username','World')
    self = request.args['self']
    if self == '':
        msg ='You dont want to tell me anything? '
    else:
        msg = self + ' is ' + username + ' characteristic'
    return"""
        <html><body>
            <h2>Im ,{0}!</h2>
            {1}<br><br><br>
            <form action = '/reply'>
            what about your name? <input type = 'text' name = 'myreply'><br>
            <input type = 'submit' value = 'Continue'>
            </form>
            
        </body></html>
        """.format(username , msg)
@app.route('/reply')
def reply ():
        thereply = request.args['myreply']
        if thereply == '':
            msg = 'ok!? bye then'
        else:
            msg = 'nice to meet you ' + thereply
            return"""
            <html><body>
            <h2> {0}</h2>
            </body></html>
            """.format(msg)



#Lunch the FlaskPy dev server
app.run(host = "localhost", debug=True)
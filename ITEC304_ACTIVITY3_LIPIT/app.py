from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
        return"""
            <html lang="en">
                <head>
                    <Title>Jethro Lipit Calculator</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
                    
                    <style>
                    div.form-check{
                        font-size: 25px;
                    {
                    </style>
                    
                </head>
            
            <body>
                <h1 style="margin-left: 300px;">Welcome to my Calculator</h2>
                <form action = "/ans">
                    <h2 style="margin-left: 300px;">First number <input type ='text' name= 'fn'></h2><br>
                    <h2 style="margin-left: 300px;">Second number <input type ='text' name='sn'></h2><br>
                    
                    <div class="container mt-3">
                        <h2 style="margin-left: 10px;">Operation</h2>
                        <form action="/action_page.php">
                            <div class="form-check">
                                <input type="radio" class="form-check-input" id="radio1" name="optradio" value="option1" checked>
                                <label class="form-check-label" for="radio1">addition</label>
                            </div>
                            <div class="form-check">
                                <input type="radio" class="form-check-input" id="radio2" name="optradio" value="option2">
                                <label class="form-check-label" for="radio2">subtraction</label>
                            </div>
                            <div class="form-check">
                                <input type="radio" class="form-check-input" id="radio3" name="optradio" value="option3">
                                <label class="form-check-label" for="radio3">multiplication</label>
                            </div>
                            <div class="form-check">
                                <input type="radio" class="form-check-input" id="radio4" name="optradio" value="option4">
                                <label class="form-check-label" for="radio4">division</label>
                            </div>
                            <button type="submit" class="btn btn-primary mt-3">Submit</button>
                        </form>
                    </div>
                </form>
                </body></html>
                """



@app.route('/ans')
def ans ():
    fn = int(request.args['fn'])
    sn = int(request.args['sn'])
    op = request.args['optradio']

    if (fn =='' or sn == ''):
        ans = 'please input some value'


    if op == 'option1':
        ans = fn + sn
    elif op == 'option2':
        ans = fn - sn
    elif op == 'option3':
        ans = fn * sn
    elif op == 'option4':
        if (fn >= 1 and sn == 0):
            ans = 'this cannot devide by zero'
        elif (fn == 0 and sn >= 1):
            ans = '0'
        else:
            ans = fn / sn



    return"""
        <form action = "/">
            <h2 style="font-size: 150px; text-align: center;">= {0}</h2>
            </body></html>
            <button style = "border-radius: 8px; background-color: blue; border: none; padding: 20px; color: white; margin: 1px 1000px; font-size: 100px;" type= "submit">back</button>
        </form>
        """.format(ans)

app.run(host = "localhost", debug=True)
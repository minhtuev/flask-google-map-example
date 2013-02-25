from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/googleMap.html")
def googleMap():
    return redirect(url_for('static', filename='googleMap.html'))

@app.route("/extensiveDemo.html")
def extensiveDemo():
    return redirect(url_for('static', filename='extensiveDemo.html'))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template
from threading import Thread

app = Flask('')

@app.route('/')
def index():
  return "Server running"

def run():
    app.run(host='0.0.0.0', port=8080)
    
def server_thread():
    #Object to be executed by the thread
    t = Thread(target=run)
    t.start()
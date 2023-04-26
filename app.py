from flask import Flask

app=Flask(__name__)


@app.route('/<name>')
def home(name):
    return 'hello'+str(name)

if __name__=="__main__":
    app.run(debug=True)
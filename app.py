from flask import Flask 

app = Flask(__name__)

@app.route('/')
def Hello():
	return "Hey! There"

if __name__ == "__main__":
	app.run()
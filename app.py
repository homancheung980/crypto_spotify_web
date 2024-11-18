from flask import Flask, render_template, request
from bitcoin_spotify import get_btcplaylist
#from weather_spotify import get_playlist


# Initialize Flask app
app = Flask(__name__)


# Landing page
@app.route('/')
def index():
	# Use the default crypto (BTC) for the initial playlist
	default_crypto = "90"
	my_playlist = get_btcplaylist(default_crypto)  #set up default input
	return render_template('index.html', playlist_id = my_playlist)


# Handle POST requests to generate a playlist for the user's city
@app.route('/', methods=['POST'])
def index_post():
	selected_crypto = request.form.get('crypto')
	if selected_crypto:
		my_playlist = get_btcplaylist(selected_crypto)
		return render_template('index.html', playlist_id= my_playlist)

	else:
		return render_template('index.html', error = "Please select a cryptocurrency")

![Screenshot 2024-11-05 151300](https://github.com/homancheung980/crypto_spotify_web.git/blob/main/images/img1.png)

<h2 align="center">Crypto Playlist Generator, based on Bitcoin and now with Ethereum.</h2>



<p align="center">
  <a href="#Description">Description</a> •
  <a href="#APIs Used ">APIs</a> •
  <a href="#Preperations (2 Steps)">Preperation</a> •
  <a href="#How this code works">How this code works</a> •
  <a href="#Credits">Credits</a> •
  <a href="#Note and More">Note and More</a>
</p>



*ChatGPT is used a lot in this project, I somehow had trouble understanding where do I start, I wasn't able to code from zero whilst I am happy to explain how every code works in this prototype.

### Description

This is a python code with FLASK to allow you to generate to generate your own crypto playlist via a webpage!The playlist will be based on the price changes of Bitcoin and Ethereum based on the previous 24 hours.

![Screenshot 2024-11-05 151300](C:\Users\Homan\OneDrive - Hogarth Worldwide\Documents\CreativeCoding\crypto_spotify_web\images\img2.png)

### APIs Used 

Spotify API : https://developer.spotify.com/documentation/web-api

CoinLore API : https://www.coinlore.com/cryptocurrency-data-api





### Preperations (2 Steps)



**1- Get the spotify API tokens** 

Please have your [SpotifyDeveloper Account](https://developer.spotify.com/documentation/web-api) ready, from the account you should have 4 main data (username/client_id/client_secret/redirect) for your to put this JSON file* template which looks like this:

```bash
{
    "username": <your spotify developer account name here>, 
    "client_id": <your client id number>,
    "client_secret": <your client id number>,
    "redirect": <your redirect link>
}
```

> **Note***
> **Please keep the key names untouched** and have your **key values set as a string** **with double quotes** in this dictionary for conveniency later on in the code.



**2- Get the Bitcoin API** 

The is a relatively simple API to obtain, all we need is a link located in the **btc_api.txt** file, which I have assigned the name "url" for the link. Alternatively you can copy the code below without having to convert strings into a variable:

```HTML
https://api.coinlore.net/api/ticker/?id=90 (BTC)
https://api.coinlore.net/api/ticker/?id=80 (ETH)
```

After setting up the url, please use the library **urllib** to open, receive and pull out the JSON list, which I have named **"crypto_json"** in my example code.



**3- Install libraries** 

Please install **jupyter** and **spotipy**  in your python library as they are not by default.





## How this code work

This Python code generates a Spotify playlist based on the 24-hour price change of Bitcoin, using the CoinLore API to track BTC's movement. If Bitcoin's price goes up, the script collects 400 songs from Spotify, filters out and pick 10 of them based on customizable audio features (such as energy, tempo, etc.), and assigns a user-specified emoji image as the playlist cover.

#### Features

- **Customizable Filters**: Modify audio feature thresholds (e.g., tempo, danceability) to customize the playlist to your taste.

- **Flexible Cover Image**: Swap the playlist cover emoji image to any URL you like.

  

#### Setup

1. Clone this repository.
2. Install required packages (e.g., `spotipy`, `base64`, `requests`).
3. Authentication with Spotify with your `client_id`, `client_secret`, and `redirect_uri` mentioned in the Preperations section.
4. Adjust **Search Parameters*, Audio Features parameters, No. of songs in playlist and Cover Image** as desired.

> **Note***
> When adjusting search parameters, sometimes the SpotifyAPI might return a message of "BAD REQUEST", just keep refreshing until it prints out something successfully. 



## Credits

This software uses the following open source packages:

- [Spotify API](https://developer.spotify.com/documentation/web-api)
- [CoinLore](https://www.coinlore.com/cryptocurrency-data-api)
- [Sublime (text editor)](https://www.sublimetext.com/)

## Note and More

---

Special thanks to everyone who helped me throughout the Creative Tech Apprenticeship 2024

GitHub [https://github.com/homancheung980]&nbsp;&middot;&nbsp;

witter.com/amit_merchant)


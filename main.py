from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'Cr6ZcBdW4MC8yo6foRAMPp09h'
csecret = 'cQizXmeD4wv4A5Ek2F8LNQ2sQoVfYmDJhRTEqBKD7EdNTKj7b2'
atoken = '825875016608841730-TKbKCdp0Z55L99nLvw9gRjfz33nP8GG'
asecret = '9I5EeD1v8Dw9lxbwpuf1FI2wpRIQospygJD3A3Z0bNKAY'

class Listener(StreamListener):
	def on_data (self, data):
		tweet = data.split(',"text":"')[1].split('","source')[0]
		for letter in tweet:
			number = ord(letter)
			print (letter)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["keyword"])

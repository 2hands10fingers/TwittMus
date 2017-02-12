from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'Cr6ZcBdW4MC8yo6foRAMPp09h'
csecret = 'cQizXmeD4wv4A5Ek2F8LNQ2sQoVfYmDJhRTEqBKD7EdNTKj7b2'
atoken = '825875016608841730-TKbKCdp0Z55L99nLvw9gRjfz33nP8GG'
asecret = '9I5EeD1v8Dw9lxbwpuf1FI2wpRIQospygJD3A3Z0bNKAY'
tweet_data =[]

class Listener(StreamListener):
	def on_data (self, data):
		tweet = data.split(',"text":"')[1].split('","source')[0].split('","display_text_range')[0].encode("utf-8")
		for i in range(0, len(tweet)):
			tweet_data.append(tweet[i])
			print tweet_data

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["seat"])

"""
>>>>>PHASES<<<<<<<<
Phase 1: Streaming and Sortinng
		1. Streaming
		2. Parsing
		3. Assigning it to an array
		4. Creating prompt for keyword <-- WE ARE HERE
	Phase 2: Conversion
		1. Decide on and assign characters in the array to MIDI values
		2. Send array
		3. Decide send method (MIDI values -> MIDI device or directly to Ableton)
	Phase 3: Musical Testing
		1. Test MIDI input speed (speed it up? Slow it down?)
		2. Set musical parameters in Ableton
		3. Tune aesthetics
"""

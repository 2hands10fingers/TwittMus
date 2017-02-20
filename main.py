from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'Cr6ZcBdW4MC8yo6foRAMPp09h'
csecret = 'cQizXmeD4wv4A5Ek2F8LNQ2sQoVfYmDJhRTEqBKD7EdNTKj7b2'
atoken = '825875016608841730-TKbKCdp0Z55L99nLvw9gRjfz33nP8GG'
asecret = '9I5EeD1v8Dw9lxbwpuf1FI2wpRIQospygJD3A3Z0bNKAY'
tweet_data =[]
#tweet_conver=[]

class Listener(StreamListener):

	def on_data (self, data):

		tweet = data.split(',"text":"')[1].split('","source')[0].split('","display_text_range')[0].encode("utf-8")

		for i in range(0, len(tweet)):
			tweet_data.append(tweet[i])
			tweetMidiAss = [i.replace('A', '4').replace('B', '5').replace('C', '7')
			.replace('D', '105').replace('E', '11').replace('F', '12').replace('G', '14')
			.replace('H', '16').replace('I', '17').replace('J', '19').replace('K', '21')
			.replace('L', '23').replace('M', '24').replace('N', '26').replace('O', '28')
			.replace('P', '29').replace('Q', '31').replace('R', '33').replace('S', '35')
			.replace('T', '36').replace('U', '38').replace('V', '40').replace('W', '41')
			.replace('X', '43').replace('Y', '45').replace('Z', '47').replace('a', '48')
			.replace('b', '50').replace('c', '52').replace('d', '53').replace('e', '55')
			.replace('f', '57').replace('g', '59').replace('h', '60').replace('i', '62')
			.replace('j', '64').replace('k', '65').replace('l', '67').replace('m', '69')
			.replace('n', '71').replace('o', '72').replace('p', '74').replace('q', '76')
			.replace('r', '77').replace('s', '79').replace('t', '81').replace('u', '83')
			.replace('v', '84').replace('w', '86').replace('x', '88').replace('y', '89')
			.replace('z', '91').replace(',', '93').replace('.', '95').replace('!', '96')
			.replace('@', '98').replace('$', '101').replace('%', '103').replace('^', '105')
			.replace('&', '107').replace('*', '108').replace('(', '110').replace(')', '112')
			.replace('-', '113').replace('_', '115').replace('+', '117').replace('\\', '119')
			.replace('{', '120').replace('}', '122').replace('[', '124').replace(']', '125')
			.replace('?', '127').replace('/', '60').replace('|', '60') for i in tweet_data]

		print tweetMidiAss

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["keyword"])


""" >>>>>PHASES<<<<<<<<
Phase 1: Streaming and Sortinng
		1. Streaming
		2. Parsing
		3. Assigning it to an array
		4. Creating prompt for keyword <-- WE ARE HERE
	Phase 2: Conversion
		1. Assign characters in array to MIDI values
		2. Send array
		3. Decide send method (MIDI values -> MIDI device or directly to Ableton)
	Phase 3: Musical Testing
		1. Test MIDI input speed (speed it up? Slow it down?)
		2. Set musical parameters in Ableton
		3. Tune aesthetics
"""

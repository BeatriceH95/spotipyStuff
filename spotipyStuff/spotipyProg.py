import sys
import spotipy
import spotipy.util as util


def main():

	#name = "Creed"		
	#spotify = spotipy.Spotify()
	#results = spotify.search(q='artist:' + name, type='artist')
	#print(results)

	scope = 'user-library-read'

	if len(sys.argv) > 1:
   		username = sys.argv[1]
	else:
		print("Usage: " + sys.argv[0] + "username")
		sys.exit()

	token = util.prompt_for_user_token(username, scope)

	if token:	
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			print(track['name'] + ' - ' + track['artists'][0]['name'])
	else:
		print("Can't get token for", username)












main()

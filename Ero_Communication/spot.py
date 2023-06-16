import speech_recognition as sr
import spotipy
import spotipy.util as util
import os
import webbrowser

# Spotify API credentials
CLIENT_ID = "d59c2afd3d144d61be5909073f876947"
CLIENT_SECRET = "7c373fb204e44c6d800d68f598920405"
REDIRECT_URI = "http://localhost:8888"
USERNAME = "31ef25bfofim3eoyrhmbtkpsbs3e"

# Set up speech recognition
r = sr.Recognizer()

# Set up Spotify API
token = util.prompt_for_user_token(
    USERNAME,
    "user-read-playback-state user-modify-playback-state",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI
)
sp = spotipy.Spotify(auth=token)

# Function to play a song


def play_song(song_name):
    # Search for the song using Spotify API
    results = sp.search(q=song_name, limit=1, type='track')

    # Check if any results were found
    if results['tracks']['items']:
        # Get the URI of the first track
        track_uri = results['tracks']['items'][0]['uri']

        # Play the song using Spotify API
        sp.start_playback(uris=[track_uri])
        print("Playing:", song_name)
    else:
        print("No results found for:", song_name)

# Function to take speech input and play song


def take_speech_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        query = r.recognize_google(audio)
        print("Heard:", query)

        # Play the song based on the speech input
        play_song(query)
    except sr.UnknownValueError:
        print("Unable to understand speech")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))


# Main loop
while True:
    take_speech_input()

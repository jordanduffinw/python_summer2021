### Setup
import os
os.chdir(r'C:\Users\jorda\OneDrive\Keys')

import importlib
import spotipy

credentials = importlib.import_module('start_spotify_jdw')
sp = spotipy.Spotify(client_credentials_manager=credentials.client_credentials)

### First, scraping the campaign tracks according to NYT
#https://www.nytimes.com/interactive/2019/08/19/us/politics/presidential-campaign-songs-playlists.html

def get_playlist_tracks(username, playlist_id):
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


### Biden's playlist -- s/out to user Zachariah Tollison for compiling
biden = get_playlist_tracks('1279940683', '5SYfP24TW8krXwBM9wT7Pp')

### Trump's playlist -- s/out to user Cody Porter for compiling
trump = get_playlist_tracks('1257617527', '7673XgxqA16yhdVEFvpYyh')

### Combining playlists
playlist = biden + trump

# Resetting the output directory
os.chdir(r'C:\Users\jorda\OneDrive\Python_Camp\python_summer2021\Project')

### Storing track information as a CSV:
import csv

with open("campaignsongs.csv", "w", newline = "") as f:
    w = csv.DictWriter(f, fieldnames = ("Playlist", "Song", "SongID", "Artist", "Acousticness",
                                        "Danceability", "Duration",
                                        "Energy", "Instrumentalness", "Key",
                                        "Liveness", "Loudness", "Mode", "Speechiness",
                                        "Tempo", "Time Signature",
                                        "Valence"))
    w.writeheader()
    playlists = {}
    
    for i in range(len(playlist)):
        if playlist[i]['added_by']['id'] == '1279940683':
            playlists["Playlist"] = "Biden"
        else:
            playlists["Playlist"] = "Trump"
    
        playlists["Song"] = playlist[i]['track']['name']
        songid = playlist[i]['track']['id']
        playlists["SongID"] = songid
        playlists["Artist"] = playlist[i]['track']['album']['artists'][0]['name']
        
        features = sp.audio_features(songid)
        
        playlists["Acousticness"] = features[0]['acousticness']
        playlists["Danceability"] = features[0]['danceability']
        playlists["Duration"] = features[0]['duration_ms'] / 1000
        playlists["Energy"] = features[0]['energy']
        playlists["Instrumentalness"] = features[0]['instrumentalness']
        playlists["Key"] = features[0]["key"]
        playlists["Liveness"] = features[0]['liveness']
        playlists["Loudness"] = features[0]['loudness']
        playlists["Mode"] = features[0]['mode']
        playlists["Speechiness"] = features[0]['speechiness']
        playlists["Tempo"] = features[0]["tempo"]
        playlists["Time Signature"] = features[0]["time_signature"]
        playlists["Valence"] = features[0]['valence']
        
        w.writerow(playlists)

### Analysis -- done in RStudio!

### Some notes on the sp.audio_features https://developer.spotify.com/documentation/web-api/reference/#category-tracks :
    # - acousticness: a measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic
    # - analysis_url: a URL to access the full audio analysis of this track. An access token is required to access this data
    # - danceability: describes how suitable a track is for dancing based on a combination of musical elements including tempo,
    #   rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable
    # - duration_ms: the duration of the track in milliseconds
    # - energy: a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks
    #   feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual
    #   features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy
    # - id: the Spotify ID for the track
    # - instrumentalness: predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context.
    #   Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track
    #   contains no vocal content. Values above 0.5 are meant to represent instrumental tracks, but confidence is higher as the value
    #   approaches 1.0
    # - key: the key the track is in. Integers map to pitches using standard pitch class notation.
    #   refer to https://en.wikipedia.org/wiki/Pitch_class for mapping
    # - liveness: detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track
    #   was performed live. A value above 0.8 provides strong likelihood that the track is live.
    # - loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for
    #   comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical
    #   strength (amplitude). Values typical range between -60 and 0 db.
    # - mode: indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented
    #   by 1 and minor is 0
    # - speechiness: detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audiobook,
    #   poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words.
    #   Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including cases
    #   such as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
    # - tempo: the overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given
    #   piece and derives directly from average beat duration
    # - time_signature: an estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how
    #   many beats are in each bar (or measure)
    # - track_href: a link to the Web API endpoint providing full details of the track
    # - type: the object type
    # - uri: the Spotify URI for the track
    # - valence: a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive
    #   (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)
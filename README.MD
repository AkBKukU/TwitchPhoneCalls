# Twitch Phone Call Bot

This is very early release/initial of a set of small programs and a config file I made for creating a channel point redemption on my Twitch channel that allows my viewers to ring a phone and "call" me over TTS.

These files, including audio.xml, will need to be modified to use on your system as there are paths hard coded for my user directory where I was running this and with my Twitch channel name in the python code. You also need to obtain a `client_id` and `client_secret` to have access to the Twitch API. You will need to modify the file path in the python code for where it looks for that as well.

You will also need to find the IP adress for your ATA and change it in `call.sh`.

Required software
 - `Festival` for TTS
 - `TwitchAPI` through `pip3` for the python code
 - `SIPp` for the phone interfacing done in `call.sh`
 - `ffmpeg` for converting audio files

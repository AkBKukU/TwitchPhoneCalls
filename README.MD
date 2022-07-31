# Twitch Phone Call Bot

This is very early release/initial of a set of small programs and a config file I made for creating a channel point redemption on my Twitch channel that allows my viewers to ring a phone and "call" me over TTS.

The python code does not currently have a single set redemption filter so it currently will call for any custom channel point reward.

These files, including audio.xml, will need to be modified to use on your system as there are paths hard coded for my user directory where I was running this and with my Twitch channel name in the python code. You also need to obtain a `client_id` and `client_secret` to have access to the Twitch API. You will need to modify the file path in the python code for where it looks for that as well.

You will also need to find the IP adress for your ATA and change it in `call.sh`.

Required software
 - `Festival` for TTS
 - `TwitchAPI` through `pip3` for the python code
 - `SIPp` for the phone interfacing done in `call.sh`
 - `ffmpeg` for converting audio files

Optional software
 - Any tool that can play back a WAV file; sox's `play`, ALSA's `aplay`, FFmpeg's `ffplay`, and so on.

# Hardware

You'll need
- a Plain Old Telephone System phone; you get more style points for older phones
- some form of Analog Telephone Adapter (ATA) with FXS ports; examples include a Linksys/Cisco SPA2102 or Grandstream HT801

Since the phone is only being used to receive calls, it can be a rotary/pulse phone.

# Software

## Ubuntu packages
 - Festival TTS - `apt install festival festvox-us-slt-hts`
 - SIPp - `apt install sip-tester`
 - FFmpeg - `apt install ffmpeg`

Other voice packs are available; `apt search festvox-`

# Testing Festival

To test Festival, run the festival command.

    festival

At the `festival>` prompt, check what voices are available.

    (voice.list)

The output will show all of the available voices; here we're highlighting the one used for this project.

    (... cmu_us_slt_artic_hts ...)

Switch to the `cmu_us_slt_arctic_hts` voice; prefix the name with `voice_`.

    (voice_cmu_us_slt_artic_hts)

Festival will print back the name without `voice_` prefixed.

    cmu_us_slt_artic_hts

Have festival say something.

    (SayText "Daisy, Daisy, give me your answer do.")

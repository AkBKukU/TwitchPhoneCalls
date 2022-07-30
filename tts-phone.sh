#!/bin/bash

cat /home/akbkuku/tts/tts.txt | text2wave -eval '(voice_cmu_us_slt_arctic_hts)' > /home/akbkuku/tts/tts.wav && ffmpeg -y -f concat -safe 0 -i /home/akbkuku/tts/loop.txt /home/akbkuku/tts/loop.flac && ffmpeg -y -i /home/akbkuku/tts/loop.flac -codec:a pcm_alaw -ar 8000 -ac 1 /home/akbkuku/tts/tts-8k.wav

cp /home/akbkuku/tts/tts.wav /home/akbkuku/tts/log/tts$(date +"%Y-%m-%d_%H-%M-%S").wav
cp /home/akbkuku/tts/tts.txt /home/akbkuku/tts/log/tts$(date +"%Y-%m-%d_%H-%M-%S").txt

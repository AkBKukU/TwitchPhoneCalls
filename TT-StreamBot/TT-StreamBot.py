#!/usr/bin/python3

import sys, os
from twitchAPI.twitch import Twitch
from twitchAPI.pubsub import PubSub
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from pprint import pprint
from uuid import UUID

from pprint import pprint
from ttbot.key import APIKey

api = APIKey("/home/akbkuku/client.json")
twitch = Twitch(api.client_id, api.client_secret)
pprint(twitch.get_users(logins=['TechTangents']))


def callback_whisper(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    pprint(data)
    with open('/home/akbkuku/tts/tts.txt', 'w', encoding="utf-8") as text:
        text.write(data['data']['redemption']['user']['display_name'] + " said " + data['data']['redemption']['user_input'])

    os.system("/home/akbkuku/tts/tts-phone.sh && /home/akbkuku/tts/call.sh")


target_scope = [AuthScope.CHANNEL_READ_REDEMPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()
# add User authentication
twitch.set_user_authentication(token, target_scope, refresh_token)
user_id = twitch.get_users(logins=['TechTangents'])['data'][0]['id']


# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()
# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_channel_points(user_id, callback_whisper)
input('press ENTER to close...')
# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
pubsub.unlisten(uuid)
pubsub.stop()

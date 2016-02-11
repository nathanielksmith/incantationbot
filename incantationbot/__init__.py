#!/usr/bin/env python
# This program is part of haikuthegibson.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from random import randint, shuffle
import sys

import tweepy
from smarkov import Markov

from secret import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

names = ["cthulhu",
         "nyarlathotep"
         "yog sothoth",
         "shuggoth",
         "shub niggurath",
         "yig",
         "azathoth",
         "dagon",
         "kadath",
         "ghatanothoa",
         "ithaqua",
         "hastur",
         "mi go",
         "gaunt",
         "tsathoggua",
         "yuggoth",
         "ulthar",
         "sarnath",
         "zin",
         "gug",
         "pnath",
         "sarkomand",
         "nodens",
         "bhole",]

def main():
    twitter_auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    twitter_client = tweepy.API(twitter_auth)

    print("building model...")

    shuffle(names)
    text = ' '.join(names)
    chain = Markov([text])

    print("making sentence...")
    length = randint(20, 35)
    result = ''
    while len(result) == 0:
        result = ''.join(chain.generate_text()[0:length])

    result = result.rstrip() + '!'

    print('tweeting...')
    print(result)
    try:
        response = twitter_client.update_status(status=result)
        print(response)
        return response
    except tweepy.error.TweepError as e:
        print(e)
        return e

if __name__ == '__main__':
    result = main()

    if isinstance(result, tweepy.error.TweepError):
        code = 1
    else:
        code = 0

    sys.exit(code)

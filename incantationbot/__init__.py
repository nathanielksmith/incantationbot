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
import sys

import tweepy
import markovify

import incantationbot.secret as secret


def main():
    twitter_auth = tweepy.OAuthHandler(secret.API_KEY, secret.API_SECRET)
    twitter_auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_SECRET)

    twitter_client = tweepy.API(twitter_auth)


    try:
        return twitter_client.update_status(status='TODO')
    except tweepy.error.TweepError as e:
        return e

if __name__ == '__main__':
    result = main()

    if isinstance(result, tweepy.error.TweepError):
        code = 1
    else:
        code = 0

    sys.exit(code)

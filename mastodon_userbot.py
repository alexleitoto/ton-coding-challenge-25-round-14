from mastodon import Mastodon
import time

mastodon = Mastodon(
    access_token="token.secret",
    api_base_url="https://mastodon.social"
)

while True:
    mentions = mastodon.notifications()
    for note in mentions:
        if note["type"] == "mention":
            mastodon.status_post("@{} pong".format(note["account"]["acct"]),
                                 in_reply_to_id=note["status"]["id"])
    time.sleep(10)

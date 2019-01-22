import os
import json
import facebook
import requests

if __name__ == '__main__':
    FACEBOOK_TEMP_TOKEN = "EAAdN7HljNZCUBAKpeA3GwLjZAZB4aIOczgWuWYlC7ZCRZCWfoq5TahubZCI8DbGg2XNzyFp7E9rE5upgT63ihI" \
                          "Mbczd6hQyWaX04OsLEEWLCv3buTN4GHkeKDVLizuuc4rImIflT3XS1nqkIS4Bn7LTof8PLf9VL6DQXIy0nHgnWw" \
                          "pzgdToYKUZCgZBY2ArznAYg2DESZCBrhDAZDZD"
    #token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    token = FACEBOOK_TEMP_TOKEN

    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='name,location{location}')
    user = graph.get_object('me')
    friends = graph.get_connections(user["id"], "friends")

    all_fields = [
        'message',
        'created_time',
        'description',
        'caption',
        'link',
        'place',
        'status_type'
    ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me', 'posts', fields=all_fields)
    

    while True:
        try:
            with open('my_posts.json3', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break

import facebook
import requests

# Get the new access_token after its expiry time
# TODO figure out way to connect it using APP_ID and APP_KEY via curl and http request
def get_api(cfg):

    graph = facebook.GraphAPI(access_token=cfg['access_token'], version='2.8')

    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
            return graph

cfg = {
            "page_id"      : "my_page_id",
            "access_token" : "EAACEdEose0cBALlA4ZAYjzjQWCXLm3ZCmwMVdS81MTO9TZBaYu7nZAkRT3ONWGFdJ43vC9IanNgLhcPFHmh9mP0VKQb9wnAvdk00GzHOWU1OrR1O3K6V3PS8jYtLfi4xmEAfGuZAn0k3oXWuvr6mfDJIS3jnB49AgYvDIYZAtS1CjzJ16tBugic1ej5eZAfugsZD"
      } 

graph = facebook.GraphAPI(access_token='EAACEdEose0cBALlA4ZAYjzjQWCXLm3ZCmwMVdS81MTO9TZBaYu7nZAkRT3ONWGFdJ43vC9IanNgLhcPFHmh9mP0VKQb9wnAvdk00GzHOWU1OrR1O3K6V3PS8jYtLfi4xmEAfGuZAn0k3oXWuvr6mfDJIS3jnB49AgYvDIYZAtS1CjzJ16tBugic1ej5eZAfugsZD', version='2.8')
msg = "Hello world!"
status = graph.put_object(parent_object='me', connection_name='feed',
                 message='Hello, world')

print("Second part")

graph = facebook.GraphAPI(access_token)
profile = graph.get_object('me')
args = {'fields' : 'id,name,email', }
profile = graph.get_object('me', **args)
friends = graph.get_connections(profile['id'], "friends")
print(friends)
posts = graph.get_connections(profile['id'], 'posts')

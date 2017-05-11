import json
import os
import urllib.request

################################################################################

def fetch_data(url, api_key):
    request = urllib.request.Request(url)
    # standard authorization for FB
    request.add_header('Authorization', 'Bearer {}'.format(api_key))

    response = urllib.request.urlopen(request)
    encoding = response.headers.get_content_charset()

    data = json.loads(response.read().decode(encoding))
    
    return data 

################################################################################

def get_next_from_data(data):
    # check for paging key in the data

    if 'paging' in data:
        paging = data['paging']
        if 'next' in paging:
            return paging['next']
        else:
            return None
    else:
        return None

################################################################################

def iterate_over_images(data, user_id, pic_number):
    for data_object in data:
        pic_url = data_object['source']
        f = open('{}.jpg'.format(pic_number), 'wb')
        f.write(urllib.request.urlopen(pic_url).read())
        f.close()

        pic_number = pic_number + 1

################################################################################

if __name__ == '__main__':

    # TODO for now support for 2.3 but upgrade to 2.9
    # TODO require extra efforts as parsing will be on the basis of ID only
    # TODO direct image url is not available in v2.9 api set

    base_url = "https://graph.facebook.com/v2.3/"

    facebook_access_token = 'EAACEdEose0cBACAxdIh7k5GKhLEnShg3BTRHu8R8EiJXw0ro4BO62NeKTIPQoDSWn1ejC1ZCqUmdMdY5zOtInGQS9ucy62QhA0BZBQuJmttWDBmBeeFcpJZBrUlkiFJ8WWZADe6ZBeV4YAlVFq5P3Qnp9irIZAYZAxEbyqz57keFPH5ZAVBCDGU0OoNatrINjlsZD'

    if not os.path.exists("fb_pictures"):
        os.makedirs("fb_pictures")
    os.chdir("fb_pictures")

    data = fetch_data(base_url+"me", facebook_access_token)

    user_id = data['id']

    data = fetch_data(base_url+"me/photos", facebook_access_token)
    next_ = get_next_from_data(data)

    data = data['data']
    pic_num = 0
    iterate_over_images(data, user_id, pic_num)
    pic_num += len(data)

    print(len(data))
    
    if next_ is None:
        is_more_photos = False
    else:
        is_more_photos = True 

    while(is_more_photos):
        data = fetch_data(next_, facebook_access_token)
        next_ = get_next_from_data(data)

        data = data['data']
        iterate_over_images(data, user_id, pic_num)

        pic_num += len(data)
        print(len(data))
        if next_ is None:
            is_more_photos=False

    print("Completed")

class EndpointUrls:
    def __init__(self, endpoint, username):
        self.endpoint = endpoint
        self.username = username

    def get_endpoint(self):
        endpoints = {
            "search_user": f'https://api.twitter.com/2/users/by/username/{self.username}'
        }

        if(self.endpoint == "search"):
            return endpoints["search_user"]
        
        return "Endpoint not found"
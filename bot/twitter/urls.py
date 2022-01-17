class EndpointUrls:
    def __init__(self, endpoint, username=None):
        self.endpoint = endpoint
        self.username = username

    @property
    def get_endpoint(self):
        endpoints = {
            "search_user": f'https://api.twitter.com/2/users/by/username/{self.username}',
            "tweet_by_topic": "https://api.twitter.com/2/tweets/search/recent"
        }

        if self.endpoint == "search":
            return endpoints["search_user"]

        if self.endpoint == "tweet_by_topic":
            return endpoints["tweet_by_topic"]

        return "Endpoint not found"

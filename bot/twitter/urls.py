class EndpointUrls:
    def __init__(self, endpoint, username=None, user_id=None, tweet_id=None):
        self.endpoint = endpoint
        self.username = username
        self.user_id = user_id
        self.tweet_id = tweet_id

    @property
    def get_endpoint(self):
        endpoints = {
            "search_user": f'https://api.twitter.com/2/users/by/username/{self.username}',
            "tweet_by_topic": "https://api.twitter.com/2/tweets/search/recent",
            "tweet_search": f'https://api.twitter.com/2/users/{self.user_id}/tweets',
            "tweets_by_id": f'https://twitter.com/{self.username}/status/{self.tweet_id}'
        }

        if self.endpoint == "search":
            return endpoints["search_user"]

        if self.endpoint == "tweet_by_topic":
            return endpoints["tweet_by_topic"]

        if self.endpoint == "tweet_search":
            return endpoints["tweet_search"]

        if self.endpoint == "tweets_by_id":
            return endpoints["tweets_by_id"]

        return "Endpoint not found"

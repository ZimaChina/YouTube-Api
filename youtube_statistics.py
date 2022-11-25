
class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key,
        self.channel_id = channel_id,
        self.channel_stats = None    
    
    def get_channel_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        print(url)

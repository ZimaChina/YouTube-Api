from youtube_statistics import YTstats

API_KEY = "AIzaSyCk4SF_hSaZK9U5H0wWflRvIgymFF69pb0" 
channel_id = "UC8ycFlguVIToxRB34x3g1eQ"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_stats()
yt.get_channel_video_data()
yt.dump()

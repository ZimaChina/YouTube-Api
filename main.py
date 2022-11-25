from youtube_statistics import YTstats

API_KEY = "" #there might be a reset
channel_id = "@JazzAcademy"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_stats()

from youtube_statistics import YTstats

API_KEY = "AIzaSyD9ogIvv86eNJWKbweDDnos1YZ1ZkFByW8"
channel_id = "@JazzAcademy"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_stats()
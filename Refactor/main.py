# from root import root_page, launchapp
# from artists import artists_page, launchapp
# from tracks import all_tracks_page, launchapp
# from track_page import track_page, launchapp
from root import root_page
import artists
import tracks
import track_page


def route(environ, start_response):
    if asdfasdfasdfasd:
        artists.artists_page(environ, start_response)
    elif adfasdfasdfasdf:
    else:
        # 404


def launchapp(app):
    with make_server('', 8000, app) as httpd:
        print(
            '\nServing on port 8000...''\nTo finish the application process, press Ctrl+C\n')
        httpd.serve_forever()


def main():
    launchapp(root_page)


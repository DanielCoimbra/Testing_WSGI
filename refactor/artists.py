from wsgiref.simple_server import make_server
from db_utils import db_connect
from werkzeug.wrappers import Request, Response


def artists_table():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('''SELECT artists.Name, albums.Title FROM artists
     LEFT JOIN albums ORDER BY artists.Name''')
    rows = cur.fetchall()
    conn.close()
    html = """
        <table>
            <tr> <th>Artist</th><th>Album</th> </tr>"""
    for row in rows:
        html += "<tr> <td>{}</td> <td>{}</td> </tr>".format(row[0], row[1])
    html += "</table>"
    
    return html
    
@Request.application
def artists_page(request):
    html = """
        <!DOCTYPE HTML>
        <head>
            <title>Music Store</title>
            <!-- CSS only -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
            <!-- JS, Popper.js, and jQuery -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        </head>
        <html>
            <body>        
                <p style="font-size:90px;text-align:center">Music Store</p>
                <br>
                <a href="http://127.0.0.1:8000" class="button" style="color:green;padding:15px 32px;text-align:center;font-size:50px;">Home</a>
                {}
            </body>
        </html>""".format(artists_table())

    
    
    return Response([html], status=200, mimetype='text/html')
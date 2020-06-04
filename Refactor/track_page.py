from db_utils import db_connect
from wsgiref.simple_server import make_server

def track_page_form(TrackId): #GET method
    conn = db_connect()
    cur = conn.cursor()
    sql = "SELECT Name, Composer FROM Tracks WHERE TrackId=?"
    cur.execute(sql, TrackId)
    rows = cur.fetchall()
    for x, y in rows:
        name = x
        composer = y

    html = """
    
    <form method="post" action="">
        <label for="Track">Track:</label>
        <input style="width:80%" "type="text" id="Track" name="Track" value ="{}" required>
        <br>
        <br>
        <label for="Composer">Composer:</label>
        <input style="width:80%" type="text" id="Composer" name="Composer" value ="{}" required>
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>
    
    <a href="http://127.0.0.1:8000" class="button" style="color:red;padding:10px 10px;text-align:center;font-size:35px;">Cancel</a>
    """.format(name, composer)
    return html

def track_form_handler(TrackId, name, comp): #POST method
    conn = db_connect()
    cur = conn.cursor()
    sql = "UPDATE Tracks SET Name = ?, Composer = ? WHERE TrackId = ?"
    try:
        cur.execute(sql, (name, comp, TrackId))
        conn.commit()
    except:
        conn.rollback()
        raise RuntimeError("An error occurred...")

def track_page(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/html')]

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
    start_response(status, response_headers)
    result = html.encode('utf-8')
    return [result]
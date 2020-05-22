#! /usr/bin/python3
from db_utils import db_connect
#All tracks               CHECK
#Artists                  CHECK
#Track_Page

def template(Title, Body, error= False):
    html = '''
        <!DOCTYPE HTML>

        <html>
            <body>        
                <p style="font-size:50px">Music Store</p>
                <pre style="font-size:38px">     {}</pre>
                {}
            </body>
        </html>'''.format(Title, Body)
        
        
    return html.encode('utf-8')

def all_tracks():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT TrackId, Name, Composer, Milliseconds FROM Tracks ORDER BY TrackId')
    rows = cur.fetchall()
    cur.execute("select TrackId from Tracks")
    IDs = cur.fetchall()
    id_num=0
    countLinks=0
    html = """
        <table style="width=100%">
            <tr>
                <th>TrackID</th>
                <th>Name</th>
                <th>Composer</th>
                <th>Milliseconds</th>
            </tr>
            """
    
    
    for row in rows:
        count=0
        html+="""<tr>"""
        # html+="""<a href="127.0.0.1:8000/tracks/{}"><td>{}</td></a>""".format(IDs[i], IDs[i])
        for cell in row: 
            count +=1
            
            html+= "<td>" #Open cell tag
            
            if count==2: #this makes sure only the Name has a bound link
                html +="<a href='127.0.0.1:8000/tracks/{}'>".format(IDs[countLinks]) #Open Link tag
            
            html+=str(cell) # Table Cell Argument
            
            if count==2: #this makes sure only the Name has a bound link

                html +="</a>" #close link tag
            html+="</td>" # Close cell tag
        html+="</tr>"
    html+= "</table>"

    return html

def artists_page():
    
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT artists.Name, albums.Title FROM artists LEFT JOIN albums ORDER BY artists.Name')
    rows = cur.fetchall()
    html="""
        <table>
            <tr> <th>Artist</th><th>Album</th> </tr>"""
    for row in rows:
        html += "<tr> <td>{}</td> <td>{}</td> </tr>".format(row[0], row[1])
    html +="</table>"
    return html    


def track_page(TrackId):
    conn =db_connect()
    cur = conn.cursor()
    cur.execute("SELECT Name, Composer FROM Tracks WHERE TrackId='" + str(TrackId) + "'")
    rows = cur.fetchall()
    for x,y in rows:
        name = x 
        composer = y
    
    html = """
    
    <form action="localhost:8000/{}" method="post">
        <label for="Track">Track:{}</label>
        <input type="text" id="Track" name="Track">
        <br>
        <br>
        <label for="Composer">Composer:{}</label>
        <input type="text" id="Composer" name="Composer">
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>""".format(TrackId, name,composer)
    return html



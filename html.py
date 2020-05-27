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
                <a href="http://127.0.0.1:8000"><p style="font-size:30px">Home</p></a>
                {}
            </body>
        </html>'''.format(Title, Body)
        
        
    return html.encode('utf-8')

def all_tracks():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT TrackId, Name, Composer, Milliseconds/1000 FROM Tracks ORDER BY TrackId')
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
                <th>Seconds</th>
            </tr>
            """
    
    
    for row in rows:
        id_num +=1
        count=0
        html+="""<tr>"""

        for cell in row: 
            count +=1
            
            html+= "<td>" #Open cell tag
            
            if count==2: #this makes sure only the Name has a bound link
                html +="<a href='http://127.0.0.1:8000/tracks/{}'>".format(id_num) #Open Link tag
            
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
    
    <form method="post" action="">
        <label for="Track">Track:{}</label>
        <input type="text" id="Track" name="Track">
        <br>
        <br>
        <label for="Composer">Composer:{}</label>
        <input type="text" id="Composer" name="Composer">
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>""".format(name,composer)
    return html

def track_form_handler(TrackId, name, comp):
    conn =db_connect()
    cur = conn.cursor()
    sql = "UPDATE Tracks SET Name = ?, Composer = ? WHERE TrackId = ?"
    try:
        cur.execute(sql, (name, comp, TrackId))
        conn.commit()
    except:
        conn.rollback()
        raise RuntimeError("An error occurred...")


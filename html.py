#! /usr/bin/python3
from db_utils import db_connect

def template(path, error= False):
    if error:
        html = '''
        <!DOCTYPE HTML>

        <html>
            <p style="font-size:50px;">ERROR 404</p>
            <pre style="font-size:18px;">        RESOURCE NOT FOUND.</pre>
        </html>
         '''
    else:
        html = '''
        <!DOCTYPE HTML>

        <html>
            <p style="font-size:30px">This is  {}  directory.</p>
        </html>'''.format(path)
        
        
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
    html ="<!DOCTYPE HTML>"
    html += """
    
    <html>
    <body>
        <h1 style="font-size:35px">Tracks List</h1>
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
        html+="<tr>"
        # html+="""<a href="127.0.0.1:8000/tracks/{}"><td>{}</td></a>""".format(IDs[i], IDs[i])
        for x in row: 
            count +=1
            
            html+= "<td>" #Open cell tag
            
            if count==2: #this makes sure only the Name has a bound link
                html +="<a href='127.0.0.1:8000/tracks/{}'>".format(IDs[countLinks]) #Open Link tag
            
            html+=str(x) # Table Cell Argument
            
            if count==2: #this makes sure only the Name has a bound link

                html +="</a>" #close link tag
            html+="</td>" # Close cell tag
        html+="</tr>"

    html += "</table></body></html>"

    return html.encode('utf-8')


def track_page(TrackId):
    conn =db_connect()
    cur = conn.cursor()
    sql = """SELECT Name, Composer FROM Tracks WHERE TrackId='"""
    sql += str(TrackId) + "'"
    cur.execute(sql)
    All_IDs = cur.fetchall()

    html = """
    <!DOCTYPE html>
    <html>
        <body>
            <form action=\"localhost:8000\" method=\"post\">
        </body>
    </html>
    """
    return html.encode('utf-8')


def artists_page():
    
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT TrackId, Name, Composer, Milliseconds FROM Tracks ORDER BY TrackId')
    rows = cur.fetchall()
    html="<!DOCTYPE html>"
    html+="""


    """
    return html.encode('utf-8')
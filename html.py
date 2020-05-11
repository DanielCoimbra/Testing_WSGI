#! /usr/bin/python3
def index(path):
    html1 = '''
    <!DOCTYPE HTML>

    <html>
        <h1>This is  {}  directory.</h1>
    </html>'''.format(path)
    
    return html1.encode('utf-8')

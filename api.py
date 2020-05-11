from flask import Flask, jsonify, request
import json, yaml # data (de)serializers
import pymysql    # database frameworks

# read config from config.yml file and save in conf variable
with open('config.yml') as confile:
    try:
        conf = yaml.safe_load(confile)
    except yaml.YAMLError as exception:
        print("Something went wrong, couldn't parse config.yml")

# name of this variable is used on every api method (e.g. app.route)
# and must be defined for WSGI server to use
app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
# name of next function means nothing, because it will be invoked by
# first argument of app.route() method
def home():
    """
    home page that binded to root address (primary FQDN w/o any path after it)
    """
    return """<h1>Sample api engine</h1>
            <p>This is a home page of sample API engine. API methods:<br>
            <ul>
            <li><i>/samplelist</i> - return sample list in JSON format</li>
            <li><i>/books/all</i> - return full sample list of books in JSON format</li>
            <li><i>/books?id={int}</i> - return book from sample list by id in JSON format</li>
            <li><i>/mysql/offices/all</i> - return full mysql table "offices"</li>
            </ul>
            and some more methods on the way.
            </p>
            <p>Thanks for visiting</p>
            <footer><p>Created by Trofogol for education purposes. No contacts provided.</p></footer>"""

@app.errorhandler(404)
def not_found(exc):
    return '<h1>Not found (404)</h1><h3>There is no such address or method, check URL and try again</h3>' + '<p>exc == "' + str(exc) + '"</p>'

@app.route('/samplelist', methods=['GET'])
def list():
    """
    return sample list from external json file
    """
    with open('data.json') as jfile:
        result = json.load(jfile)
    
    return jsonify(result)

@app.route('/books/all', methods=['GET'])
def books():
    """
    load sample list from raw.py
    """
    import raw
    return jsonify(raw.get_books())

@app.route('/books', methods=['GET'])
def get_book():
    """
    return filtered results or text about id abscence
    """
    # Check if an ID was provided as part of the URL.
    if 'id' in request.args:
        # If ID is provided, assign it to a variable.
        id = int(request.args['id'])
    else:
        # If no ID is provided, display an error in the browser.
        return "Request error: no id field provided"

    # prepare results variable (empty list)
    results = []

    import raw
    for book in raw.get_books():
        if book['id'] == id:
            results.append(book)

    # return data in json format
    return jsonify(results)

# finally, work with real database
@app.route('/mysql/offices/all', methods=['GET'])
def offices():
    """
    return all entries from books [TODO: in html table format]
    or in json format (must be requested explicitly)
    """
    # shorten mysql config var name
    mysql = conf['databases']['mysql']
    
    # connect to database
    with pymysql.connect(mysql['address'],mysql['login'],mysql['password'],mysql['database'],mysql['port']) as db:
        # here happened some magic (probably __start__ method includes connector creation)
        # so db eventually became cursor, not connector
        # execute query
        db.execute('SELECT * FROM offices')    # hardcoded (don't do that)
        
        # save raw data for return
        result = db.fetchall()

    # now check query arguments (look for "format")
    if 'format' in request.args:
        if request.args['format'] == 'json':
            # return whole table in json format
            return jsonify(result)
        
        # probably not the best implementation, but it's pretty short for current version
        else:
            # return error about format parameter
            return 'Sorry, only html (no query args) or json formats available (not "' + request.args['format'] + '"'
    else:
        # default format is html, so let's form a table
        pretty_result = '<style>table, th, td {border: 1px solid black;}</style><table>'
        for row in result:
            # form table row
            pretty_result += '<tr>'
            for column in row:
                # form table column (cell)
                pretty_result += '<td>' + str(column) + '</td>'
            # close row tag
            pretty_result += '</tr>'
        # close table tag
        pretty_result += '</table>'
        return pretty_result

# run api
#app.run()                  # localhost visible
app.run(host='0.0.0.0', port=conf['api']['port'])    # externally visible "single request" mode

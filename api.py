from flask import Flask, jsonify, request
import json, yaml # data (de)serializers
import pymysql    # database frameworks

# read config from config.yml file and save in conf variable
with open('config.yml') as confile:
    try:
        conf = yaml.safe_load(confile)
    except yaml.YAMLError as exception:
        print(f"Something went wrong, couldn't parse config.yml correctly: {exception}")

app = Flask(__name__)
#app.config["DEBUG"] = True

def exec_mysql(query):
    """
    execute query on mysql database which is defined in config.yml
    """
    # shorten mysql config variable name for better readability
    mysql = conf['databases']['mysql']

    # connect to database
    with pymysql.connect(mysql['address'],mysql['login'],mysql['password'],mysql['database'],mysql['port']) as db:
        # here happened some magic
        # looks like  __start__ method includes connector creation
        # so db eventually became cursor, not connector
        db.execute(query) # execute query
        result = db.fetchall() # save data for return

    # I placed return statement out of "with" to make sure that all clean-up
    # jobs is completed
    return result

@app.route('/', methods=['GET'])
# name of next function means nothing, because it will be invoked by
# first argument of app.route() method
def home():
    """
    home page that binded to root address (primary FQDN w/o any path after it)
    """
    # NB! keep data below actual
    #TODO: move it to external file
    return """<h1>Sample api engine</h1>
            <p>This is a home page of sample API engine. API methods:<br>
            <ul>
            <li><i>/samplelist</i> - return sample list in JSON format</li>
            <li><i>/books/all</i> - return full sample list of books in JSON format</li>
            <li><i>/books?id={int}</i> - return book from sample list by id in JSON format</li>
            <li><i>/mysql/offices/all</i> - return full mysql table "offices"</li>
            <li><i>/mysql/offices?name={string}</i> - get office by specified name</li>
            </ul>
            and some more methods on the way.
            </p>
            <p>______________________________________</p>
            <p>* - there are data types in braces. To form correct request, just put required data there (also remove braces).</p>
            <footer style="border-top: double;">
            <p>Created by Trofogol for education purposes. GitHub: <a href=https://github.com/Trofogol>Trofogol</a></p>
            </footer>"""

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
def all_offices():
    """
    return all entries from books
    or in json format (must be requested explicitly)
    """
    
    # save result of query 'SELECT * from offices' to result var
    result = exec_mysql('SELECT * from offices')

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
        # close table tag and add info about JSON format
        pretty_result += '</table><p>You can get this result in JSON format. Just specify format=json as query parameter (add it after ? in address string)</p>'
        return pretty_result

@app.route('/mysql/offices', methods=['GET'])
def office():
    """
    return specified row (defined by name) from offices table
    """
    if 'name' in request.args:
        result = exec_mysql('SELECT * from offices WHERE name = "' + request.args['name'] + '";')
        return jsonify(result)
    else:
        return '<p>Sorry, I need to know name of office. Please specify it by adding "?name=office_name" (w/o quotes) at the end of URL</p>'

# run api
app.run(host='0.0.0.0', port=conf['api']['port'])    # externally visible (if debug mode is disabled)

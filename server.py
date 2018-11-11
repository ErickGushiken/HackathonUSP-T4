from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

@app.route("/api/pius", methods=['GET'])
def get_all_projects():
    #função que retorna a lista de projetos
    with open('projects_database.txt', 'r') as project_database:
        project_list = project_database.read()
    return json.dumps(project_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, threaded=True, debug=True, use_reloader=True)
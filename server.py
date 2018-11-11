from flask import Flask
from flask import request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route("/api/pius", methods=['GET'])
def get_all_projects():
    #função que retorna a lista de projetos
    with open('projects_database.txt', 'r') as project_database:
        project_list = project_database.read()
    return json.dumps(project_list)

@app.route("/cadastros", methods=['POST'])
def update_database():
    new_project = request.get_json()
    with open('projects_database.txt', 'r') as project_database:
        project_list = json.loads(project_database.read())
    project_list.append(new_project)
    with open('projects_database.txt', 'w') as project_database:
        project_database.write(json.dumps(project_list))
    return "Project submitted successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, threaded=True, debug=True, use_reloader=True)
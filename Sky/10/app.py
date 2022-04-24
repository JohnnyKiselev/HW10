import json
from flask import Flask

app = Flask(__name__)

candidates = []
with open('candidates.json', 'r', encoding='utf-8') as file:
    fin = file.read()
    fin = json.loads(fin)
    for i in fin:
        candidates.append(i)


@app.route("/")
def page_index():
    result = "<pre>"
    for candidate in candidates:
        result += (
            f"{candidate['name']}\n"
            f"{candidate['position']}\n"
            f"{candidate['skills']}\n\n"
        )
    result += "</pre>"
    return result


@app.route("/candidate/<int:x>")
def candidate_page(x):
    x = x - 1
    result = '<pre>'
    result += (
        f"img scr={candidates[x]['picture']}\n\n"
        f"{candidates[x]['name']}\n"
        f"{candidates[x]['position']}\n"
        f"{candidates[x]['skills']}\n\n"
    )
    result += '</pre>'
    return result


@app.route("/skills/<x>")
def search_skill(x):
    result = '<pre>'
    for candidate in candidates:
        skills = candidate['skills'].lower()
        skills.split(', ')
        if x.lower() in skills:
            result += (
                f"{candidate['name']}\n"
                f"{candidate['position']}\n"
                f"{candidate['skills']}\n\n"
            )
    result += '</pre>'
    return result


app.run()

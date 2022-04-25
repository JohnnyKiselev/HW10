import utils
from flask import Flask

app = Flask(__name__)

candidates = utils.get_candidates()


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


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id):
    return utils.candidate_page(candidate_id)


@app.route("/skills/<skill>")
def search_skill(skill):
    return utils.search_skill(skill)


app.run()

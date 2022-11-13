from flask import Flask, render_template
from utils import get_all, get_by_skills, get_by_pk, get_by_name

if __name__ == '__main__':

    json_file = 'candidates.json'
    app = Flask(__name__)

    @app.route("/")
    def page_index():
        candidates = get_all(json_file)
        return render_template('index.html', candidates = candidates)


    @app.route('/candidates/<int:pk>')
    def page_candidates(pk):
        candidate = get_by_pk(json_file, pk)
        return render_template('card.html', candidate=candidate)


    @app.route('/search/<candidate_name>')
    def page_search(candidate_name):
        candidates = get_by_name(json_file, candidate_name)
        candidates_length = len(candidates)
        return render_template('search.html', candidates=candidates, candidates_length=candidates_length)


    @app.route('/skills/<skill>')
    def page_skills(skill):
        candidates = get_by_skills(json_file, skill)
        candidates_length = len(candidates)
        return render_template('skill.html', candidates=candidates, candidates_length=candidates_length)
        # result = ''
        # for candidate in get_by_skills(json_file, skill):
        #     result += candidate[1] + '<br>'
        #     result += candidate[3] + '<br>'
        #     result += candidate[6] + '<br>'
        #     result += '<br>'
        # return f"<pre>{result}</pre>"


    app.run()

from flask import Flask
from utils import get_all, get_by_skills, get_by_pk

if __name__ == '__main__':

    json_file = 'candidates.json'
    app = Flask(__name__)

    @app.route("/")
    def page_index():
        result = ''
        for candidate in get_all(json_file):
            result += candidate[1] + '<br>'
            result += candidate[3] + '<br>'
            result += candidate[6] + '<br>'
            result += '<br>'
        return f"<pre>{result}</pre>"


    @app.route('/candidates/<int:pk>')
    def page_candidates(pk):
        result = ''
        candidate = get_by_pk(json_file, pk)
        result += candidate[1] + '<br>'
        result += candidate[3] + '<br>'
        result += candidate[6] + '<br>'
        return f"""
        <img src = "{candidate[2]}">
        <pre> {result} </pre>
        """


    @app.route('/skills/<skill>')
    def page_skills(skill):
        result = ''
        for candidate in get_by_skills(json_file, skill):
            result += candidate[1] + '<br>'
            result += candidate[3] + '<br>'
            result += candidate[6] + '<br>'
            result += '<br>'
        return f"<pre>{result}</pre>"


    app.run()

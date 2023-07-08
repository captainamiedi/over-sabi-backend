from flask import Flask, request, jsonify
import os
import QAReport
from dotenv import dotenv_values
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

config = dotenv_values(".env") 
os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEYS']

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/api/eu_election_report_chat/', methods=['POST'])
def eu_election_report_chat():
    try:
        report = QAReport
        question = request.form['question']
        result = report.query_chain(question)
        return jsonify({'data': result})
    except Exception as exc:
        print(exc, 'exception handle')

@app.route('/api/summary/', methods=['GET'])
def eu_election_report_summary():
    try:
        report = QAReport
        # question = request.form['question']
        result = report.summary_of_document()
        return jsonify({'data': result})
    except Exception as exc:
        print(exc, 'exception handle')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
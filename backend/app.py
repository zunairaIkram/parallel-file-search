from flask import Flask
from flask_cors import CORS
from TextFiles import text_files_searching
from ResearchFiles import research_files_searching  
from GeneratePDF import generate_pdf 

app = Flask(__name__)
CORS(app) 

app.add_url_rule('/textFileSearch', view_func=text_files_searching, methods=['POST'])
app.add_url_rule('/researchFileSearch', view_func=research_files_searching, methods=['POST'])
app.add_url_rule('/generate-pdf', view_func=generate_pdf, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)

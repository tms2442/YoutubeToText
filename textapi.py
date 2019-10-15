from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/simpleconvert/*": {"origins": "*"}})
@app.route("/", methods= ['GET', 'POST'])
def helloWorld():
	requ = request.json['title']
	video = requ.split("watch?v=", 1)[1]	
	res = []
	res = YouTubeTranscriptApi.get_transcript(video)
	formatted = []
	for item in res:
		formatted.append(str(int(item['start'])) + " | " + item['text'])
	return jsonify(formatted)
	

if __name__ == '__main__':
	app.run(debug=True)


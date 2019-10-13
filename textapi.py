from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
#api = Api(app)

#class TextConv(Resource):
#	def get(self):
#		return {'hello': 'world'}

CORS(app)
cors = CORS(app, resources={r"/simpleconvert/*": {"origins": "*"}})
@app.route("/", methods= ['GET', 'POST'])
def helloWorld():
	v = 'HRxjvaKu-X4&t=129s'
	requ = request.json['title']
	video = requ.split("watch?v=", 1)[1]	
	res = []
	res = YouTubeTranscriptApi.get_transcript(video)
#	fin = ''
#	for item in res:
#		fin += item['text'] + str(int(item['start'])) + '\n'
#	return fin
	formatted = []
	for item in res:
		formatted.append("Time in seconds: " + str(int(item['start'])) + " | " + item['text'])
	return jsonify(formatted)

#api.add_resource(TextConv, '/')

if __name__ == '__main__':
	app.run(debug=True)


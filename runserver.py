from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import cancer_v2


app = Flask(__name__)

@app.route('/sms',methods = ['POST'])

@app.route('/mms',methods = ['POST'])


def sms_reply():
	resp = MessagingResponse()
	if request.values['NumMedia'] != '0':
		image_url = request.values['MediaUrl0']
		r = cancer_v2.run_ai(image_url)
		print(r)
		print(type(r))
		if r == 1:
			print('in the inner if')
			resp.message('You have a low risk for melanoma')
			return str(resp)
		else:
			print('in the inner else')
			resp.message('You might be at risk. Please consult a professional')
			return str(resp)
	else:
		print('in the outer else')
		resp.message('Please send an image')
	return str(resp)

if __name__ == '__main__':
	app.run()

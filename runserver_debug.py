from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import cancer_v2


app = Flask(__name__)

@app.route('/sms',methods = ['POST'])

@app.route('/mms',methods = ['POST'])



def sms_reply():
	
	auth_sid = "ACc6aef54bbd44a1adf02367b25ce45fbb"
	auth_token = "5bd4ae759ab2bde7e8a7cdfe64209bcb"
	client = Client(auth_sid, auth_token)
	number = request.form['From']
	number = '+1' + number[1:]
	resp = MessagingResponse()
	if request.values['NumMedia'] != '0':
		image_url = request.values['MediaUrl0']
		r = cancer_v2.run_ai(image_url)
		print(r)
		print(type(r))
		if r == 1:
			print('in the inner if')
			message = client.messages.create( to = str(number), from_ = "+18058708120", body = 'You have a low risk for melanoma')
			#resp.message('You have a low risk for melanoma')
			#return str(resp)
		else:
			print('in the inner else')
			message = client.messages.create(to = str(number), from_= "+18058708120", body = "You might be at risk. Please consult a professional")
			#resp.message('You might be at risk. Please consult a professional')
			#return str(resp)
	else:
		print('in the outer else')
		resp.message('Please send an image')
	return str(resp)

if __name__ == '__main__':
	app.run()

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/voice", methods=['GET','POST'])
def voice():
    response = VoiceResponse()

    gather = Gather(num_digits=1, action='/gather')
    gather.say( 'if this was you press 1, if not press,2')
    response.append(gather)
    response.redirect('/voice')
    return str(response)        
        

@app.route("/gather", methods=['GET', 'POST'])
def gather():
    resp = VoiceResponse()
    if 'Digits' in request.values:
        choice = request.values['Digits']

        if choice == '1':
            gather = Gather(num_digits=6)
            gather.say('Thank you, please enter the 6 digit code')
            return str(gather)

        elif choice == '2':
            gather = Gather(num_digits=6)
            gather.say('enter the 6 digit code now')
            response.append(gather)

        else:
            response.say ("Sorry, I dont understand that choice.")




print (str(gather))

if __name__ = "__main__":
    app.run(debug=True)

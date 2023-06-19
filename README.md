# whatsapp-chatgpt-bot
 # install flask
the WebHook URL must be provided for the server to trigger our script for incoming messages. we will deployed the server using the FLASK microframework. The FLASK server allows us to conveniently process incoming requests.

pip install flask

Then clone the repository for yourself.

# install ngrok
for local development purposes, a tunneling service is required.

Create Virtual Evironment.
virtualenv env --python=python3
Activate Virtual Evironment.

source env/bin/activate
Install All Required Libraries.

pip install -r requirements.txt
Then Run Python flask App.

python whatsapp.py

Run ngrok
Run ngrok For Windows :
ngrok http 5000

Run ngrok For Mac :
./ngrok http 5000

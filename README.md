## Python flask starter
This starter app contains a flask web server that serves a simple Miro app. Once installed on a board, the Miro app can open a panel that ddisplays a form with a single text box and a 'Submit' button. When the 'Submit' button is pressed, the content of the text box is sent to the flask web server.

### Installation

Create a virtual environment in your project directory. This will create a .env directory:

```
cd miroapp_flask_starter
python3 -m venv .venv
```

Activate your virtual environment:

```
source .venv/bin/activate
```

After activating the virtual environment, your prompt will have a prefix (.env), like this:

```
(.venv) daniela@MacBook-Pro miroapp_flask_starter %
```

If you are not familiar with python virtual environments, read more here: https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/

Install all the required packages in the virtual environment

```
pip install -r requirements.txt
```

### Run the flask web server locally

```
export FLASK_APP=flask_app.py && export FLASK_ENV=development && flask run
```

It will print in which port the server is running. Usually it is http://127.0.0.1:5000. If so, you can check that it is serving the static pages by going to http://127.0.0.1:5000/static/app.html
You should see a form with a text box and a button. If you press the button, the content of the text box will be sent to the server (flask_app.py).

### Deploying to production

To use flask in production, please refer to https://flask.palletsprojects.com/en/2.3.x/deploying/

### Miro app

This project includes a simple Miro app. If you got the flask web server running, the entry point of your Miro app is the index.html file found at http://127.0.0.1:5000/static/index.html
When configuring your Miro app in your App Settings page in miro.com, paste the url that points to the index.html file in the input box for App URL. 

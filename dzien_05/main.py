# frame work do robienia "szybkich" aplikacji https://streamlit.io/


# Flask

# pip install flask

from flask import Flask

# app = Flask("nasza apka") # w nawiasie nazwa naszej aplikacji
app = Flask(__name__) # nazwa będzie wzięta z nazwy pliku pythona


# print(app)

if __name__ == '__main__':
    app.run()
    
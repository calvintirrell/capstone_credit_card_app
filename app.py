from flask import Flask, send_from_directory, render_template, request, abort
import sklearn
from waitress import serve
from src.models.card_classifier import card_predict
from src.utils import get_features #validate_input

app = Flask(__name__, static_url_path = "/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/get_results", methods = ["POST"])
def get_results():
    """ Predict the approval (or not) of credit card application based on the inputs. """
    data = request.form
    print(data)

    selection = data['selection']
    test_value = get_features(selection)

    prediction = card_predict(test_value)

    if selection == 'James_Bond':
        prediction = """James you have been approved. Congratulations on your new credit card!
        You are approved for a credit card by having a strong credit score, high income and over 5 years of work experience.
        Despite a somewhat high amount of debt your positive attributes offset this."""
        return render_template("approved.html", prediction = prediction)

    elif selection == 'Hermoine_Granger':
        prediction = """Hermoine you have been approved. Congratulations on your new credit card!
        You are approved for a credit card by having a solid credit score and minimal debt.
        A modest income and minimal years of work experience were not enough to deny you credit."""
        return render_template("approved.html", prediction = prediction)

    elif selection == 'Catwoman':
        prediction = """Catwoman, sorry but we are unable to extend you credit at this time.
        Minimal work experience and a low credit score along with a modest income and some debt don't line up for approval."""
        return render_template("denied.html", prediction = prediction) 

    elif selection == 'Maverick':
        prediction = """Maverick, sorry but we are unable to extend you credit at this time.
        Despite over 6 years of work experience and low debt, a low credit score and minimal income are not in your favor."""
        return render_template("denied.html", prediction = prediction) 

if __name__ == "__main__":
    serve(app, host = '0.0.0.0', port = 5000)
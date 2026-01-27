import random
import os

import dotenv
from flask import Flask, render_template, request
from mistralai import Mistral

from calcs import plot_expression

dotenv.load_dotenv()
mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))


def convert_request_to_expression(user_request):
    response = mistral_client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "system",
                "content": "Convert user's request to a Python math expression using variable x. Return ONLY the expression, nothing else. Use math module functions like math.sin Examples: 'sine wave' -> 'math.sin(x)'"
            },
            {
                "role": "user",
                "content": user_request
            }
        ]
    )
    return response.choices[0].message.content.strip()

# Docs and examples for Flask: https://flask.palletsprojects.com/en/stable/
app = Flask(__name__)  # To run, use flask --app webapp run --debug

@app.route("/")  # http://127.0.0.1:5000/
def main_page():
    plot_file = ''
    user_input = ''  # TODO: real input

    if user_input.strip() != '':
        rnd_suffix = ''  # some random suffix to caching in browser
        plot_file = f"plot_{rnd_suffix}.png"
        plot_expression(user_input, 0, 4, f"static/{plot_file}")

    return render_template('plot_func.html')  # Add parameters for the template

@app.route("/test")  # http://127.0.0.1:5000/test
def test_route():
    x = random.randint(0, 10)

    return render_template('main_page.html', lucky_num=x)

@app.route("/plot_graph_api")
def plot_graph_api():
    user_request = request.args.get('func_expr', '')

    func_expr = convert_request_to_expression(user_request)

    rnd_suffix = random.randint(0, 1000000)

    plot_file = f"plot_{rnd_suffix}.png"
    plot_expression(func_expr, 0, 4, f"static/{plot_file}")

    res = {
        'plot_image_url': f'static/{plot_file}',
        'expression': func_expr
    }
    return res


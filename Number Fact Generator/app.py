from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def get_response():
    response = None
    number = None
    message = None
    try:
        if request.method == 'POST':
            number = request.form.get('response')
            number = int(number)  # May raise ValueError
            url = f"http://numbersapi.com/{number}"
            res = requests.get(url)
            if res.status_code == 200:
                response = res.text
                message = response
            else:
                message = "Error: Unable to retrieve data."
    except ValueError:
        message = "Invalid number format. Please enter a valid number."
    except requests.RequestException:
        message = "An error occurred while fetching the data."
    except Exception as e:
        message = "An unexpected error occurred."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

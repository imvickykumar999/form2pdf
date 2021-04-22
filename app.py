# Note we imported request!
from flask import Flask, render_template, request
import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def report():

    first_name = None
    last_name = None

    print(first_name, last_name)

    return render_template('form.html',
                            first_name = first_name,
                            last_name = last_name
                           )


@app.route('/converted_report', methods=['POST', 'GET'])
def converted_report():

    first_name = request.form['first_name']
    last_name = request.form['last_name']

    print(first_name, last_name)
    text = f'''
    Special Pathogens Laboratory, {first_name} {last_name} is committed to protecting and
    respecting your privacy. We only use your personal information
    to administrate your account and to provide products and services
    you requested from us. From time to time, we would like to
    contact you about additional products and services, as well as
    other content that may be of interest to you. If you consent to
    us contacting you for this purposes, please check the box:
    '''

    with open("myfile.txt", "w") as f:
        f.write(text)

    from vicks import text2pdf as pdf
    pdf.convert()

    return render_template('form.html',
                            first_name = first_name,
                            last_name = last_name
                           )

if __name__ == '__main__':
    app.run(debug=True)

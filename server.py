from flask import Flask, render_template, url_for, request, redirect
import csv
from utils import movies, lookup_movieId, print_movie_titles
from recommender import recommend_most_popular, recommend_random
import requests


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name,):
    return render_template(page_name, movies=movies['title'].tolist())


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject}, {message}")


@app.route('/recommendations')
def recommendations():
    # read user input from url
    print(request.args)

    titles = request.args.getlist("title")
    ratings = request.args.getlist("rating")

    print(titles, ratings)

    user_rating = dict(zip(titles, ratings))

    print(user_rating)

    recs = recommend_random(movies, user_rating, k=3)
    return render_template('recommendations.html', recs=recs)


def write_to_csv(data):
    with open("database.csv", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        requests.post('https://api.telegram.org/bot5130190712:AAHiIwiIWCflDgFnK-R8Ir7HBncQPlG1NUo/sendMessage',
                      data={'chat_id': '@outout_server', 'text': 'EYYY leo you got a message from:' })
        requests.post('https://api.telegram.org/bot5130190712:AAHiIwiIWCflDgFnK-R8Ir7HBncQPlG1NUo/sendMessage',
                      data={'chat_id': '@outout_server', 'text': data['email'] })
        requests.post('https://api.telegram.org/bot5130190712:AAHiIwiIWCflDgFnK-R8Ir7HBncQPlG1NUo/sendMessage',
                      data={'chat_id': '@outout_server', 'text': data['subject'] })
        requests.post('https://api.telegram.org/bot5130190712:AAHiIwiIWCflDgFnK-R8Ir7HBncQPlG1NUo/sendMessage',
                      data={'chat_id': '@outout_server', 'text': data['message'] })
    
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong"

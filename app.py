
# - request library used to send HTTPS requests
# - jsonify used to return results in JSON format
from flask import Flask, render_template, jsonify, request, redirect, url_for

#import flask_cors to enable cross-origin requests for our API
# - CORS = "cross-origin resource sharing"
# https://aws.amazon.com/what-is/cross-origin-resource-sharing/#:~:text=In%20browser%20terminology%2C%20the%20current,origin's%20protocol%2C%20host%2C%20and%20port
#from flask_cors import CORS
#Reference: https://towardsdatascience.com/build-a-movie-recommendation-api-using-scikit-learn-flask-and-heroku-bee239dc96e3

#import the movie recommendation code
import recommendation


#instantiate the application
app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
     return render_template("index.html")

#- tells flask what URL should trigger the recommend_movies function
# -in this case, the URL is just the base
@app.route('/recs', methods=['POST', 'GET'])
def recommend_movies():
    #if the user submits the form (i.e. a POST request is made),
     #   then redirect to /recommend endpoint
    if request.method=="POST":
        # getting input with name = movie in HTML form
        query_movie = request.form.get('movie')
         
        # search for movie title, then get the movie_id
         
        search_result = recommendation.search(query_movie)
        #get the movie_id of the top search result
        movie_id = search_result.iloc[0]["movieId"]

        recs = recommendation.find_similar_movies(int(movie_id))

        return render_template("recs.html", recs_data = recs.to_dict('index'), query_movie_title=search_result.iloc[0]['title'])
        #jsonify(recs.to_dict(orient='index'))

    elif request.method=="GET":
        #returns a list of dictionaries. each dictionary is 1 row (i.e. 1 movie) in the recs dataframe
        # - the key is the movie's index in the movies dataframe
        return render_template("index.html")


#if we call this app from the cmdline (as "python app.py"), 
#   run the app in debug mode
if __name__ == '__main__':
    #When it runs, this application binds to all IPs on the system (“0.0.0.0”) 
    # and listens on port 5000, which is the default Flask port.
    app.run(debug=True, host='0.0.0.0', port=5000)
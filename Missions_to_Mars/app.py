# import dependencies
from flask import Flask, render_template, redirect

# import pymongo library
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# create home route and define home function
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_info = conn.db.mars_collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_info)

# create scrape route 
@app.route("/scrape")
def scrape():
    # run the scrape function
    mars_data = scrape_mars.scrape()

    # insert the mars data in to the collection
    conn.db.mars_collection.update({}, mars_data, upsert=True)

    # go back to the home page
    return redirect("/")

# run the app
if __name__ == "__main__":
    app.run(debug=True)
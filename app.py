from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
destinations = []
@app.route("/")
@app.route("/home")
def home():
    return render_template('bucketlist.html', places=destinations)

@app.route("/destinations/<int:dest_id>", methods=["GET"])
def get_dests_by_id(dest_id):
    for each_dest in destinations:
        if each_dest['id'] == dest_id:
            return render_template('view_destination.html', this_place=each_dest)
    return render_template('error.html')

@app.route("/new_destination", methods=["GET", "POST"])
def new_destination():
    if request.method =="POST":
        dest_name = request.form.get('dest_name')
        destination = {
            "id": len(destinations) + 1,
            "name": dest_name,
            "photo": dest_name + ".jpg"
        }
        destinations.append(destination)

        return f'<h1>Your form was submitted to add {dest_name}. <a href="/home">Continue</a></h1>'
    return render_template('new_dest.html')

@app.route("/destinations/delete/<int:dest_id>", methods=["POST"])
def del_dest_by_id(dest_id):
    print("deleting dest_id")
    for each_dest in destinations:
        if each_dest['id'] == dest_id:
            destinations.remove(each_dest)
            return f'<h1>Destination was removed. <a href="/home">Continue</a></h1>'
    return render_template('error.html')
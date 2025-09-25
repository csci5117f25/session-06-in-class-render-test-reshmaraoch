from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

guest_list = []


@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        if name and message:
            guest_list.append({"name": name, "message": message})

        
        return redirect(url_for("index"))

    return render_template("hello.html", guest_list=guest_list)

# @app.route("/<name>")
# def hello(name):
#     return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

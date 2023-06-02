import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from photo_restorer import predict_image
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services.html")
def services():
    return render_template("services.html")

@app.route("/comingsoon.html")
def comingsoon():
    return render_template("comingsoon.html")

@app.route("/contacts.html")
def contacts():
    return render_template("contacts.html")

# @app.route('/contacts.html', methods=['POST'])
# def send_mail():
#     if request.method == 'POST':
#         return 1

@app.route('/', methods=['POST'])
def send_email():
    print(request.method)
    if request.method == "POST":
        print(request.files)
    

@app.route("/enhance_img.html")
def enhance_img():
    return render_template("enhance_img.html")

@app.route("/team.html")
def team():
    return render_template("team.html")

@app.route("/text2image.html")
def text2image():
    return render_template("text2image.html")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/enhance_img.html', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        os.makedirs("static/images/", exist_ok=True)
        os.makedirs("static/restored/", exist_ok=True)

        if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_filename = "." + url_for("static", filename = "images/" + filename)
            print(full_filename)
            file.save(full_filename)

            predicted_url = predict_image(filename)
            return render_template("enhance_img.html", filename = filename, restored_url = predicted_url)

if __name__ == "__main__":
    app.run(debug = True)
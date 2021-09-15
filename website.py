from PIL import Image
from datetime import datetime
from pathlib import Path
from flask import Flask, request, render_template
from tkinter import Tk, mainloop
from tkinter import filedialog
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model


app = Flask(__name__ )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_img"]

        img = Image.open(file.stream)

        upload_img_path = "uploaded/" + \
                          datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(upload_img_path)

        return render_template("index.html", query_path=upload_img_path)

    else:
        return render_template("index.html")

app.run()
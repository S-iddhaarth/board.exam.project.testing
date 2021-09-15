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

root = Tk()


class FeatureExtractor:
    def __init__(self):
        base_model = VGG16(weights="imagenet")
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer("fc1").output)

        pass

    def extract(self, img):
        img = img.resize((224, 224)).convert("RGB")
        x = image.img_to_array(img)  # to np.array
        x = np.expand_dims(x, axis=0)
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)


fe = FeatureExtractor()
img_path = filedialog.askopenfilename()
opened = Image.open(img_path)
feature = fe.extract(opened)
print(type(feature), feature.shape)
np.save("feature_path", feature)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_img"]

        img = Image.open(file.stream)

        upload_img_path = "uploaded/" + \
                          datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(upload_img_path)
        query = fe.extract(img)
        dists = np.linalg.norm(feature - query,axis=1)
        ids = np.argsort(dists)[:30]
        scores = [(dists[id], img_path[id]) for id in ids]

        print(scores)

        return render_template("index.html", query_path=upload_img_path,scores = scores)

    else:
        return render_template("index.html")

app.run()

root.mainloop()

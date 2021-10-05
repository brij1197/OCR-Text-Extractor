from flask import Flask, request
from flask.json import jsonify
from ocr import OCR

app = Flask(__name__)


@app.route("/search/text", methods=["GET", "POST"])
def search():
    """ 
    The function takes receives a request with parameters that consist of the file name and coordinates of x0,y0,x2,y2.
    The coordinates are then used to find the set of spanned words in the particular range.
    """
    content = request.json
    filename = content["file_name"]

    obj = OCR(filename=filename)
    [x0, y0, x2, y2] = content["position"]
    text = obj.spanWords(x0=x0, y0=y0, x2=x2, y2=y2)

    return jsonify({"text": text})


@app.errorhandler(Exception)
def exceptError(error):
    return jsonify({"message": str(error)})


if __name__ == "__main__":
    app.run(debug=True)

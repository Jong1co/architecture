from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zzspc1v.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/architecture", methods=["POST"])
def picture_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    tag_receive = request.form['tag_give']

    doc = {
        'url': url_receive,
        'name': name_receive,
        'tag': tag_receive,
    }
    db.picture.insert_one(doc)
    return jsonify({'msg':'저장 완료 !'})

@app.route("/architecture", methods=["GET"])
def picture_get():
    picture_list = list(db.picture.find({}, {'_id': False}))
    return jsonify({'pictures':picture_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
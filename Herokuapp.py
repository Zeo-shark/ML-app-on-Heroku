from flask import Flask
from flask.json import jsonify,request#import object from Flask model
app= Flask(__name__)#define app using flask
languages=[{'name':'Javascript'},{'name':'Python'},{'name':'Ruby'}]
@app.route('/',methods=['GET'])
def returnAll():
    return jsonify({'languages':languages})
@app.route('lang/<string:name>',methods=['GET'])
def returnOne(name):
    langs=[language for language in languages if language['name'] == name]
    return jsonify({'language':langs[0]})

if __name__=='__main__':
    app.run(debug=True,port=8080)
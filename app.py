# import a library

from flask import Flask , render_template,request
import joblib

# instance of an app
app = Flask(__name__)

# load the model
model = joblib.load('diabetic_79.pkl')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data' , methods = ['POST'])
def data():

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    # print(preg)
    # print(plas)
    # print(pres)
    # print(skin)
    # print(test)
    # print(mass)
    # print(pedi)
    # print(age)

    output = model.predict([[preg , plas , pres , skin , test , mass , pedi , age]])

    if output[0] == 1:
        result = 'person is diabetic'
    else:
        result = 'person is not diabetic'
    
    return render_template('result.html' , predict = result)

    
if __name__ == '__main__':
    app.run(debug = True)
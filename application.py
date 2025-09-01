from flask import Flask,render_template,request
from pipeline.prediction_pipeline import hybrid_recommendation
from src.custom_exception import CustomExeption

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def home():

    recomandations = None

    if request.method == 'POST':
        try:
            user_id = int(request.form["UserID"])

            recomandations = hybrid_recommendation(user_id) 
        except Exception as e:
            raise CustomExeption("Error occured",e)
    return render_template('index.html',recomandations = recomandations)

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
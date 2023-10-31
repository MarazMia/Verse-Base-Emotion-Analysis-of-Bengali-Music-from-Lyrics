#import libraries
import numpy as np
from flask import Flask, render_template,request
import joblib
#Initialize the flask App
app = Flask(__name__)
model1 = joblib.load('ML_Models/sgd2class_model.pickle')
model2 = joblib.load('ML_Models/sgd3class_model.pickle')
# ans = model.predict(["I love you"])[0]
# print(ans)
#for detecting verses
def Verse_from_Bengali_Song(song: str)-> list:
    all_verse = []
    all_verse = song.split('\r\n\r\n')
    if len(all_verse)==1:
        all_verse = song.split('॥\r\n')
    if len(all_verse)==1:
        all_verse = song.split('।।\r\n')
    for i in range(len(all_verse)):
        all_verse[i] = " ".join(all_verse[i].split('\r\n')).strip()
    return all_verse


#To use the predict button in our web-app
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = request.form.get('song_input')
    # print(int_features.split('।।\r\n'))
    # print(Verse_from_Bengali_Song(int_features))
    # print(len(Verse_from_Bengali_Song(int_features)))

    verses = Verse_from_Bengali_Song(int_features)
    original_verses = ''
    for i in range(len(verses)):
        original_verses += "Verse "+str(i+1)+" "+verses[i]+'\n\n\n'
    # print(verses)

    output = ""
    for i in range(len(verses)):  
        prediction1 = model1.predict([verses[i]])
        if prediction1==1:
            output += "verse " + str(i+1) + ': ' + verses[i] + "\nemotion : " + "Positively "
        else:
            output += "verse " + str(i+1) + ': ' + verses[i] + "\nemotion : " + "Negatively "

        prediction2 = model2.predict([verses[i]])
        if prediction2==1:
            output += "Love.\n\n"
        elif prediction2==2:
            output += "Sad.\n\n"
        else:
            output += "Life Oriented.\n\n"  

    return render_template('index.html', prediction_text='{}'.format(output), original_text=int_features)


if __name__ == "__main__":
    app.run(debug=True)
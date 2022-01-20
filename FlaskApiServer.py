from flask import Flask, render_template
from flask_restful import Api, Resource
import pandas as pd
import json



sheet_id = '18Teb8AnWLYUPPILsnUY0OIEyOUp2niFJDnnoKDQOe1Y'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
#df = df.to_json()
#print(df)
records = df.to_dict(orient='records')
#print(records)


 
app = Flask(__name__)
#initialize API object for the Flask Application
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

#Api requests
class All(Resource):
    
    def get(self):
        data = json.dumps(records)
        python_obj = json.loads(data)
        #print(python_obj[0]['Score'])
        result = []
        for field in python_obj:
            level = "Beginner"
            if int(field['Score'].split('/')[0]) > 7:
                level = 'Intermediate'
            else:
                level = 'Beginner'
            result.append({"Level":level, "Email": field['Email Address'], "Module": field['Module/Course']})
        return result

#Register Api resources
api.add_resource(All,'/api/')

if __name__ == "__main__":
    app.run(host= '127.0.0.1', port= 5001, debug= True)
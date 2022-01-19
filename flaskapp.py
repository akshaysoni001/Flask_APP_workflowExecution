from flask import *
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)  
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)

class WorkflowStepExecution(db.Model):
    __tablename__ = 'workflow_step_execution'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    workflow_execution_id = db.Column(db.Integer)
    workflow_step_id = db.Column(db.Integer)
    status = db.Column(db.String(32), default="In Queue")
    
    # To maintain account creation and update time
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, workflow_execution_id, workflow_step_id):
        self.workflow_execution_id = workflow_execution_id
        self.workflow_step_id = workflow_step_id


# TO add Sample Data
@app.route("/add",methods=["GET","POST"])
def add_data():
      for i in range(2,20):
            row=WorkflowStepExecution(i,i+5)
            db.session.add(row) 
            db.session.commit()     
      db.session.add(row)
      db.session.commit()
      return render_template("mainpage.html")

#Initial Page
@app.route('/')  
def message():  
      return render_template("mainpage.html",current_time=datetime.utcnow())


@app.route('/request',methods=["GET","POST"])
def requests():
      workflowid = request.args.get("Workflowid")
      row=WorkflowStepExecution.query.filter_by(workflow_execution_id = workflowid).all()
      return render_template("mainpage.html",rows = row,current_time=str(datetime.utcnow()))
      
      
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

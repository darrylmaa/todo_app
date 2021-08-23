from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import DateTime

todo_app = Flask(__name__)
todo_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
todo_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(todo_app)

# def no_micro():
# 	mic_date = datetime.datetime.now
# 	nomic_date = mic_date.strftime("%Y-%m-%d %H:%M:%S")
# 	return nomic_date

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key= True)
	title = db.Column(db.String(100))
	status = db.Column(db.String)
	description = db.Column(db.String(1000))
	created_date = db.Column(DateTime, default=datetime.datetime.now)


	

@todo_app.route('/')
def index():
	#show all todos
	todo_list = Todo.query.all()
	print(todo_list)
	return render_template("base.html", todo_list=todo_list)

@todo_app.route("/add", methods=["POST"])
def add():
	#add new todo
	title = request.form.get("title")
	description = request.form.get("description")
	if description == "":
		description = "N/A"
	new_todo = Todo(title = title, status = "not_complete", description=description)
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for("index"))

@todo_app.route("/not_comp/<int:todo_id>")
def not_comp(todo_id):
	#udpate
	todo = Todo.query.filter_by(id=todo_id).first()
	todo.status = "not_complete"
	db.session.commit()
	return redirect(url_for("index"))

@todo_app.route("/comp/<int:todo_id>")
def comp(todo_id):
	#udpate
	todo = Todo.query.filter_by(id=todo_id).first()
	todo.status = "complete"
	db.session.commit()
	return redirect(url_for("index"))

@todo_app.route("/in_prog/<int:todo_id>")
def in_prog(todo_id):
	#udpate
	todo = Todo.query.filter_by(id=todo_id).first()
	todo.status = "in_progress"
	db.session.commit()
	return redirect(url_for("index"))

@todo_app.route("/delete/<int:todo_id>")
def delete(todo_id):
	#delete
	todo = Todo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for("index"))

@todo_app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
	searchbox = request.form.get("text")
	cursor

# @todo_app.route('/about')
# def about():
# 	return "Hello About"

if __name__ == "__main__":
	db.create_all()

	# new_todo = Todo(title="todo 1", status=False)
	# db.session.add(new_todo)
	# db.session.commit()

	todo_app.run(debug=True)
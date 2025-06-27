from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "aelpsnebcy56y33"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        date = request.form.get('date')
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')  # Format date
        occupation = request.form.get('occupation')
        # Process the data as needed

        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date,
            occupation=occupation
        )
        db.session.add(form)
        db.session.commit()
        flash('Form submitted successfully!', 'success')
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)

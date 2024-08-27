# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.name}>'
    
# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg', methods=['POST'])
def regee():
    name=request.form['email']
    feedback_text=request.form['text']
    new_feedback = Feedback(name=name, feedback_text=feedback_text)
        
    # Agregar a la base de datos
    db.session.add(new_feedback)
    db.session.commit()
    return render_template('index.html')

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)

from flask_blog.models.entries import Entry
from flask_blog import db
from datetime import datetime

class Entry(db.Model):
  __tablename__ = 'entries'
  id = db.Column(db.Integar, primary_key=True)
  title = db.Column(db.String(50), unique=True)
  text = db.Column(db.Text)
  created_at = db.Column(db.DateTime)

  def __init__(self, title=None, text=None):
    self.title = title
    self.text = text
    self.created_at = datetime.utcnow()

  def __repr__(self):
    return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)

@app.route('/entries/new', methods=['GET'])
def new_entry():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('entries/new.html')

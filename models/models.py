# from .database import db
from config.settings import db

class GigiCmsLogin(db.Model):
  __tablename__ = 'GIGICMSLOGIN'  # Table name in the database
  GL_RECID = db.Column(db.Integer, primary_key=True)
  GL_USERNAME = db.Column(db.String(100), nullable=False)
  GL_PASSWORD = db.Column(db.String(100), nullable=False)
  GL_ROLE = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"GIGICMSLOGIN('{self.GL_RECID}', '{self.GL_USERNAME}', '{self.GL_PASSWORD}')"
# GL_USERNAME	varchar
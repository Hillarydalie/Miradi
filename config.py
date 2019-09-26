class Config:
  
    DEBUG="True"
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOAD_PHOTOS_DEST = 'app/static/images'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hillarydalie:password@localhost:5432/miradi'


class DevConfig(Config):
    Debug = True

class ProdConfig(Config):

    Debug=True
configurations = {"development":DevConfig, "production":ProdConfig}

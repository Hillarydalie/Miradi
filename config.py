class Config:

    DEBUG="True"
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/images'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://keren:kayren@localhost:5432/miradi'


class DevConfig(Config):
    Debug = True

class ProdConfig(Config):

    Debug=True
configurations = {"development":DevConfig, "production":ProdConfig}

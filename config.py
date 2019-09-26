class Config:
  
    DEBUG="True"
    MAP_API_KEY = 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
    MAP_BASE_URL = 'https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings'
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOAD_PHOTOS_DEST = 'app/static/images'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hillarydalie:password@localhost:5432/miradi'



class DevConfig(Config):
    Debug = True

class ProdConfig(Config):

    Debug=True
configurations = {"development":DevConfig, "production":ProdConfig}

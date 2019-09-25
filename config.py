class Config:

    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    DEBUG="True"
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hillarydalie:password@localhost:5432/miradi'


class DevConfig(Config):
    Debug = True

class ProdConfig(Config):

    Debug=True
configurations = {"development":DevConfig, "production":ProdConfig}

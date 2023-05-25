SECRET_KEY = "inakyuiblog"

# Database.
HOSTNAME = "127.0.0.1"
PORT     = "3306"
DATABASE = "blog"
USERNAME = "root"
PASSWORD = "root"
DB_URI   = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# Mail.
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3023667843@qq.com"
MAIL_PASSWORD = "rvifyaoknztcdggc"
MAIL_DEFAULT_SENDER = "3023667843@qq.com"

# Cache.
CACHE_TYPE = "redis"
CACHE_REDIS_HOST = "127.0.0.1"
CACHE_REDIS_PORT = "6379"
CACHE_REDIS_PASSWORD = ""
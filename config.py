class Config:
    SECRET_KEY = 'your-secret-key'  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    SECRET_KEY = 'your-secret-key'  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ahossain3324@gmail.com'  # Replace with your email username
    MAIL_PASSWORD = 'yxdh bvxd hrbo wppn'  # Replace with your email password

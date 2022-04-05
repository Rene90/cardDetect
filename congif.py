import os
from os import environ

class Config(object):
	DEBUG = False
	TESTING = False
	basedir = os.path.abspath(os.path.dirname(__file__))
	SECRET_KEY= 'pirene'
	UPLOADS = "/home/rene/Documentos/DatasCourse/p1/uploads"
	SESSION_COOKIE_SECURE = True
	DEFAULT_THEME = None
class DevelopmentConfig(Config):
	DEBUG = True
	SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
	DEBUG = False
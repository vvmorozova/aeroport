from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
class Flight(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
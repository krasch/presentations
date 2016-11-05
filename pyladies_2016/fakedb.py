"""
fake database that does nothing
"""

class UnknownDatabase(Exception):
	pass


class SQLError(Exception):
	pass


class FakeDatabase:
	def __init__(self, db_name):
		if db_name != "meetups.db":
			raise UnknownDatabase("I only know the meetups.db database")

	def close(self):
		pass

	def query(self, sql):
		if sql != "SELECT * FROM meetups":
			raise SQLError("I only support one query")
		else:
			return ["Pyladies Berlin", "PyData", "PostgreSQL Meetup Group"]

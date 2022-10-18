from application import db

# This drops stored data from the database, then creates the database.
db.drop.all()
db.create.all()
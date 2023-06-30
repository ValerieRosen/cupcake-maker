from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="Vanilla Bean",
    size="Small",
    rating=10,
)

c2 = Cupcake(
    flavor="Salted Caramel",
    size="Large",
    rating=9,
)

db.session.add_all([c1, c2])
db.session.commit()

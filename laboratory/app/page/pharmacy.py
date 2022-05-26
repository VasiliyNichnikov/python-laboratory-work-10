from app import db


class Pharmacy(db.Model):
    __tablename__ = 'pharmacies'

    id = db.Column(db.Integer, primary_key=True)
    pharmacy_name = db.Column(db.String, nullable=True)
    patients_full_name = db.Column(db.String, nullable=True)
    name_of_medicine = db.Column(db.String, nullable=True)
    type_of_medicine = db.Column(db.String, nullable=True)
    price_of_medicine = db.Column(db.Integer, nullable=True)
    county_of_origin = db.Column(db.String, nullable=True)
    date_of_sale = db.Column(db.String, nullable=True)

    def __repr__(self) -> str:
        return f"<Pharmacy {self.pharmacy_name}>"

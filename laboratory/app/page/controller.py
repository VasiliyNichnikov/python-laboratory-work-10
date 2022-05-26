from flask import Blueprint
from .pharmacy import Pharmacy
from .forms import SearchForm
from flask import render_template, url_for, redirect
from app import db

module = Blueprint("entity", __name__)


@module.route("/index", methods=["GET", "POST"])
@module.route('/', methods=["GET", "POST"])
def index() -> str:
    form = SearchForm()
    pharmacies = Pharmacy.query.all()
    if form.validate_on_submit():
        text = f"%{form.search.data}%"
        pharmacies = Pharmacy.query.filter(Pharmacy.pharmacy_name.like(text)).all()
        if len(pharmacies) == 0:
            pharmacies = None
    return render_template("page/page.html", pharmacies=pharmacies, form=form)


@module.route("/remove_blog/<pharmacy_name>", methods=["GET"])
def remove_block(pharmacy_name: str):
    pharmacy = Pharmacy.query.filter(Pharmacy.pharmacy_name == pharmacy_name).first()
    if pharmacy is not None:
        db.session.delete(pharmacy)
        db.session.commit()
    return redirect(url_for(".index"))
from flask import Blueprint, redirect, render_template, request

from repositories import biting_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    return render_template(
        "bitings/index.html", bitings=biting_repository.select_all()
        )

# NEW

# CREATE

# EDIT

# UPDATE

# DELETE

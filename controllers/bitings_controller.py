from flask import Blueprint, redirect, render_template, request

from repositories import biting_repository, human_repository, zombie_repository
from models.biting import Biting

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    return render_template(
        "bitings/index.html", bitings=biting_repository.select_all()
        )

# NEW
@bitings_blueprint.route("/bitings/new", methods=['GET'])
def goto_record_biting():
    return render_template(
        "bitings/new.html",
        humans=human_repository.select_all(),
        zombies=zombie_repository.select_all()
    )

# CREATE
@bitings_blueprint.route("/bitings", methods=['POST'])
def record_biting():
    biting_repository.save(
        Biting(
            human_repository.select(request.form['human_id']),
            zombie_repository.select(request.form['zombie_id'])
        )
    )
    return redirect("/bitings")

# EDIT

# UPDATE

# DELETE

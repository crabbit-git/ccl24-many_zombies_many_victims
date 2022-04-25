from db.run_sql import run_sql

from models.biting import Biting
from repositories import human_repository
from repositories import zombie_repository

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    selection = run_sql(sql, values)
    biting.id = selection[0]['id']
    return biting

def select_all():
    # selection = run_sql("SELECT * FROM bitings")
    # bitings = []
    # for row in selection:
    #     human = human_repository.select(row['human_id'])
    #     zombie = zombie_repository.select(row['zombie_id'])
    #     biting = Biting(human, zombie, row['id'])
    #     bitings.append(biting)
    # return bitings
    # Or, more directly:
    return [Biting(
        human_repository.select(row['human_id']),
        zombie_repository.select(row['zombie_id']),
        row['id']
    ) for row in run_sql("SELECT * FROM bitings")]

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    selection = run_sql(sql, [id])[0]
    if selection is not None:
        return Biting(
            human_repository.select(selection['human_id']),
            zombie_repository.select(selection['zombie_id']),
            selection['id']
        )

def delete_all():
    run_sql("DELETE FROM bitings")

def delete(id):
    run_sql("DELETE FROM bitings WHERE id = %s", [id])

def edit(biting):
    sql = "UPDATE bitings SET (human_id, zombie_id) = (%s, %s) WHERE id = %s"
    values = [biting.human.id, biting.zombie.id, biting.id]
    run_sql(sql, values)

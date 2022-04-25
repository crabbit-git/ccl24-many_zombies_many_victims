# What's this then?

It's a "lab" exercise assigned as part of a software development course. This one was designed to expand on previous exercises practicing full stack development with Python and PostgreSQL by exploring how to structure a many-to-many relationship (rather than just one-to-one or many-to-many like in previous exercises). And yes, this one has to do with zombies biting people, which makes it automatically more interesting to me.

One point of interest (to me, anyway) is that I specifically put focus on upsetting the Python Gods by generally not declaring local variables for everything when I wanted to chain a bunch of things into a somewhat complex function or return statement, partly just as an exercise and partly to try to check/reinforce my understanding of how all this is structured. For example, based on how it was done in the worked examples from previous full stack exercises in the course, this is how one of the functions "should" have been structured:

```
def select_all():
    selection = run_sql("SELECT * FROM bitings")
    bitings = []
    for row in selection:
        human_id = row['human_id']
        human = human_repository.select(human_id)
        zombie_id = row['zombie_id']
        zombie = zombie_repository.select(zombie_id)
        biting_id = row['id']
        biting = Biting(human, zombie, biting_id)
        bitings.append(biting)
    return bitings
```

But, y'know, that's a whole buncha typing, so I did this:

```
def select_all():
    return [Biting(
        human_repository.select(row['human_id']),
        zombie_repository.select(row['zombie_id']),
        row['id']
    ) for row in run_sql("SELECT * FROM bitings")]
```

As usual, the instructions we were set are in `task.md` and the start code is in `startpoint`. I've pretty much done everything except mess with CSS, which is mostly because looking at CSS continues to feel like something for people who have more time than I do and I will be dead before I am ever truly happy with any CSS I may write. This will of course have to change over the next week when we are tasked with working on a complete full stack project, but let me enjoy my freedom while I still can, damn it.

Anyway. Zombies. Woo.

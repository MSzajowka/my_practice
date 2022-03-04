hobbit = {
    "name": "Bilbo Baggins",
    "occupation": "burglar"
}
description = "%(name)s is a %(occupation)s." % hobbit
print(description)

description = "{} is a {}.".format("Gandalf The Grey", "wizard")
print(description)

dead = 'Sauron'
description = f'{dead} is defeated.'
print(description)
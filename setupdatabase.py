from basic import db,Puppy

# CREATES ALL THE TABLES Model --> Db Table
db.create_all()

sam = Puppy('Sammy', 3, 'German Shepherd')
frank = Puppy('Frankie', 4, 'Maltese Poodle')

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)
print(frank.id)
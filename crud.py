from basic import db,Puppy

## CREATE ##
my_puppy = Puppy('Rufus',5, 'Shitzu')
db.session.add(my_puppy)
db.session.commit()

## READ ## 
all_puppies = Puppy.query.all() # list of puppies in the table
print("All puppies (1) : ")
print(all_puppies)

# SELECT BY ID
puppy_one = Puppy.query.get(1)
print("First Puppy")
print(puppy_one.name)

# FILTERS
# PRODUCES SQL CODE!
puppy_frankie = Puppy.query.filter_by(name = "Frankie")
print("All puppies with name Frankie")
print(puppy_frankie.all())
## EXPECTED OUTPUT IS ["Frankie is 3 years old"]

### UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
print("Updating age of first puppy to 10")
print(first_puppy)


## DELETE
# second_pup = Puppy.query.get(2)
# db.session.delete(second_pup)
# db.session.commit()

# pPRINT AL PUPPIES
all_puppies = Puppy.query.all()
print("These are all the puppies in final")
print(all_puppies)
class my_life:


    lan="eng"
    heimat='kurdistan'

    def __init__(self,job,location):
        self.job=job
        self.location=location

    def find_mylocation(self):
        print(self.location)

    def find_myjo(self):
        print(self.job)

    @classmethod
    def lana(cls):
        print(cls.lan)







ukena=my_life("coal creek","crested butte")
edi=my_life("mcgills","crested butte")
zack=my_life("mtn prime","idaho spring")


edi.find_myjo()
my_life.lana()

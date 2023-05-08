from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'Manager')
    def giveRaise(self, percent, bonus=0.1):
        ##self.pay *= (1.0 + percent + bonus)
        Person.giveRaise(self, percent + bonus)
        
if __name__=='__main__':
    bob = Person('Bob Smith', 42, 10000, "software")
    sue = Person('Sue Jones', 45, 20000, 'hardware')
    tom = Manager('Tom Doe', 50, 30000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    tom = Manager('Tom Doe', 50, 30000)
    print(tom.pay)
    
    db = [bob, sue, tom]
    
    for obj in db:
        obj.giveRaise(0.10)
        print(obj.lastName(), '=> ', obj.pay)
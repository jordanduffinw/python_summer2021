# An exercise
# JDW's typing alongside this

class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = [] ## list of Bill objects

  def __str__(self): # Print Method
    return "Senator : %s" % (self.name)

  def vote(self, bill, choice):
    # 1: update the bill object--add the senator's name to the the list of yes/no/abstain
    # 2: update the senator object--add this bill to the bills this senator has voted on
    # 3: print an informative message announcing the vote

    # Step 1
    bill.votes[choice].append(self.name)
    # Step 2
    self.bills_voted_on.append(bill)
    # Step 3
    # return "Senator %s voted %s " % (self.name, choice)
    return "Senator " + self.name + " voted " + choice + " on " + bill.title + "."

class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def __str__(self): # Print Method
    return self.title


  def result(self):
    ## update and return the "passed" variable to indicate True/False if the bill passed
    if len(self.votes["yes"] > len(self.votes["no"])):
      self.passed = True
    else:
      self.passed = False
    return self.passed


## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
print(jack)
print(jane)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print(environment.votes)
print(environment.passed)
print(jack.bills_voted_on[0].passed)

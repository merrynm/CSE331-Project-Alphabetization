"""
Alphabetizer: Takes in a roster list consisting of
first names, last names, and corresponding emails.
Orders the people on the list based on given ordering (by first name
or by last name, and checks if they are ordered.
"""
class Person:
    """
    Represents each person in the roster, including first name, last name and email.
    """
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    def __str__(self):
        return '{0} {1} <{2}>'.format(self.first, self.last, self.email)
    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.first, self.last, self.email)
    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.email == other.email
def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    #make each name lowercase for comparison
    firstname1 = (a.first).lower()
    lastname1 = (a.last).lower()
    firstname2 = (b.first).lower()
    lastname2 = (b.last).lower()
    #if have the same first name
    if firstname1 == firstname2:
        #if also have the same last name
        if lastname1 == lastname2:
            return False #they're the same person
        #if don't share a last name
        if lastname1 != lastname2:
            #iterate through last names
            for i, ch in enumerate(lastname1):
                if ch < lastname2[i]:
                    #are alphabetical
                    return True
                if ch > lastname2[i]:
                    #not alphabetical
                    return False
    #if they don't have the same first name
    if firstname1 != firstname2:
        #iterate through the first names
        for i, ch in enumerate(firstname1):
            if ch < firstname2[i]:
                #are alphabetical
                return True
            if ch > firstname2[i]:
                #not alphabetical
                return False
    return False
def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    #make each name lowercase for comparison
    firstname1 = (a.first).lower()
    lastname1 = (a.last).lower()
    firstname2 = (b.first).lower()
    lastname2 = (b.last).lower()
    #if have the same last name
    if lastname1 == lastname2:
        #if also have the same first name
        if firstname1 == firstname2:
            return False
        #if they don't have the same first name
        if firstname1 != firstname2:
            #iterate through last names
            for i, ch in enumerate(firstname1):
                #are alphabetical
                if ch < firstname2[i]:
                    return True
                #are not alphabetical
                if ch > firstname2[i]:
                    return False
    #if they don't have the same first name
    if lastname1 != lastname2:
        #iterate through first names
        for i, ch in enumerate(lastname1):
            #are alphabetical
            if ch < lastname2[i]:
                return True
            #are not alphabetical
            if ch > lastname2[i]:
                return False
    return False
def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    for i, person in enumerate(roster):
        if i < (len(roster)-1):
            #ignore if same person 2x
            if person == roster[i+1]:
                continue
            #if roster is not alphabetized
            elif not ordering(person, roster[i+1]):
                return False
    #if roster is alphabetized
    return True
def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """
    #the roster is alphabetized using merge sort
    cost = 0
    #only finished when n = 1
    if len(roster) != 1:
        halfway = len(roster)//2
        left = roster[0:halfway] #first half
        right = roster[halfway:len(roster)] #second half
        #go through it again til all lists at len=1
        leftcost = alphabetize(left, ordering)[1]
        rightcost = alphabetize(right, ordering)[1]
        cost += (leftcost + rightcost) #merge costs
        i = 0 #iterator for left
        j = 0 #iterator for right
        k = 0 #iterator for roster
        #sort/merge
        while (len(left) > i and len(right) > j):
            if ordering(left[i], right[j]):
                roster[k] = left[i] #smaller item gets copied
                i += 1
            else: #left list's item is not smaller than right
                if not ordering(right[j], left[i]): #then items are the same
                    roster[k] = left[i] #left item gets copied
                    i += 1
                else:
                    roster[k] = right[j] #right item is smaller, gets copied
                    j += 1
            k += 1
            cost += 1
        #add the rest of left
        while len(left) > i:
            roster[k] = left[i]
            i += 1
            k += 1
        #add the rest of right
        while len(right) > j:
            roster[k] = right[j]
            j += 1
            k += 1
    #return the sorted list and total cost
    return (list(roster), cost)
    
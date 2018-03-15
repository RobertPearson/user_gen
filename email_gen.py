#! /bin python
import random
import json
import requests
import os

def mail(domain):
    email = first()+"."+last()+"@"+domain+"\n"
    return email
def first():
    selected = random.random()*90
    with open("first.txt") as names:
        for line in names:
            name, _,cumm,_ = line.split()
            if float(cumm)>selected:
                return name.title()
    return ""
def last():
    selected = random.random()*90
    with open("last.txt") as names:
        for line in names:
            name, _,cumm,_ = line.split()
            if float(cumm)>selected:
                return name.title()
    return ""
def email_value(domain):
    given = first()
    family = last()
    value = str(random.randbetween(0,1000))
    email = given+''+family+'@'+domain
    return (email,value)

def email_name_value(domain, seperator):
    given = first()
    family = last()
    value = str(int(random.random()*1000))
    email = given+seperator+family+'@'+domain
    return (email.lower(),given,family,value)

def email_number_name_value(domain,seperator):
    given = first()
    family = last()
    value = str(int(random.random()*1000))
    email = given+seperator+family+seperator+value+'@'+domain
    return (email.lower(),given,family,value)

def email_from_name(given,family,domain,seperator):
    email = given+seperator+family+'@'+domain
    return email

def email_from_name_value(given,family,value,domain,seperator):
    email = given+seperator+family+seperator+str(value)+'@'+domain
    return email

def makeUser(seperator):
        given = first()
        family = last()
        value = int(random.random()*1000)
        email = email_from_name(given,family,"gmail.com",seperator)
        userdict = dict()
        userdict["email"] = email.lower()
        userdict["full_name"] = given+' '+family
        userdict["first_name"] = given
        userdict["last_name"] = family
        userdict["attr_value"] = value
        return userdict

def makeUser_numbers(seperator):
        given = first()
        family = last()
        value = int(random.random()*1000)
        email = email_from_name_value(given,family,value,"gmail.com",seperator)
        userdict = dict()
        userdict["email"] = email.lower()
        userdict["full_name"] = given+' '+family
        userdict["first_name"] = given
        userdict["last_name"] = family
        userdict["attr_value"] = value
        return userdict

def main():
    data = []
    lines = []
    #make 100 users, with 50 differnt names and values
    for i in range(50):
        # creates a user
        userDict = makeUser('')
        # create a JSON string
        userJSON = json.dumps(userdict)
        print(userJSON)
        lines.append(userJSON)
        # generate a new email with the value appended to the email, add as a new user
        userdict["email"] = email_from_name_value(userDict["first_name"],userDict["last_name"],userDict["attr_value"],"gmail.com",seperator)
        userJSON = json.dumps(userdict)
        print(userJSON)
        lines.append(userJSON)
    
    # save the users to a JSON lines file
    with open("users.JSONL","w") as record:
        for line in lines:
            record.write(line)
            record.write("\n")
    # done


if __name__ == "__main__":
    main()


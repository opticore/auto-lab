#!/usr/bin/env python

# Variables (Vars)
def Variables():
  x = 1
  y = "donkey"
  z = 1.1

  print type(x)
  print type(z)
  print('\n')
  print x
  print y

def Lists():
  creatures = ["Chicken", "Monkey" , "Demogorg" , "Dog", "Dragon"]

  print type(creatures)
  print creatures
  print ("Length" , len(creatures))
  print('\n')
  print creatures[1]
  print creatures[2]
  print('\n')
  print creatures[2:4]
  return creatures


def Dictionarys():
  creature = {}
  creature['Type'] = 'Demogorg'
  creature['Name'] = ''
  creature['Food'] = 'Nougart'
  creature['Friends'] = ["omid","rich"]

  #print type(creature)
  #print creature['Friends']
  #print creature
  #print('\n')
  #print "Grrrr, I am a", creature['Type'], "Feed me", creature['Food']

  return creature

def if_control():
  creature  = Dictionarys()
  print (creature)

  if creature['Name'] == 'Dart':
    print "I'm", creature['Name'], "how you doin?"
  else:
    print "I have on name :("


def for_control():
    myanimals = Lists()

    for i in myanimals:
        print i

#Variables()
#Lists()
#Dictionarys()
#if_control()
for_control()

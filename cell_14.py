#!/usr/bin/env python
# coding: utf-8

# In[ ]:


upper = 100
lower = 0
guess = 50
counter = 0
running = True
input("Please think of a number between 0 and 100 and i shall guess, once ready press enter")
while running == True:
  print ("My guess is " + str(guess))
  indicator = input("Please input -1, 0, or 1 to indicate the guess is too low, exactly right, or too high (respectively)  ")
  if indicator == '-1':
    lower = guess + 1
    guess = (lower + upper) // 2
    counter +=1
  elif indicator == '0':
    print ("it took the system " + str(counter) + " tries")
    break
  elif indicator == '1':
    upper = guess - 1
    guess = (lower + upper) // 2
    counter +=1


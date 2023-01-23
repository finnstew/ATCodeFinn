from datetime import datetime
import shelve
import random
accounts = {}
current = None
prompts = ['Favorite food?', 'Least favorite food?', 'Favorite movie?', 'Least favorite movie?', 'Favorite subject?', 'Least favorite subject?']
responses = {}
responseCount = 0

class Take:
    def __init__(self, prompt,response, account, time):
        self.prompt = prompt
        self.response = response
        self.account = account
        self.time = time

class User:
  def __init__(self, name):
    self.name = name
    self.responseCodes = []

def start():
  global prompts
  global current
  global accounts

  with shelve.open('takes') as db:
    if 'accounts' in db:
      accounts = db['accounts']

    choice = input('[1] Create Account ; [2] Login')
    if choice == '1':
      name = input('Name: ')
      a = User(name)
      accounts[name] = a
      current = accounts[name]
      db['accounts'] = accounts
      main()

    if choice == '2':
      name = input('Login Name: ')
      if name in accounts:
        current = accounts[name]
        main()
      else:
        print('This account does not exist')
        start()

def main():
    global prompts
    global current
    global responses
    global responseCount

    with shelve.open('takes') as db:
      if 'responses' in db:
        responses = db['responses']
      if 'responseCount' in db:
        responseCount = db['responseCount']
      if 'prompts' in db:
        prompts = db['prompts']
      choice = input('1: Submit Topic | 2: Respond | 3: See Your Responses | 4: See Others Responses | 5. Logout ')

      if choice == '2':
        responseCount = responseCount + 1
        db['responseCount'] = responseCount
        prompt = prompts[random.randint(0, len(prompts)) - 1]
        print(prompt)
        r = Take(prompt, input('Respond Here: '), current.name, datetime.now())
        responses[str(responseCount)] = r
        main()

      if choice == '1':
        prompts.append(input('Question: '))
        db['prompts'] = prompts
        main()

      if choice == '3':
        for key in responses:
          g = responses[key]
          if g.account == current.name:
            print(g.prompt + ' Response: ' + g.response + ' at ' + str(g.time))
        main()

      if choice == '4':
        for key in responses:
          r = responses[key]
          print(r.prompt + ' Response: ' + r.response + ' at ' + str(r.time) + ' by ' + r.account)
        main()

      if choice == '5':
        start()

start()

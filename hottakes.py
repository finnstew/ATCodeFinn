class User:
  def __init__(self, name, passW, dayResponse):
    self.name = name
    self.passW = passW
    self.dayResponse = dayResponse

  def changeName(self, name):
    self.name = input("New Name: ")

  def changePass(self, passW):
    passAttempt1 = input("New Password: ")
    passAttempt2 = input("Confirm New Password: ")
    if passAttempt1 == passAttempt2:
      self.passW = passAttempt1

  def respondDaily(self, dayResponse):
    pass



import random
accounts = {}
current = None
daily question = " "
questions = ['Favorite food', 'favorite movie', 'worst tv show']


def start():

  global current

  choice = input('[1] Create Account ; [2] Login')

  if choice == '1':
    name = input('Name: ')
    a = User(name, '')
    accounts[name] = a
    current = accounts[name]
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
  dayQuestion = questions[random.randint(0 , len(questions) - 1)]
  print(dayQuestion)

  current.respondDaily()

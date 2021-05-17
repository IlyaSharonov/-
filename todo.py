import time


HELP = """
help  - список команд
add   - добавить задачу
show  - показать задачи
done  - убрать выполненную задачу
exit  - закрыть приложение
"""

todo = {}

def checkDate(date):
  try:
    time.strptime(date, "%d.%m.%Y")
    return True
  except ValueError:
    print("Error. Неправильный формат даты")
    return False

def add(command, usrAns):
  if command == 1:
    #получить дату
    print()
  elif command == 2:
    #получить task и добавить в todo
    print()


  userDate = input( "Введите дату:\n" )
  if checkDate(userDate) == False:
    continue
  userTask = input( "Что нужно сделать?" )

  if userDate in todo.keys():
    todo[ userDate ].append( userTask )
  else:
    todo[ userDate ] = [ userTask ]
  print(f"[ {userDate} ] - добавлена задача '{userTask}'")
print ("Введите команду, введите help для вывода списка команд")

while True:
  userAnswer = input()

  if userAnswer == "add":
    
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    for date in sorted( todo.keys() ):
      for tasks in todo[ date ]:
        print( f"[ {date} ] - {tasks}" )
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает\n") 

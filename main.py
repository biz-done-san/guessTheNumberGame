import sys
import random

def main():
      limit = int(sys.argv[1]) if sys.argv[1] is not None else 5
      printLimit(limit)
      n = inputIntValue()
      m = inputIntValue()
      answers = randIntArr(limit, n, m)
      guessTheAnswer(answers)
      
def printLimit(limit):
    sys.stdout.buffer.write(b"Limit is ")
    sys.stdout.flush()
    sys.stdout.buffer.write(str(limit).encode())
    sys.stdout.flush()
    sys.stdout.buffer.write(b"\n\n")
    sys.stdout.flush()

def inputIntValue():
    sys.stdout.buffer.write(b"Input value(Integer): \n")
    sys.stdout.flush()
    value = sys.stdin.buffer.readline().decode()
    return int(value)

def randIntArr(count, num1, num2):
    res = []
    if num1 > num2:
        tmp = num1
        num1 = num2
        num2 = tmp
    
    for i in range(count):
        res.append(random.randint(num1, num2))
    
    return res

def guessTheAnswer(intArr):
    for i in range(len(intArr)):
          sys.stdout.buffer.write(str(i+1).encode())
          sys.stdout.flush()
          sys.stdout.buffer.write(b": Guess the answer \n")
          sys.stdout.flush()
          userAnswer = int(sys.stdin.buffer.readline())
          if userAnswer == intArr[i]:
              sys.stdout.buffer.write(b"It's correct!!\n\n--- GAME CLEAR ---\n")
              sys.stdout.flush()
              return
          else:
              sys.stdout.buffer.write(b"It's incorrect!!\n\n")
              sys.stdout.flush()
              
    sys.stdout.buffer.write(b"--- GAME OVER ---\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
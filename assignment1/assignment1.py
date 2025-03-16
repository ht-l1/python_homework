# Write your code here.
# run the file by typing python assignment1.py in the terminal
# test by using commmand pytest -v-x assignment1-test.py

# Task 1
def hello():
 return "Hello!"

# Task 2
def greet(name):
 return(f"Hello, {name}!")

# Task 3
# a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) and power. The function returns the result.
def calc(a,b,operation="multiply"):
 try:
  match operation:
   case "add":
    return a + b
   case "subtract":
    return a - b
   case "multiply":
    return a * b
   case "divide":
    if b == 0:
     raise ZeroDivisionError
    return a / b
   case "modulo":
    if b == 0:
     raise ZeroDivisionError
    return a % b
   case "int_divide":
    if b == 0:
     raise ZeroDivisionError
    return a // b
   case "power":
    return a ** b
   case _:
    return "Invalid!"
   
 except ZeroDivisionError:
  return "You can't divide by 0!"
 except TypeError:
  return "You can't multiply those values!"

#  Task 4
# It takes two parameters, the value and the name of the data type requested, one of float, str, or int. Return the converted value.
def data_type_conversion(value, data_type_name):
 try:
  match data_type_name:
    case "float":
        return float(value)
    case "str":
        return str(value)
    case "int":
        return int(value)
    case _:
        return f"Invalid"
 except ValueError:
   return f"You can't convert {value} into a {data_type_name}."
 
 # Task 5
def grade(*args):
   try:
        #  compute the average, and return the grade
        avg = sum(args) / len(args)
        match avg:
          case avg if avg >= 90:
            return "A"
          case avg if avg >= 80:
            return "B"
          case avg if avg >= 70:
            return "C"
          case avg if avg >= 60:
            return "D"
          case avg if avg < 60:
            return "F"
   except (TypeError, ZeroDivisionError):
      return "Invalid data was provided."
   
# Task 6
def repeat(string, count):
  result = ""
  for _ in range(count):
    result += string
  return result

# Task 7
def student_scores(operation, **kwargs):
    #  If it is "best", the name of the student with the higest score is returned.
    if operation == "best":
      best_student_name = max(kwargs, key=kwargs.get)
      return best_student_name
    # If it is "mean", the average score is returned.
    elif operation == "mean":
      average_score = sum(kwargs.values()) / len(kwargs)
      return average_score
    else:
      return "Invalid"
        
# Task 8
def titleize(title):
  little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

  words = title.split()
  for i in range(len(words)):
    if i == 0 or i == len(words) - 1:
        words[i] = words[i].capitalize()
    elif words[i].lower() not in little_words:
        words[i] = words[i].capitalize()
  return " ".join(words)

# Task 9
def hangman(secret, guess):
    result = ""

    for i in secret:
      if i in guess:
        result += i
      else:
        result += "_"
    return result

# Task 10
def pig_latin(text):
    words = text.split()
    result = []
    
    for word in words:
        # (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end.
        if word[0] in 'aeiou':
            result.append(word + 'ay')
        # (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
        elif word.startswith('qu'):
            result.append(word[2:] + 'quay')
        # (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them
        else:
            # starting with the first index
            i = 0
            # Find where to split the word
            while i < len(word) and word[i] not in 'aeiou':
                # if 'qu' is in the middle, like 'square'
                if i < len(word) - 1 and word[i:i+2] == 'qu':
                    i += 2  # if "qu" matches, skip both 'q' & 'u'
                else:
                    i += 1
            
            result.append(word[i:] + word[:i] + 'ay')
    
    return ' '.join(result)
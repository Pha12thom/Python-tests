# If Statements
These statements are a bit like asking a question.
You are telling the computer: **if** something is true, **then** do this specific block of code.
Double equals (`==`) is asking the computer to compare if these two things are ***exactly*** the same.

&nbsp;

In the code below, I am asking `if` the variable `myName` is the same as the string `David`.

```python
myName = input("What's your name?: ")
if myName == "David":
```

## But that doesn't print anything?

To create a `print` statement related to the input from the if statement, you must go to the next line and indent **once** (Luckily, Replit does this for you, but be careful!) so it is all a part of the code we run.

👉 Copy this code and see what happens.

  
```python
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
  ```
  


## What is else?
If the condition is **not** met with the `if` statement, then we want the computer to do the `else` part instead.
Likewise, if the condition **is** met in the `if` statement, then the `else` bit is ignored by the computer.
The `else` statement must be the first thing **unindented** after the `if` statement and in line with it (Replit helps you out here too!)

👉 Copy this code and give it a go. Watch those indents!

 ```python
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
  print("You're just the baldest dude I've ever seen")
else:
  print("Who on earth are you?!")
  ```
&nbsp;
&nbsp;



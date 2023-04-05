# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Syntax Error
👉 What is wrong with this code below?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs = "cat":
  print("Meow")
else:
  print("Woof")
```
<details><summary>Answer 👀</summary>

- Our `if` statement must include `==` so it should read:
- `if catsOrDogs == "cat":`
</details>

## Syntax Error...again


👉 What is wrong with this code?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat"
  print("Meow")
else:
  print("Woof")
```
<details> <summary> Answer 👀</summary>

- Our `if` statement is missing the `:`
</details>

## Indentation Error

👉 Do you see the error here?
```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
print("Woof")
```
<details><summary>Answer 👀</summary>

- As soon as you see a colon, the next line should be indented **one** more than the line above it.
</details>


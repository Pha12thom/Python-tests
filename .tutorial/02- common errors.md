# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*
## Syntax Error

👉 What is wrong with the code below?


```python
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
else:
  print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
```

<details><summary> 👀 Answer  </summary>

```python
else:
  print("Nah, Daddy Pig's the greatest")
  ```
  
is not indented properly. 

- This `else` statement is referring to `faveCharacter` and therefore, both the above `else` and `print` statements need to be indented one time. Highlight them both and click 'tab' one time.
</details>


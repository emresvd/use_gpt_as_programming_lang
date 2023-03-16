# use gpt as programming language

this is a project to use GPT as a programming language.

## install requirements
```bash
pip install -r requirements.txt
```

## api key
you need to get an api key from [openai](https://openai.com/)<br>
and put it in a file called `.env` in the root of the project.<br>
the file should look like this:
```bash
OPENAI_API_KEY=your_api_key
```

<br><br>

## hello world
```
create a new string variable called hello
set the value of the hello variable to "hello world"
print the hello variable
```
or
```
print hello world
```
### run these codes:
```bash
python main.py examples/hello/hello1
python main.py examples/hello/hello2
```
### output:
```
hello world
```

<br><br>

## bubble sort
```
create a new array named a
add 7, 8, 9, 4, 5, 6, 1, 2, 3 and 0 to array a respectively
sorting an array with bubble sort
print array a
```
or
```
a = 7, 8, 9, 4, 5, 6, 1, 2, 3 and 0
bubble sort a
print a
```
### run these codes:
```bash
python main.py examples/bubble_sort/bubble_sort1
python main.py examples/bubble_sort/bubble_sort2
```
### output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# Lesson 1: factorial Numbers

In this we will cover the basics of Python, and end up writing a simple factorial generator.

## Setup

**NB:** This lesson assumes that you're using a Mac, although Linux and Windows will work very similarly.

Before we start, we must have a setup that allows us to both write and run Python code.  We will need a few things for this to work:

* The terminal (to run the programs);
* The Python language;
* A simple text editor that can understand Python syntax; and
* A way of running python programs.

### The Terminal

All the way through this lesson, you'll need to use the terminal. On a Mac, the easiest way to get this is to run the `Terminal.app` program. This is located in the *Applications → Utilities* folder. When you start this up, you'll get a input prompt that allows you to copntrol your computer using text. The program that you're now using to interact with the computer is called `bash`. If you've not used `bash` before, there are a lot of resources online to help you get up and running.  For this lesson though, you only need a few commands:

command         | description
----------------|------------
`cd <folder>`   | Go to the specified directory `<folder>`
`cd ..`         | Go up to the enclosing folder 
`ls`            | List all of the files and folders in the current directory
`pwd`           | Print the current directory
`python <file>` | Run the specified file using the python language
`mkdir <folder>`| Create the folder named `<folder>`
`touch <file>`  | Create a empty file named `<file>`, if there isn't already one (and does nothing if it already exists).


### Installing Python

You almost certainly already have Python installed. You can check this by typing the following command into the terminal:

~~~bash
python -V
~~~

This command runs pyhton, and asks it to tell us which version is installed. You will either get back a message telling you which version of python is running, or an error that looks something like:

~~~
-bash: python: command not found
~~~

If you see this message, then we need in install Python. We'll cover this separately if necessary.

**NB:** You should start learning Python 3. Python 2 is still very common, but almost everything you learn in Python 3 will work the same in older versions of Python.

### A Good Text Editor

A good text editor is to bioinformatics what a good pipette is to wet-lab work: an essential tools that will rapidly become an extension of yourself. It is therefore worth spending time to learn to use it well. It is up to you to choose an editor, but here are a few good ones for the Mac:

* [Atom](https://atom.io) (free, and works on many operating systems);
* [TextMate](https://macromates.com) (Not free, but my favourite);
* [BBEdit](http://www.barebones.com/products/bbedit/index.html);
* [Sublime Text](https://www.sublimetext.com)

Whatever editor you choose, make sure that you spend time to learn how it works. This effort now will be repaid tenfold later in your career.

## Starting A Project

Now that we have the tools, we can start to code. Open the terminal, and go to a sensible directory. The following commands will create a new folder on your desktop (called `01-python-tutorial`, and go into it (**NB:** The folder called `~` is a special way of saying *My Home Folder*)

~~~bash
cd ~/Desktop
mkdir 01-python-tutorial
cd 01-python-tutorial
~~~

You can always open a new Finder window in the current folder using the following command:

~~~bash
open .
~~~

Now, create an empty python script file in this directory:

~~~bash
touch ./01-factorial.py
~~~

This will create an empty file called `01-factorial.py` in the current folder. You can now open this file in your favourite editor. Keep the terminal window open, as we'll now use both the terminal and the editor together.

**NB:** The file extension `.py` is standard for Python files, put all this does is tell us that this is likely to be a Python file. There is no need to stick to this convention.

## Python first steps

In your text editor, write the following code into the editor, and save the file:

~~~python
print("Hello, World!")
~~~

Now, go back to the terminal and attempt to run the program:

~~~bash
python ./01-factorial.py
~~~

If everything works, you should see the following response on the screen:

~~~
Hello, World!
~~~

If so, Well Done!  This is a complete Python program. However, to be useful for more complex tasks, we must add more functionality.

## Getting Help

The most useful source of help for Python is the internet. [Stack Exchange](https://stackexchange.com) often has simple answers to complex questions; whilst the [Python website](https://www.python.org) has full documentation (at [https://docs.python.org/3/](https://docs.python.org/3/)).

### Basic Types & Variables

One of the most fundamental concepts in programming are variables. These are simply placeholders for variables (think of a variable as a box: a container where we can put something, and a label on the outside that we will use to retrieve the contents of the box). Creating variables is simple. Here, we create three variables:

~~~python
a = 12
b = 3.1415
c = "Hello"
~~~

You can refer to a variable by it's name.  Here, we create a new variable by reference to a pre-existing variable:

~~~python
d = a + 5
~~~

Hopefully, you can see that the value of `d` will be `17` (as the value of `a` is 12, and we added `5` to it).

Python allows for many different types of thing to be stored in a variable, but the most important ones for us are *numbers*, *boolean* values (True & False), and *strings* (words and characters).

#### Numbers

Python numbers are pretty intuitive. If the number does not have a decimal point it is an *integer*, whilst numbers with decimal parts are *floating-point*. Both can be used together (most of the time):

~~~python
x = 10
y = 0.5
z = x + y
~~~

We can use normal arithmatic on numbers, for example the python expression `x + y` will give `10.5`, whilst `x / y` will give `20.0`.

#### Boolean Values

Very frequently, we need to store a simple TRUE/FALSE value. This is done using the values `True` and `False` (**NB:** case is important!):

~~~python
a = True
~~~

#### Strings

Finally (for the simple types), we can store strings of characters as strings. We need to enclose the entire string we wish to store in quotes. It does not matter if we use single quotes (`'`) or double quotes (`"`), as long as we use the same at the beginning and end of the string:

~~~python
s = "Hello"
~~~

We can often use simple operators (like `+`, and `*`) for strings. Try the following:

~~~python
greeting = "Hello"
name = "Sathya"
res = greeting + ", " + name + "."
print(res)
~~~

Hopefully, when you run this program you will get the result:

~~~
Hello, Sathya.
~~~

#### Coercion

Python is pretty good at working out what kind of variable it is given, and doing sensible things to it. However, often you need to convert a value from one type to another. For example, we might need to convert the string "12" to the number 12. Of, get a string representation of the value -45. This is the process of coercion:

~~~python
x = str(12)
y = int("-45")
~~~

Try both of these. What happens when you ask for conversions that don't make sense?

### Collections

Although individual variables are very useful, often we need to store collections of values. Examples include:

* Lists of names, or numbers;
* Sets of values; and
* Sets of named *key:value* pairs

These are *collection* objects in Python, and are very easy to create.

#### Lists

The simplest collection is a list. A list is an *ordered* collection of values. We can create lists using square brackets:

~~~python
names = ['Alice', 'Bob', 'Charlie', 'Daisy']
~~~

We can now refer to a specifc *element* in the list also using square brackets, by using its *index* (i.e. its position in the index). **NB:** Python uses zero-based indexing, so the first entry in the list has an index of zero:

~~~python
print(names[0])
i = 2
print(names[i])
~~~

In the above code, the first line (`print(names[0])`) will return "Alice", as this is the first element in the list. What will the second and third line return? Try it.

We can pull out specific subsets of a list using a similar syntax:

~~~python
print(names[0:2])
~~~

will print `['Alice', 'Bob']`. The colon syntax defines a range (from the first element up to but not including the second element). So, the range `3:8` will return elements 3, 4, 5, 6, and 7.

We can append items to a list using the `append` list method (more on methods later):

~~~python
names.append('Erica')
print(names)
~~~


#### Dictionaries

Lists are fine for many uses, but sometimes we do not care about the order of elements, but rather we want to associate a value with a key (think of a dictionary in which a definition is associated with a key). For this we can use dictionaries. We create dictionaries using the curly-brace syntax:

~~~python
passwords = {'alice':'123', 'bob':'password', 'charlie':'password123'}
~~~

When using dictionaries, we can no longer use a number *index* to refer to an element (as dictionaries have *no order*), but rather we use the key:

~~~python
who = 'charlie'
print(paswords[who])
~~~

The above code will return `password123`. Try to use a numeric index as we did for lists, and see what happens.

We can add new elements to a dictionary by simply assigning a value to a new key:

~~~python
passwords['erica'] = 'oGoLgmbUnB94zgqUvEh39okCvRabfnY0'
~~~

**NB:** If we use a key that already exists, we'll simply overwrite the old key.

**NB:** Remember that the order of a elements in a dictionary is not defined. You should *never assume anything* about the order of values in dictionaries. 

### Testing

Once we've defined variables, we can write tests to check their values. Often, these tests will return either `True` or `False`. Several examples:

~~~python
x = 10
y = 5
print(x < 100)
print(x > 5)
print(x == 5)
print(x / 2 == y)
~~~

Try each of the above, and make sure that they make senbse to you.

**NB:** The operator `==` is *completely different* to the assignment operator `=`. `=` assigns values to variables, whilst `==` tests two things for equality.

### Looping

Often, we will want to do something multiple times. As you should always attempt to avoid repeating yourself when programming (fewer chances of introducing errors!), we need a way to `iterate` over multiple values. We do this with loops. Loops have a *condition* (which specifies the conditions for running the loop), and a *body* which will be run.

**NB:** Python uses indentation for defining blocks of code. In the following code, the body of the loop is indented. This is important. It does not matter if you use a tab, of several spaces (as long as you are consistent). The standard is to use 4 spaces.

Loops come in multiple flavours. Here, we'll cover `while` and `for`.

#### While Loops

A while loop will test its condition, and will continue to run whilst the condition is `True`. The following code will continue to run until the value of the variable `x` is no longer less than 10:

~~~python
x = 1
while x < 10:
    print(x)
    x = x + 1
~~~

Have a play.

#### For Loops

In a `for` loop, we specifiy a *loop variable* (often a list) that we wish to loop over. The loop will run with the specified loop variable getting each of the specified values in turn:

~~~python
names = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Erica']
for name in names:
   print('Hello ' + name + '.')
~~~

### Functions

We have already used several functions. A function is simply a named block of code that might have some parameters to pass in. You can think of a function as a black box: You give it inputs and it gives back outputs. Python functions behave very similarly to functions in mathematics.

We've already used several functions. `print` is a function, as is `append`. In both of these cases, we supplied some inputs (*parameters*) in parentheses. We can easily define our own functions:

~~~python
def add_one(x):
    return x + 1

a = 5
b = add_one(a)
print(y)
print(add_one(100))
~~~

**NB:** The single variable name `x` in the parenthesis during the function definition states that this function requires a single parameter. It is therefore an error to give it any other number of parameters. Furthermore, note that the variable called `x` *inside* the function is separate to the value *outside* the function. Thus, if we assign a value to `x` inside the function, any variable outside the function that is also called `x` will be uneffected. This is called *scope* and is quite a tricky idea to get your head around...

If a function block contains the `return` keyword, then the function will return a value. However, functions do not need to return values.

### Putting it all Together

To wrap up this lesson, we will now create a function to generate factorial numbers. A factorial number is defined as the sum of the preceeding numbers (see [Wikipedia](https://en.wikipedia.org/wiki/Factorial)). For example, 3 factorial (written `3!`) is `3 * 2 * 1 * 0`; where `0!` is defined as 1.

We could hard-code the values into a list, but that would be cheating. Instead we wish to create a function to do this. We therefore want to create a function that takes a single integer `x` and returns a new integer that is `x!`.

Once written, we wish to generate a list of all the values of x! from 1 to 10.

Before continuing, have a think about how you could do this.

There are many ways to do this, but about the simplest is this:

~~~python
def factorial(x):
    if x == 0: return 1
    return x * factorial(x - 1)
~~~

Have a thinmk about this code. It is simple, but really very powerful. The first line simply defines a function called `factorial` that takes a single value. The second line tests to see if `x` is equal to zero, and if it is then it returns `1`. The next line is more clever: it returns the value of `x` multiplied by the value obtained from running the same function on `x-1`. This technique of using a function within its own definition is called *recursion*, and is often very powerful.

We can now use this function to give us all the factorial values from 1 to 50 as follows. (In this code, we use the `range` function which returns a list of all integers from its first argument up to but not including its second):

~~~python
max_i = 50
n = range(1, max_i + 1)
for i in n:
    print('The value of ' + str(i) + '! is ' + str(factorial(i)) + '.')
~~~

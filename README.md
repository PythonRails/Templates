Pyth*on*Rails Templates
===

Easy to use and very simple structured templates in python style.

Syntax of templates very similar to Python. After transformation you will get python files with commands that will be executed as regular python code. It allow  you to understand how it work, where is it work wrong and how to improve it. Also you can extend templates with your custom template tags by creating very simple python class for each new tag in templates code.

For example - you write in template **`div: Hello`** and know that will be created instance of **`TagDiv`** with pass **`Hello`** as first parameter. If you write **`div.main: It works!`** that it will be converted to python code **`TagDiv('It works!', _class='main')`**. More complex: **`a.button.active onclick='alert("Clicked")'`** will be ransformed to **`TagA(_class='button active', _onclick='alert("Clicked"))`**.

As you can see - you can extend this template engine as you like.

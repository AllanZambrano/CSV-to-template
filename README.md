# CSV-to-template
Dynamically generate word documents using data from a CSV - with 1 template file.

## How to use it
Open the command line and write the following lines.

```cmd
pip install docxtpl
pip install pandas
pip install wheel
pip install numpy==1.19.3
```


## Template
In order to use the template, you'll need to watch 2 things:
1) Column title: Use the column name between curly brackets to call it on the Template.    
2) Template: To call the information on the template, you just need to call the column title between curly brackets.  
    Example: My name is {{ name }}. 
3) Run script


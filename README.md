# user_gen
Random User Generator

This is a package designed to generate users for testing applications. It has functions for generating realistic names and emails, and a value attribute.
It's name generation is based on [this repo](https://github.com/treyhunner/names). 

## Usage
user_gen can be used as a command line utility or an imported python package.

### Command Line Usage
To use the script from the command line: 
```
$python user_gen.py
```
It will print the 100 JSON encoded users and generate a JSON lines file with the users generated

### Python Package Usage
```
>>> import user_gen
>>> user_gen.MakeUser('')
{'first_name': 'Mary', 'last_name': 'Jane', 'full_name': 'Mary Jane', 'email': 'maryjane@gmail.com', 'attr_value': 110 }
>>> user_gen.MakeUser_value('')
{'first_name': 'Bernard', 'last_name': 'Szczepanek', 'full_name': 'Bernard Szczepanek', 'email': 'bernardszczepanek998@gmail.com', 'attr_value': 998 }
```



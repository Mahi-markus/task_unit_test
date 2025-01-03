
### Libray Management System Testing ###

**required tool and prerequisite**
- pytest
- coverage 
- python 3.8+


## Steps of installations and step the project ##

```bash
git clone https://github.com/Mahi-markus/task_unit_test.git

```

 **then setup the environment**
```bash 
python3 -m venv venv        #On macOS/Linux:
source venv/bin/activate
```



**open a terminal and paste the below command**

```bash
pip install pytest coverage
```

```bash
pytest
coverage run -m pytest test_library.py 
coverage report -m
```
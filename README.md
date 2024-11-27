# curd_operation_on_file

# setup instruction

# clone the repo
```bash
git clone https://github.com/Aashish-Raj/curd_operation_on_file.git
```

## setup

# ftech all branch
```bash
git fetch --all
```

# swith to file_ops
```bash
git checkout file_ops
```

# create the  environmet file
```python
python -m venv env
```

# cd to project file
```bash
cd curd_operation_on_file/document_listing_pro
```


# install the required pakages

```python
pip install -r requirements.txt
```

# make migrations 
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```

# runserver 
```python
python manage.py runserver 8000
```


# curd_operation_on_file

# setup instruction
gitclone: git clone https://github.com/Aashish-Raj/curd_operation_on_file.git

# fetch all the  branch
git fetch --all

# swith to file_ops
git checkout file_ops

# create the  environmet file
python -m venv env

# cd to project file
cd curd_operation_on_file/document_listing_pro

# install the required pakages
pip install -r requirements.txt

# make models 
python manage.py makemigrations
python manage.py migrate


# runserver 
python manage.py runserver 8000

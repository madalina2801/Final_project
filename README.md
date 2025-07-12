# Final_project
Final project about  python and django 
pyhon --version                             --> python version 3.13
python -m venv venv                         --> creates a python virtual enviroment with the name : venv 
where pyhton                                --> locates where python system variable is in PC 
source venv/Scripts/activate                --> activates virtual enviroment that was created at previous step (venv)
pip install -r requirements.txt             --> instals the packages that are mentioned in requirements.txt file (like django == 5.2.3)
pip list                                    --> lists all the packages installed 
where pip                                   --> locates where pip packages are located in PC
django-admin startproject name_project      --> creates django project 

python manage.py runserver                  --> runs the server applications (at this point you should make sure to be in the right folder of the django project /name_project )
python manage.py migrate                    --> apply migrations to the project (should be requested after first runserver)

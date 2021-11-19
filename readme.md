# The Penalty Box

The Penalty Box is a blog built using Python and the Django Framework! I am the author of the site and am able to create, post, and edit my own blogs. I wanted to build a blog that causes a bit of controversy in order to rile visitors up enough that they can't help but come back in order to prove me wrong! Currently under construction is the ability for visitors of the site to create a profile as well as edit and delete their own comments. In the future there will also be a store in which visitors will be able to purchase merch! You can visit the site here...
[The Penalty Box](https://penalty-box.herokuapp.com/)

The Wireframes, Models, User Stories, and User flow can all be accessed here...
[Penalty Box Designs](https://drive.google.com/drive/folders/1G-zAkFpX8eAKDwrL6YwWN_HCxGC3lSUH?usp=sharing)

## Installation
If you would like to help further develope this blog follow the instructions below.

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project.


## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/michaelbryanstark/penalty-box.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## Technologies Used
- Python
- Django
- HTML5
- Bootstrap 4
- PostgreSQL
- Heroku
- Git
- GitHub


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
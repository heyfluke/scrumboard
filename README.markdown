# installation & usage

    $ git clone git://github.com/heyfluke/scrumboard.git
    $ cd scrumboard
    $ pip install -r requirements.txt
    $ cp scrumboard/settings/local-dist.py scrumboard/settings/local.py # and edit local.py to change db path.
    $ ./manage.py syncdb
    $ ./manage.py runserver 0.0.0.0:8081

Then view http://127.0.0.1:8081 in browser. Enjoy.

=========
Odoo demo
=========

Setup you dev environment
=============================

Clone the project repository :

    `git clone git@github.com:regispirard/demo-project.git`

Install pip-deepfreeze [#]_ using pipx [#]_ (so it wont be installed in the same virtualenv as your project) :

    `pipx install pip-deepfreeze`

This project uses code formatters to make sure the coding conventions are respected.
Install pre-commit [#]_ after cloning the repository and run :

     `pre-commit install`

Install bump2version [#]_ for an versioning of the project :

    `pipx install bump2version`

Make sure msgmerge is installed on your system (usefull for the maintaining of .po / translation files).

    `sudo apt install gettext`

Create and activate a virtualenv (using for example virtualenvwrapper's [#]_):

    `mkvirtualenv demo -a . --python=$(which python3.11)`

In your activated python3.11 virtualenv, run:

    `pip-df sync`

! Important : you will have to run ``pip-df sync`` again later if there is any change in the dependencies of the project (cf. requirements.txt).

Copy ``odoo.cfg.template`` to ``odoo.cfg`` and update it as needed (set value for admin_passwd), then run:

    `cp odoo.cfg.template odoo.cfg`

Run odoo and create your local database with the project installed :

    `odoo -c odoo.cfg -d demo -i demo`


Upgrade database
----------------

After any modification, use click-odoo-update to automatically update modules which needs an upgrade (and only thoses) :

    `click-odoo-update -c odoo.cfg -d demo --i18n-overwrite`

Maintain .po files (Translation)
--------------------------------

Run click-odoo-makepot :

    `click-odoo-makepot -c odoo.cfg -d demo --commit --msgmerge --addons-dir=<path>/demo/odoo/addons/`

Release
-------

Once the code is ready for deployement, use bump2version to create a version tag and push it on the repository :
! Note : this should be done on the main project/iteration branch (and not on your developpement branch).

    For a patch version : `bump2version patch` (eg : 1.0.0 -> 1.0.1)
    For a minor version : `bump2version minor` (eg : 1.0.1 -> 1.1.0)
    For a major version : `bump2version major` (eg : 1.1.0 -> 2.0.0)

.. [#] https://pypi.python.org/pypi/pip-deepfreeze
.. [#] https://pypa.github.io/pipx/
.. [#] https://github.com/pre-commit/pre-commit
.. [#] https://pypi.org/project/bump2version/
.. [#] https://virtualenvwrapper.readthedocs.io/en/latest/install.html

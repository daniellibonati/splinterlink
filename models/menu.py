# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('Buttons'), False, URL('button','show')),
        (T('Manage'), False, '#', [
            (T('Users'), False, URL('user', 'manage')),         
            (T('Groups'), False, URL('group', 'manage')),
            (T('Buttons'), False, URL('button', 'manage'))
        ])
    ]

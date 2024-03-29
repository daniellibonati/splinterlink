# -*- coding: utf-8 -*-

db.define_table('button_group',
                Field('name', 'string', label=T('Group Name')),
                Field('bootstrap_class', 'list:string', requires=IS_IN_SET(
                    ('primary',
                     'secondary',
                     'success',
                     'danger',
                     'warning',
                     'info',
                     'light',
                     'dark',
                     'link'
                    ))),
                format='%(name)s'
               )

db.define_table('button',
                Field('button_group_id', 'reference button_group', required=True, label=T('Button Group')),
                Field('name', 'string', required=True, notnull=True),
                Field('url', 'string', required=True, notnull=True, default="", label=T('URL')),
                Field('bootstrap_class', 'list:string', requires=IS_IN_SET(
                    ('primary',
                     'secondary',
                     'success',
                     'danger',
                     'warning',
                     'info',
                     'light',
                     'dark',
                     'link'
                    ))),
                Field('outline', 'boolean', label=T('Outline')),
                format='%(name)s'
                )

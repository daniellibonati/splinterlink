# -*- coding: utf-8 -*-

@auth.requires_login()
def manage():
    form = SQLFORM.grid(db.button_group)
    return dict(form=form)

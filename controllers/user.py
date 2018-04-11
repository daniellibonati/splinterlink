# -*- coding: utf-8 -*-

@auth.requires_login()
def manage():
    form = SQLFORM.grid(db.auth_user)
    return dict(form=form)

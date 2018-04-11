# -*- coding: utf-8 -*-

@auth.requires_login()
def manage():
    form = SQLFORM.grid(db.button)
    return dict(form=form)


@auth.requires_login()
def show():
    groups = db(db.button_group).select()
    buttons = db(db.button).select(orderby=db.button.name)
    return dict(groups=groups, buttons=buttons)

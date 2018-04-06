# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from group.py")

def manage():
    form = SQLFORM.grid(db.button_group)
    return dict(form=form)

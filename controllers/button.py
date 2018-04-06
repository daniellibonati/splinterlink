# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from button.py")

def manage():
    form = SQLFORM.grid(db.button)
    return dict(form=form)

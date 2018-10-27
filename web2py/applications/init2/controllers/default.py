# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import datetime


def index():
    result = [] # We will accummulate the result here.
    for r in db(db.eventpost.id > 0).select():
        # This is a loop over all the eventposts.

        # Each eventpost can have replies; you need to read here the list of replies.
        # As each companypost has an author and a content, a list of dictionaries seems
        # appropriate here.
        companypost_list=[]
        replies = db(db.companypost.eventpost_id == r.id).select(orderby=db.companypost.companypost_time)
        for companypost in replies:
            companypost_list.append(dict(
                companypost_id = companypost.id,
                companypost_author = companypost.companypost_author,
                companypost_content = companypost.companypost_content,
            ))

        result.append(dict(
            eventpost_title=r.eventpost_title,
            eventpost_author=r.eventpost_author,
            eventpost_content=r.eventpost_content,
            companypost_list=companypost_list,
            id=r.id,
        ))

    logger.info("Result: %r" % result)
    return dict(rows=result)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

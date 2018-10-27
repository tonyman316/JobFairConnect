def index():
    pass


@auth.requires_login()
def add_eventpost():
    """More sophisticated way, in which we use web2py to come up with the form."""
    form = SQLFORM(db.eventpost)
    # We can process the form.  This will check that the request is a POST,
    # and also perform validation, but in this case there is no validation.
    # THIS process() also inserts.
    if form.process().accepted:
        redirect(URL('default', 'index'))
    # We ask web2py to lay out the form for us.
    logger.info("My session is: %r" % session)
    return dict(form=form)


# We require login.
@auth.requires_login()
def edit_eventpost():
    """Allows editing of a eventpost.  URL form: /default/edit/<n> where n is the eventpost id."""

    # For this controller only, we hide the author.
    db.eventpost.eventpost_author.readable = False

    eventpost = db.eventpost(request.args(0))
    # We must validate everything we receive.
    if eventpost is None:
        logging.info("Invalid edit call")
        redirect(URL('default', 'index'))
    # One can edit only one's own eventposts.
    if eventpost.eventpost_author != auth.user.email:
        logging.info("Attempt to edit some one else's eventpost by: %r" % auth.user.email)
        redirect(URL('default', 'index'))
    # Now we must generate a form that allows editing the eventpost.
    form = SQLFORM(db.eventpost, record=eventpost)
    if form.process().accepted:
        # The deed is done.
        redirect(URL('default', 'index'))
    return dict(form=form)


@auth.requires_signature()
@auth.requires_login()
def delete_eventpost():
    eventpost = db.eventpost(request.args(0))
    # We must validate everything we receive.
    if eventpost is None:
        logging.info("Invalid edit call")
        redirect(URL('default', 'index'))
    # One can edit only one's own eventposts.
    if eventpost.eventpost_author != auth.user.email:
        logging.info("Attempt to edit some one else's eventpost by: %r" % auth.user.email)
        redirect(URL('default', 'index'))
    db(db.eventpost.id == eventpost.id).delete()
    redirect(URL('default', 'index'))

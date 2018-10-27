@auth.requires_login()
def add_companypost():
    """COMPLETE (and remove line below or replace as appropriate)"""
    # You will be creating a form, in some way, e.g. using SQLFORM, and you will write
    # BEFORE processing the form:
    form = SQLFORM(db.companypost)
    form.vars.eventpost_id = int(request.args[0])
    if form.process().accepted:
        redirect(URL('default', 'index'))
    logger.info("My session is: %r" % session)
    return dict(form=form)


@auth.requires_login()
@auth.requires_signature()
def edit_companypost():
    """COMPLETE (and remove line below or replace as appropriate)"""
    db.companypost.id.readable = False

    companypost = db.companypost(request.args(0))
    # We must validate everything we receive.
    if companypost is None:
        logging.info("Invalid edit call")
        redirect(URL('default', 'index'))
    # One can edit only one's own companypost.
    if companypost.companypost_author != auth.user.email:
        logging.info("Attempt to edit some one else's eventpost by: %r" % auth.user.email)
        redirect(URL('default', 'index'))
    # Now we must generate a form that allows editing the companypost.
    form = SQLFORM(db.companypost, record=companypost)
    if form.process().accepted:
        # The deed is done.
        redirect(URL('default', 'index'))
    return dict(form=form)


@auth.requires_login()
@auth.requires_signature()
def delete_companypost():
    """COMPLETE (and remove line below or replace as appropriate)"""
    companypost = db.companypost(request.args(0))
    # We must validate everything we receive.
    if companypost is None:
        logging.info("Invalid edit call")
        redirect(URL('default', 'index'))
    # One can edit only one's own companypost.
    if companypost.companypost_author != auth.user.email:
        logging.info("Attempt to edit some one else's eventpost by: %r" % auth.user.email)
        redirect(URL('default', 'index'))
    db(db.companypost.id == companypost.id).delete()
    return redirect(URL('default', 'index'))

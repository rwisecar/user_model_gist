from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from sqlalchemy.exc import DBAPIError

from ..security import check_credentials

from ..models import User


@view_config(route_name='list', renderer='../templates/list.jinja2')
def list_view(request):
    """Show simple home page."""
    return {}


@view_config(
    route_name='register',
    renderer='../templates/register.jinja2')
def register_view(request):
    """Allow users to register new usernames."""
    if request.method == "POST":
        try:
            new_first = request.POST["first_name"]
            new_last = request.POST["last_name"]
            new_email = request.POST["email"]
            new_username = request.POST["username"]
            new_password = request.POST["password"]
            new_food = request.POST["favorite_food"]
            query = request.dbsession.query(User)
            user = query.filter(User.id == request.matchdict["id"])
            user.update({
                "first_name": new_first,
                "last_name": new_last,
                "email": new_email,
                "username": new_username,
                "password": new_password,
                "favorite_food": new_food
                })
            return HTTPFound(location=request.route_url('profile'))
        except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)
        return {}


@view_config(
    route_name='profile',
    renderer='..templates/profile.jinja2',
    permission="add")
def profile_view(request):
    """Allow registered, logged in users to view profile info."""
    try:
        query = request.dbsession.query(User)
        user = query.filter(User.id == request.matchdict["id"]).first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'user': user}


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login_view(request):
    """Allow users to login and route to profile page."""
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        if check_credentials(username, password):
            auth_head = remember(request, username)
            return HTTPFound(
                location=request.route_url("profile"),
                headers=auth_head
            )
    return {}


@view_config(route_name="logout")
def logout_view(request):
    auth_head = forget(request)
    return HTTPFound(location=request.route_url("list"), headers=auth_head)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_user_model_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

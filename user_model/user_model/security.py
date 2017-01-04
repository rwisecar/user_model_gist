import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Authenticated, Allow
from pyramid.session import SignedCookieSessionFactory
from passlib.apps import custom_app_context as pwd_context

from .models import User


class MyRoot(object):

    def __init__(self, request):
        self.request = request

    __acl__ = [
        (Allow, Authenticated, "add"),
    ]


def check_credentials(username, password, request):
    """Check user credentials to determine access; returns a boolean."""
    query = request.dbsession.query(User).all()
    if username and password:
        if username in query:
            db_user = query.filter(
                User.username == request.matchdict["username"].first())
            if pwd_context.verify(password, db_user.password):
                return True
    return False


def includeme(config):
    """Establish Pyramid security configuration."""
    auth_secret = "lalala"
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg="sha512"
    )
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(MyRoot)

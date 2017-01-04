"""Adding routes for the configuration to find."""


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list', '/')
    config.add_route('profile', '/profile/{id:\d+}')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')

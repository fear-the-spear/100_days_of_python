# Advanced Python Decorator Functions

# here is a very basic class (User), that has a name and and is_logged_in
#   property. we want to pass this user object to a 'create_blog_post'
#   function, but ONLY if the 'is_logged_in' property is set to 'True'

class User:
    def __init__(self, name):
        self.name = name.capitalize()
        self.is_logged_in = False

# this decorator function will run 'create_blog_post' if the user's
#   'is_logged_in' property is set to True


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            # the 'user' argument that was passed into 'create_blog_post' is
            #   a positional argument at position '0'
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User('dakota')
new_user.is_logged_in = True
create_blog_post(new_user)

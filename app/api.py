# from flask.ext.login import current_user
# PLACEHOLDER
# from flask.ext.restless import ProcessingException

# - Note: If IDE shows weak warning '**kwargs unused', that is technically untrue. Calling function will use.


class ApiAuth:
    # @classmethod
    # def logged_in(cls, **kwargs):
    #     user_logged_in = False
    #     if not current_user.is_authenticated():
    #         raise ProcessingException(description='Not Authorized. Please log in first.', code=401)
    #     elif current_user.is_authenticated():
    #         user_logged_in = True
    #     return user_logged_in

    # @classmethod
    # def basic_admin(cls, **kwargs):
    #     user_logged_in = cls.logged_in()
    #     allowable_roles = ('basic', 'super', 'master')
    #     if user_logged_in:
    #         if current_user.admin_role not in allowable_roles:
    #             raise ProcessingException(description='Not Authorized. Basic administrative permissions or higher '
    #                                                   'required.', code=401)

    @classmethod
    def super_admin(cls, **kwargs):
        # PLACEHOLDER
        # user_logged_in = cls.logged_in()
        user_logged_in = True
        allowable_roles = ('super', 'master')
        # if user_logged_in:
            # if current_user.admin_role not in allowable_roles:
            #     raise ProcessingException(description='Not Authorized. Super administrative permissions or higher '
            #                                           'required.', code=401)

    # @classmethod
    # def master_admin(cls, **kwargs):
    #     user_logged_in = cls.logged_in()
    #     allowable_roles = ('master')
    #     if user_logged_in:
    #         if current_user.admin_role not in allowable_roles:
    #             raise ProcessingException(description='Not Authorized. Master administrative permissions or higher '
    #                                                   'required.', code=401)

    def __init__(self):
        self.description = 'API Authorization Object'

    def __repr__(self):
        return 'API Authorization Object'



class BaseTemplate(object):
    """
    Base class for auto-generated templates.
    """
    
    def use(self, libs):
        """
        Include libs to extend behaviour.
        """
        pass

    def __getattr__(self, name):
        """
        Get virtual tag or variable.
        """
        if name.startswith('tag_'):
            # return tag instance
            pass
        elif name.startswith('var_'):
            # return variable value
            pass
        raise Exception


class BaseTag(object):
    """
    Base class for all Tags.
    """
    pass

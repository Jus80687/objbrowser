""" 
   Program that shows the local Python environment using the inspect module
"""
from __future__ import print_function

import sys, logging
from objbrowser import browse, create_object_browser, execute, logging_basic_config

logger = logging.getLogger(__name__)

MY_CONSTANT = 55
YOUR_CONSTANT = MY_CONSTANT
ANOTHER_CONSTANT = MY_CONSTANT * 2

def call_viewer_test():
    """ Test procedure. 
    """
    import types, os
    from os.path import join
    
    if 1:
        class OldStyleClass: 
            """ An old style class (pre Python 2.2)
                See: http://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes
            """
            static_member = 'static_value'
            def __init__(self, s, i):
                'constructor'            
                self._member_str = s
                self.__member_int = i
                
        class NewStyleClass(object):
            """ A new style class (Python 2.2 and later). Note it inherits 'object'.
                See: http://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes
            """
            static_member = 'static_value'
            def __init__(self, s, i):
                'constructor'
                self._member_str = s
                self.__member_int = i
                
            @property
            def member_int(self):
                return self.__member_int
                
            @member_int.setter
            def member_int(self, value):
                self.__member_int = value
                
            def method(self):
                pass
            
        
        old_style_object = OldStyleClass('member_value', 44)    
        new_style_object = NewStyleClass('member_value', -66)    

    # Some comments just above
    # the function definition.
    def my_function(param):
        "demo function"
        return param
    
    _copyright = types.__builtins__['copyright'] 
    
    x_plus_2 = lambda x: x+2
    
    d = {'4': 44, 's': 11}
    a = 6
    b = 'seven'
    n = None
    tup = ('this', 'is', 'a tuple')
    lst = [4, '4', d, ['r', dir], main]
    my_set = set([3, 4, 4, 8])
    my_frozenset = frozenset([3, 4, 5, 6, 6])
    
    # These will give error in the str() representation. 
    # I deliberately did not use string.encode('ascii', 'backslashreplace') to 
    # demonstrate the difference between str() and repr()
    u1 = unichr(40960) + u'ab\ncd' + unichr(1972)
    u2 = u"a\xac\u1234\u20ac\U00008000"
    u3 = u'no strange chars'
    multi_line_str = """hello\r\nworld
                        the\rend."""
    
    # When creating multiple object browsers, make sure to keep a
    # reference to each of them. Otherwise windows will be garbabe-
    # collected and will disappear.
    _locals_obj_browser = create_object_browser(obj = locals(), # without obj_name
                                                show_special_attributes = None, 
                                                show_callables = None ) 
    #_globals_obj_browser = create_object_browser(obj = globals(), obj_name = 'globals',
    #                                             attr_columns = ALL_ATTR_MODELS[1:4], 
    #                                             attr_details = ALL_ATTR_DETAILS)
    exit_code = execute()
    return exit_code
    

def call_viewer_small_test():
    """ Test procedure. 
    """
    try:
        raise ValueError("my value error")
    except ValueError, ex:
        my_value_error = ex

    a = 6
    b = ['seven', 'eight']
    nested_list = [5, 6, 'a', ['r', 2, []], (a, b), range(1, 100), my_value_error]
    exit_code = browse(obj = nested_list, obj_name='nested_list', show_root_node = True)
    return exit_code
    
        
def main():
    """ Main program to test stand alone 
    """
    logging_basic_config('DEBUG')
    logger.info('Started example')
    
    if 1:
        exit_code = call_viewer_test()
    else: 
        exit_code = call_viewer_small_test() 
    
    logging.info('Done example')
    sys.exit(exit_code)

if __name__ == '__main__':
    main()

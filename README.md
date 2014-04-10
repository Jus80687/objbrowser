objbrowser
==========

Extensible Python object inspection tool implemented in Qt.

Displays objects as trees and allows you to inspect their attributes
recursively (e.g. browse through a list of dictionaries). You can add 
your own inspection methods as new columns to the tree view, or as radio buttons
to the details pane. Altering existing inspection methods is possible as well.
#### Installation:

1.	Install PySide:
	http://qt-project.org/wiki/Category:LanguageBindings::PySide
	
2.	Run the installer:

		%> pip install objbrowser
		

#### User interface:

![objbrowser screen shot](screen_shot.png)


From the _View_ menu you can select some extra columns, for instance the 
objects' _id_ column. This can also be done by right-clicking on the table
header.

If the _Show routine attributes_ from the _View_ menu is checked, 
functions and methods that are attributes of the object are shown, 
otherwise they are hidden. Routines that are not an object attribute, for
instance functions that are an element in a list, are always displayed.

If the _Show special attributes_ from the _View_ menu is checked,
attributes whos name start and end with two underscores are displayed.

The details pane at the bottom shows object properties that do not fit
on one line, such as the docstrings and the output of various functions 
of the `inspect` module from the Python standard library.


	
#### Usage examples:

The first parameter is the object to be inspected. For example you can 
examine the dictionary with the local variables:

```Python
from objbrowser import browse
a = 67; pi = 3.1415 
browse(locals())
```

The second parameter can be the name of the object. In that case the object
itself will be displayed in the root node.

```Python
browse(locals(), 'locals()')
```

By setting the `show_routine_attributes` and/or the `show_special_attributes` 
parameters you can override the settings from the _View_ menu. The `reset`
parameter resets the persistent window settings (e.g. size and position)

```Python
s1 = 'Hello'
s2 = 'World'

browse({'s1': s1, 's2': s2}, 
        show_routine_attributes = True,
        show_special_attributes = False, 
        reset = True)
```

Some complete examples can be found in the [examples directory](examples). E.g.:

* [Define your own column](examples/simple_add_column.py)
* [Override the summary column](examples/override_summary.py)
* [Show two browser windows simultaneously](examples/modules.py)

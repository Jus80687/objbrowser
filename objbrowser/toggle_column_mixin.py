""" Defines ToggleColumnMixIn class
"""
from __future__ import print_function

import logging
from PySide import QtCore, QtGui
from PySide.QtCore import Qt

logger = logging.getLogger(__name__)



class ToggleColumnMixIn(object):
    """ Adds actions to a QTableView that can show/hide columns 
        by right clicking on the header
    """ 
    def add_header_context_menu(self, checked = None, checkable = None, enabled = None):
        """ Adds the context menu from using header information
        
            checked can be a header_name -> boolean dictionary. If given, headers
            with the key name will get the checked value from the dictionary. 
            The corresponding column will be hidden if checked is False.
        
            checkable can be a header_name -> boolean dictionary. If given, headers
            with the key name will get the checkable value from the dictionary.
            
            enabled can be a header_name -> boolean dictionary. If given, headers
            with the key name will get the enabled value from the dictionary.
        """
        checked = checked if checked is not None else {}
        checkable = checkable if checkable is not None else {}
        enabled = enabled if enabled is not None else {}
        
        horizontal_header = self._horizontal_header()
        horizontal_header.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.toggle_column_actions_group = QtGui.QActionGroup(self)
        self.toggle_column_actions_group.setExclusive(False)
        self.__toggle_functions = []  # for keeping references
        
        for col in range(horizontal_header.count()):
            column_label = self.model().headerData(col, Qt.Orientation.Horizontal, Qt.DisplayRole)
            logger.debug("Adding: col {}: {}".format(col, column_label))            
            action = QtGui.QAction("Show {} column".format(column_label), 
                                   self.toggle_column_actions_group, 
                                   checkable = checkable.get(column_label, True), 
                                   enabled = enabled.get(column_label, True), 
                                   toolTip = "Shows or hides the {} column".format(column_label))
            func = self.__make_show_column_function(col) 
            self.__toggle_functions.append(func) # keep reference
            horizontal_header.addAction(action)
            is_checked = checked.get(column_label, not horizontal_header.isSectionHidden(col))
            horizontal_header.setSectionHidden(col, not is_checked)
            action.setChecked(is_checked)
            assert action.toggled.connect(func)
    
    
    def get_header_context_menu_actions(self):
        """ Returns the actions of the context menu of the header
        """
        return self._horizontal_header().actions()
        
        
    def _horizontal_header(self):
        """ Returns the horizontal header (of type QHeaderView).
        
            Override this if the horizontalHeader() function does not exist.
        """
        return self.horizontalHeader()
        
        
    def __make_show_column_function(self, column_idx):
        """ Creates a function that shows or hides a column."""
        show_column = lambda checked: self.setColumnHidden(column_idx, not checked)
        return show_column   
    
    
    def read_view_settings(self, key, settings=None, reset=False):
        """ Reads the persistent program settings
        
            :param reset: If True, the program resets to its default settings
            :returns: True if the header state was restored, otherwise returns False
        """ 
        logger.debug("Reading view settings for: {}".format(key))
        header_restored = False
        if not reset:
            if settings is None:
                settings = QtCore.QSettings()
            horizontal_header = self._horizontal_header()
            header_restored = horizontal_header.restoreState(settings.value(key))
            
            # update actions
            for col, action in enumerate(horizontal_header.actions()):
                is_checked = not horizontal_header.isSectionHidden(col)
                action.setChecked(is_checked)
                
        return header_restored

    def write_view_settings(self, key, settings=None):
        """ Writes the view settings to the persistent store
        """         
        logger.debug("Writing view settings for: {}".format(key))
        
        if settings is None:
            settings = QtCore.QSettings()
        settings.setValue(key, self._horizontal_header().saveState())



class ToggleColumnTableWidget(QtGui.QTableWidget, ToggleColumnMixIn):
    """ A QTableWidget where right clicking on the header allows the user to show/hide columns
    """
    pass

        
        
class ToggleColumnTreeWidget(QtGui.QTreeWidget, ToggleColumnMixIn):
    """ A QTreeWidget where right clicking on the header allows the user to show/hide columns
    """
    def _horizontal_header(self):
        """ Returns the horizontal header (of type QHeaderView).
        
            Override this if the horizontalHeader() function does not exist.
        """
        return self.header()   
    
        
        
class ToggleColumnTreeView(QtGui.QTreeView, ToggleColumnMixIn):
    """ A QTreeView where right clicking on the header allows the user to show/hide columns
    """
    def _horizontal_header(self):
        """ Returns the horizontal header (of type QHeaderView).
        
            Override this if the horizontalHeader() function does not exist.
        """
        return self.header()   
    


        
        
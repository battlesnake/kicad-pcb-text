# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-88b0f50)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class CloneSettingsDialog
###########################################################################

class CloneSettingsDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Clone settings", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		rows_0_sizer = wx.BoxSizer( wx.VERTICAL )

		columns_1_sizer = wx.BoxSizer( wx.HORIZONTAL )

		instances_sizer = wx.BoxSizer( wx.VERTICAL )

		self.instances_label = wx.StaticText( self, wx.ID_ANY, u"Instances to clone the layout into", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.instances_label.Wrap( -1 )

		instances_sizer.Add( self.instances_label, 0, wx.ALL, 5 )

		self.instances = wx.dataview.DataViewTreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_MULTIPLE|wx.dataview.DV_NO_HEADER )
		instances_sizer.Add( self.instances, 1, wx.ALL|wx.EXPAND, 5 )


		columns_1_sizer.Add( instances_sizer, 2, wx.EXPAND, 5 )

		position_strategy_box_sizer = wx.BoxSizer( wx.VERTICAL )

		self.position_strategy_label = wx.StaticText( self, wx.ID_ANY, u"Positioning strategy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position_strategy_label.Wrap( -1 )

		position_strategy_box_sizer.Add( self.position_strategy_label, 0, wx.ALL, 5 )

		self.position_strategy = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position_strategy_relative = wx.Panel( self.position_strategy, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		position_strategy_relative_sizer = wx.BoxSizer( wx.VERTICAL )

		self.relative_anchor_label = wx.StaticText( self.position_strategy_relative, wx.ID_ANY, u"Select footprint to use as origin in each instance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.relative_anchor_label.Wrap( -1 )

		position_strategy_relative_sizer.Add( self.relative_anchor_label, 0, wx.ALL, 5 )

		relative_anchorChoices = []
		self.relative_anchor = wx.ListBox( self.position_strategy_relative, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, relative_anchorChoices, 0 )
		position_strategy_relative_sizer.Add( self.relative_anchor, 1, wx.ALL|wx.EXPAND, 5 )


		self.position_strategy_relative.SetSizer( position_strategy_relative_sizer )
		self.position_strategy_relative.Layout()
		position_strategy_relative_sizer.Fit( self.position_strategy_relative )
		self.position_strategy.AddPage( self.position_strategy_relative, u"Relative", True )
		self.position_strategy_grid = wx.Panel( self.position_strategy, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		position_strategy_grid_sizer = wx.FlexGridSizer( 0, 2, 0, 10 )
		position_strategy_grid_sizer.AddGrowableCol( 1 )
		position_strategy_grid_sizer.SetFlexibleDirection( wx.BOTH )
		position_strategy_grid_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.grid_flow_direction_label = wx.StaticText( self.position_strategy_grid, wx.ID_ANY, u"Flow direction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_flow_direction_label.Wrap( -1 )

		position_strategy_grid_sizer.Add( self.grid_flow_direction_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		grid_flow_directionChoices = [ u"Row", u"Column" ]
		self.grid_flow_direction = wx.Choice( self.position_strategy_grid, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, grid_flow_directionChoices, 0 )
		self.grid_flow_direction.SetSelection( 1 )
		position_strategy_grid_sizer.Add( self.grid_flow_direction, 0, wx.ALL, 5 )

		self.grid_wrap_label = wx.StaticText( self.position_strategy_grid, wx.ID_ANY, u"Wrapping", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_wrap_label.Wrap( -1 )

		position_strategy_grid_sizer.Add( self.grid_wrap_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.grid_wrap = wx.CheckBox( self.position_strategy_grid, wx.ID_ANY, u"Enable wrapping", wx.DefaultPosition, wx.DefaultSize, 0 )
		position_strategy_grid_sizer.Add( self.grid_wrap, 0, wx.ALL, 5 )

		self.grid_wrap_at_label = wx.StaticText( self.position_strategy_grid, wx.ID_ANY, u"Items per wrap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_wrap_at_label.Wrap( -1 )

		position_strategy_grid_sizer.Add( self.grid_wrap_at_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.grid_wrap_at = wx.SpinCtrl( self.position_strategy_grid, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		position_strategy_grid_sizer.Add( self.grid_wrap_at, 0, wx.ALL|wx.EXPAND, 5 )

		self.grid_main_interval_label = wx.StaticText( self.position_strategy_grid, wx.ID_ANY, u"Main-axis interval", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_main_interval_label.Wrap( -1 )

		position_strategy_grid_sizer.Add( self.grid_main_interval_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.grid_main_interval = wx.SpinCtrlDouble( self.position_strategy_grid, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1e+06, 0, 1 )
		self.grid_main_interval.SetDigits( 3 )
		position_strategy_grid_sizer.Add( self.grid_main_interval, 0, wx.ALL|wx.EXPAND, 5 )

		self.grid_cross_interval_label = wx.StaticText( self.position_strategy_grid, wx.ID_ANY, u"Cross-axis (wrap) interval", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_cross_interval_label.Wrap( -1 )

		position_strategy_grid_sizer.Add( self.grid_cross_interval_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.grid_cross_interval = wx.SpinCtrlDouble( self.position_strategy_grid, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1e+06, 0, 1 )
		self.grid_cross_interval.SetDigits( 3 )
		position_strategy_grid_sizer.Add( self.grid_cross_interval, 0, wx.ALL|wx.EXPAND, 5 )


		self.position_strategy_grid.SetSizer( position_strategy_grid_sizer )
		self.position_strategy_grid.Layout()
		position_strategy_grid_sizer.Fit( self.position_strategy_grid )
		self.position_strategy.AddPage( self.position_strategy_grid, u"Grid", False )

		position_strategy_box_sizer.Add( self.position_strategy, 1, wx.EXPAND |wx.ALL, 5 )


		columns_1_sizer.Add( position_strategy_box_sizer, 1, wx.EXPAND, 5 )


		rows_0_sizer.Add( columns_1_sizer, 1, wx.EXPAND, 5 )

		self.ok_button = wx.Button( self, wx.ID_ANY, u"Clone", wx.DefaultPosition, wx.DefaultSize, 0 )
		rows_0_sizer.Add( self.ok_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( rows_0_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.instances.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.instances_selection_toggle, id = wx.ID_ANY )
		self.instances.Bind( wx.dataview.EVT_DATAVIEW_ITEM_START_EDITING, self.instances_edit_veto, id = wx.ID_ANY )
		self.position_strategy.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.position_strategy_changed )
		self.relative_anchor.Bind( wx.EVT_LISTBOX, self.relative_anchor_changed )
		self.grid_flow_direction.Bind( wx.EVT_CHOICE, self.grid_flow_direction_changed )
		self.grid_wrap.Bind( wx.EVT_CHECKBOX, self.grid_wrap_changed )
		self.grid_wrap_at.Bind( wx.EVT_SPINCTRL, self.grid_wrap_at_changed )
		self.grid_main_interval.Bind( wx.EVT_SPINCTRLDOUBLE, self.grid_main_interval_changed )
		self.grid_cross_interval.Bind( wx.EVT_SPINCTRLDOUBLE, self.grid_cross_interval_changed )
		self.ok_button.Bind( wx.EVT_BUTTON, self.ok_button_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def instances_selection_toggle( self, event ):
		pass

	def instances_edit_veto( self, event ):
		pass

	def position_strategy_changed( self, event ):
		pass

	def relative_anchor_changed( self, event ):
		pass

	def grid_flow_direction_changed( self, event ):
		pass

	def grid_wrap_changed( self, event ):
		pass

	def grid_wrap_at_changed( self, event ):
		pass

	def grid_main_interval_changed( self, event ):
		pass

	def grid_cross_interval_changed( self, event ):
		pass

	def ok_button_click( self, event ):
		pass



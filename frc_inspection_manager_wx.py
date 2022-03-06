# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

ID_I_AVAILABLE = 1000
ID_I_PIT = 1001
ID_I_FIELD = 1002
ID_I_BREAK = 1003
ID_I_OFF = 1004
ID_I_PIT_RETURN = 1005
ID_T_CHECKIN = 1006
ID_T_WEIGHIN = 1007
ID_T_REINSPECT = 1008
ID_T_FINAL_WEIGHIN = 1009

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FRC Inspection Manager", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_file_open = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_file_open )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_help_about = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_help_about )

		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inspector_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.inspector_grid = wx.grid.Grid( self.inspector_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.inspector_grid.CreateGrid( 0, 3 )
		self.inspector_grid.EnableEditing( False )
		self.inspector_grid.EnableGridLines( True )
		self.inspector_grid.EnableDragGridSize( False )
		self.inspector_grid.SetMargins( 0, 0 )

		# Columns
		self.inspector_grid.EnableDragColMove( False )
		self.inspector_grid.EnableDragColSize( True )
		self.inspector_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.inspector_grid.EnableDragRowSize( True )
		self.inspector_grid.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.inspector_grid.SetRowLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.inspector_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.inspector_grid, 0, wx.ALL|wx.EXPAND, 5 )


		self.inspector_panel.SetSizer( bSizer2 )
		self.inspector_panel.Layout()
		bSizer2.Fit( self.inspector_panel )
		self.inspector_popup_menu = wx.Menu()
		self.m_i_inspector = wx.MenuItem( self.inspector_popup_menu, wx.ID_ANY, u"Inspector name", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_inspector )
		self.m_i_inspector.Enable( False )

		self.inspector_popup_menu.AppendSeparator()

		self.m_i_available = wx.MenuItem( self.inspector_popup_menu, ID_I_AVAILABLE, u"&Available", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_available )

		self.m_i_pit = wx.MenuItem( self.inspector_popup_menu, ID_I_PIT, u"Send to &pit for inspection", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_pit )

		self.m_i_field = wx.MenuItem( self.inspector_popup_menu, ID_I_FIELD, u"Going to &field", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_field )

		self.m_i_break = wx.MenuItem( self.inspector_popup_menu, ID_I_BREAK, u"Go on &break", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_break )

		self.m_i_off = wx.MenuItem( self.inspector_popup_menu, ID_I_OFF, u"&Off", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_off )

		self.inspector_popup_menu.AppendSeparator()

		self.m_i_pit_return = wx.MenuItem( self.inspector_popup_menu, ID_I_PIT_RETURN, u"Pit &return", wx.EmptyString, wx.ITEM_NORMAL )
		self.inspector_popup_menu.Append( self.m_i_pit_return )

		self.inspector_panel.Bind( wx.EVT_RIGHT_DOWN, self.inspector_panelOnContextMenu )

		self.m_notebook1.AddPage( self.inspector_panel, u"Inspectors", True )
		self.team_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.team_grid = wx.grid.Grid( self.team_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.team_grid.CreateGrid( 0, 2 )
		self.team_grid.EnableEditing( False )
		self.team_grid.EnableGridLines( True )
		self.team_grid.EnableDragGridSize( False )
		self.team_grid.SetMargins( 0, 0 )

		# Columns
		self.team_grid.EnableDragColMove( False )
		self.team_grid.EnableDragColSize( True )
		self.team_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.team_grid.EnableDragRowSize( True )
		self.team_grid.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.team_grid.SetRowLabelAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.team_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.team_grid, 0, wx.ALL|wx.EXPAND, 5 )


		self.team_panel.SetSizer( bSizer1 )
		self.team_panel.Layout()
		bSizer1.Fit( self.team_panel )
		self.team_popup_menu = wx.Menu()
		self.m_t_team = wx.MenuItem( self.team_popup_menu, wx.ID_ANY, u"team #", wx.EmptyString, wx.ITEM_NORMAL )
		self.team_popup_menu.Append( self.m_t_team )
		self.m_t_team.Enable( False )

		self.team_popup_menu.AppendSeparator()

		self.m_t_checkin = wx.MenuItem( self.team_popup_menu, ID_T_CHECKIN, u"&Check in"+ u"\t" + u"c", wx.EmptyString, wx.ITEM_CHECK )
		self.m_t_checkin.SetBitmap( wx.NullBitmap )
		self.team_popup_menu.Append( self.m_t_checkin )

		self.m_t_weighin = wx.MenuItem( self.team_popup_menu, ID_T_WEIGHIN, u"&Weigh In", wx.EmptyString, wx.ITEM_NORMAL )
		self.team_popup_menu.Append( self.m_t_weighin )

		self.m_t_reinspect = wx.MenuItem( self.team_popup_menu, ID_T_REINSPECT, u"&Reinspect", wx.EmptyString, wx.ITEM_NORMAL )
		self.team_popup_menu.Append( self.m_t_reinspect )

		self.m_t_final_weighin = wx.MenuItem( self.team_popup_menu, ID_T_FINAL_WEIGHIN, u"&Final weighin"+ u"\t" + u"f", wx.EmptyString, wx.ITEM_NORMAL )
		self.team_popup_menu.Append( self.m_t_final_weighin )

		self.team_panel.Bind( wx.EVT_RIGHT_DOWN, self.team_panelOnContextMenu )

		self.m_notebook1.AddPage( self.team_panel, u"Teams", False )

		bSizer11.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.my_on_close )
		self.inspector_grid.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_inspector_right_click )
		self.inspector_grid.Bind( wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.on_inspector_right_click )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_available.GetId() )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_pit.GetId() )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_field.GetId() )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_break.GetId() )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_off.GetId() )
		self.Bind( wx.EVT_MENU, self.on_i_context, id = self.m_i_pit_return.GetId() )
		self.team_grid.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_team_right_click )
		self.team_grid.Bind( wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.on_team_right_click )
		self.Bind( wx.EVT_MENU, self.on_t_context, id = self.m_t_checkin.GetId() )
		self.Bind( wx.EVT_MENU, self.on_t_context, id = self.m_t_weighin.GetId() )
		self.Bind( wx.EVT_MENU, self.on_t_context, id = self.m_t_reinspect.GetId() )
		self.Bind( wx.EVT_MENU, self.on_t_context, id = self.m_t_final_weighin.GetId() )
		self.Bind( wx.EVT_TIMER, self.on_timer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def my_on_close( self, event ):
		pass

	def on_inspector_right_click( self, event ):
		pass


	def on_i_context( self, event ):
		pass






	def on_team_right_click( self, event ):
		pass


	def on_t_context( self, event ):
		pass




	def on_timer( self, event ):
		pass

	def inspector_panelOnContextMenu( self, event ):
		self.inspector_panel.PopupMenu( self.inspector_popup_menu, event.GetPosition() )

	def team_panelOnContextMenu( self, event ):
		self.team_panel.PopupMenu( self.team_popup_menu, event.GetPosition() )


###########################################################################
## Class InspectionDialog
###########################################################################

class InspectionDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 384,348 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.inspectionDialogSizer = wx.BoxSizer( wx.VERTICAL )

		self.topSizer = wx.FlexGridSizer( 8, 2, 0, 0 )
		self.topSizer.AddGrowableCol( 1, 1 )
		self.topSizer.SetFlexibleDirection( wx.HORIZONTAL )
		self.topSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.robot_weight_label = wx.StaticText( self, wx.ID_ANY, u"Robot Weight", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.robot_weight_label.Wrap( -1 )

		self.topSizer.Add( self.robot_weight_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.robot_weight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.topSizer.Add( self.robot_weight, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )

		self.red_bumper_weight_label = wx.StaticText( self, wx.ID_ANY, u"<span foreground='red'>Red</span> Bumper Weight", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.red_bumper_weight_label.SetLabelMarkup( u"<span foreground='red'>Red</span> Bumper Weight" )
		self.red_bumper_weight_label.Wrap( -1 )

		self.red_bumper_weight_label.SetForegroundColour( wx.Colour( 250, 75, 56 ) )

		self.topSizer.Add( self.red_bumper_weight_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.red_bumper_weight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.red_bumper_weight.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.topSizer.Add( self.red_bumper_weight, 0, wx.ALL|wx.EXPAND, 5 )

		self.blue_bumper_weight_label = wx.StaticText( self, wx.ID_ANY, u"<span foreground='red'>Blue</span> Bumper Weight", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.blue_bumper_weight_label.SetLabelMarkup( u"<span foreground='red'>Blue</span> Bumper Weight" )
		self.blue_bumper_weight_label.Wrap( -1 )

		self.blue_bumper_weight_label.SetForegroundColour( wx.Colour( 78, 140, 203 ) )

		self.topSizer.Add( self.blue_bumper_weight_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.RIGHT, 5 )

		self.blue_bumper_weight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.blue_bumper_weight.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.topSizer.Add( self.blue_bumper_weight, 1, wx.ALL|wx.EXPAND, 5 )

		self.robot_weight_with_red_label = wx.StaticText( self, wx.ID_ANY, u"Robot + Red Bumper Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.robot_weight_with_red_label.Wrap( -1 )

		self.robot_weight_with_red_label.SetForegroundColour( wx.Colour( 250, 75, 56 ) )

		self.topSizer.Add( self.robot_weight_with_red_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.robot_weight_with_red = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.topSizer.Add( self.robot_weight_with_red, 0, wx.ALL|wx.EXPAND, 5 )

		self.robot_weight_with_blue_label = wx.StaticText( self, wx.ID_ANY, u"Robot + Blue Bumper Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.robot_weight_with_blue_label.Wrap( -1 )

		self.robot_weight_with_blue_label.SetForegroundColour( wx.Colour( 78, 140, 203 ) )

		self.topSizer.Add( self.robot_weight_with_blue_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.robot_weight_with_blue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.topSizer.Add( self.robot_weight_with_blue, 0, wx.ALL|wx.EXPAND, 5 )

		self.inspector_label = wx.StaticText( self, wx.ID_ANY, u"Inspector", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.inspector_label.Wrap( -1 )

		self.topSizer.Add( self.inspector_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		inspectorChoices = []
		self.inspector = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, inspectorChoices, 0 )
		self.inspector.SetSelection( 0 )
		self.topSizer.Add( self.inspector, 0, wx.ALL|wx.EXPAND, 5 )

		self.passed_label = wx.StaticText( self, wx.ID_ANY, u"Passed Inspection", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.passed_label.Wrap( -1 )

		self.topSizer.Add( self.passed_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		passedChoices = []
		self.passed = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, passedChoices, 0 )
		self.passed.SetSelection( 0 )
		self.topSizer.Add( self.passed, 0, wx.ALL|wx.EXPAND, 5 )

		self.comments_label = wx.StaticText( self, wx.ID_ANY, u"Comments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comments_label.Wrap( -1 )

		self.topSizer.Add( self.comments_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.comments = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.topSizer.Add( self.comments, 1, wx.ALL|wx.EXPAND, 5 )


		self.inspectionDialogSizer.Add( self.topSizer, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.inspectionDialogSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		buttonSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.ok_bottom = wx.Button( self, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.ok_bottom.SetDefault()
		buttonSizer.Add( self.ok_bottom, 0, wx.ALL, 5 )

		self.cancel_button = wx.Button( self, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonSizer.Add( self.cancel_button, 0, wx.ALL|wx.LEFT, 5 )


		self.inspectionDialogSizer.Add( buttonSizer, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( self.inspectionDialogSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ok_bottom.Bind( wx.EVT_BUTTON, self.on_OK_button )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_OK_button( self, event ):
		pass


###########################################################################
## Class TeamStatusFrame
###########################################################################

class TeamStatusFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FRC Inspection Manager Big Board", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )


		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.my_on_close )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def my_on_close( self, event ):
		pass


###########################################################################
## Class TeamStatusPanel
###########################################################################

class TeamStatusPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 240,83 ), style = wx.BORDER_DEFAULT, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.team_number = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.team_number.Wrap( -1 )

		self.team_number.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer1.Add( self.team_number, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.team_status = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.team_status.Wrap( -1 )

		gbSizer1.Add( self.team_status, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 2 )


		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 0 )

		self.SetSizer( gbSizer1 )
		self.Layout()

	def __del__( self ):
		pass



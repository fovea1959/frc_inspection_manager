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
import wx.aui

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
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.team_grid = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.team_grid.CreateGrid( 1, 2 )
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


		self.m_panel1.SetSizer( bSizer1 )
		self.m_panel1.Layout()
		bSizer1.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Teams", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.inspector_grid = wx.grid.Grid( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.inspector_grid.CreateGrid( 1, 2 )
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
		self.inspector_grid.SetRowLabelAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.inspector_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.inspector_grid, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Inspectors", False )

		bSizer11.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.my_on_close )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def my_on_close( self, event ):
		pass


###########################################################################
## Class Status
###########################################################################

class Status ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Status", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

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
## Class TeamStatus
###########################################################################

class TeamStatus ( wx.Panel ):

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


###########################################################################
## Class MainFrameAUI
###########################################################################

class MainFrameAUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_ALLOW_ACTIVE_PANE|wx.aui.AUI_MGR_DEFAULT|wx.aui.AUI_MGR_RECTANGLE_HINT|wx.aui.AUI_MGR_TRANSPARENT_DRAG)

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
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_notebook1, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.team_grid = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.team_grid.CreateGrid( 5, 5 )
		self.team_grid.EnableEditing( True )
		self.team_grid.EnableGridLines( True )
		self.team_grid.EnableDragGridSize( False )
		self.team_grid.SetMargins( 0, 0 )

		# Columns
		self.team_grid.EnableDragColMove( False )
		self.team_grid.EnableDragColSize( True )
		self.team_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.team_grid.EnableDragRowSize( True )
		self.team_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.team_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.team_grid, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer1 )
		self.m_panel1.Layout()
		bSizer1.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"a page", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.inspector_grid = wx.grid.Grid( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.inspector_grid.CreateGrid( 5, 5 )
		self.inspector_grid.EnableEditing( False )
		self.inspector_grid.EnableGridLines( False )
		self.inspector_grid.EnableDragGridSize( False )
		self.inspector_grid.SetMargins( 0, 0 )

		# Columns
		self.inspector_grid.EnableDragColMove( False )
		self.inspector_grid.EnableDragColSize( True )
		self.inspector_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.inspector_grid.EnableDragRowSize( True )
		self.inspector_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.inspector_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.inspector_grid, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"a page", False )


		self.m_mgr.Update()
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.my_on_close )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, override them in your derived class
	def my_on_close( self, event ):
		pass



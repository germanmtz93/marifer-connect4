from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Form1 import Form1


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(Form1(model_choice="CNN"))
    pass    

  def button_2_click(self, **event_args):
     """This method is called when the button is clicked"""
     open_form(Form1(model_choice="Transformer"))  # Open Form1 with Transformer model 
     pass

  def icon_button_1_click(self, **event_args):
    open_form('MainPage')
    pass
    
    

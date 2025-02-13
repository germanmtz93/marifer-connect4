from ._anvil_designer import DocumentationTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Documentation(DocumentationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def button_2_click(self, **event_args):
    open_form('MainPage')
    """This method is called when the component is clicked."""
    pass

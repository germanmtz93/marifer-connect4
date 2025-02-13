from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('Documentation')
    """This method is called when the component is clicked."""
    pass

  def button_2_click(self, **event_args):
    open_form('Form2')
    """This method is called when the component is clicked."""
    pass

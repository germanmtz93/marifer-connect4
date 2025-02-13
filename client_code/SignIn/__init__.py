from ._anvil_designer import SignInTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SignIn(SignInTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    user = anvil.users.login_with_form()
    if user:  # Check if a user logged in
        open_form('MainPage')  # Navigate to the HomePage form

  def sign_up_click(self, **event_args):
    """This method is called when the sign-up button is clicked"""
    user = anvil.users.login_with_form(sign_up=True)  # Open the sign-up form
    if user:  # Check if the sign-up was successful
        open_form('MainPage')  # Navigate to the Gamepage form
    pass

  def heading_1_show(self, **event_args):
    """This method is called when the component is shown on the screen."""
    pass

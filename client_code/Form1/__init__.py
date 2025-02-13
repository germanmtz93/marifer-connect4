from anvil import *
import anvil.server
from ._anvil_designer import Form1Template

class Form1(Form1Template):
    def __init__(self, model_choice="CNN", **properties):
        'Initialize the game, set up the board, and store the selected model choice.'
        self.init_components(**properties)
        self.model_choice = model_choice  
        self.board = [[0 for _ in range(7)] for _ in range(6)]  
        self.winning_discs = []  

        self.draw_board()
        
        # Hide buttons initially
        self.play_again_button.visible = False
        self.return_home_button.visible = False

        # Initialize turn indicator
        self.turn_indicator_label.text = "Your Turn"
        self.turn_indicator_label.role = "turn-box"

        print(f"Playing against: {self.model_choice}")

    def draw_board(self):
        'Draws the Connect 4 board and highlights the winning discs if any.'
        c = self.canvas_1
        rows, cols = 6, 7
        cell_size = 60  
        
        c.fill_style = '#4178B5'  
        c.fill_rect(0, 0, cols * cell_size, rows * cell_size)
        
        for row in range(rows):
            for col in range(cols):
                x = col * cell_size + cell_size // 2
                y = row * cell_size + cell_size // 2
                c.fill_style = '#FFFFFF'  
                c.begin_path()
                c.arc(x, y, cell_size // 3, 0, 2 * 3.1416)  
                c.fill()

                if self.board[row][col] == 1:
                    c.fill_style = '#E63946'  
                elif self.board[row][col] == -1:
                    c.fill_style = '#F4D35E'  

                if (row, col) in self.winning_discs:
                    c.shadow_blur = 10
                    c.shadow_color = "white"

                c.begin_path()
                c.arc(x, y, cell_size // 3, 0, 2 * 3.1416)
                c.fill()
                c.shadow_blur = 0  

    def canvas_1_mouse_down(self, x, y, **event_args):
        'Handles user clicks to drop a piece in the selected column.'
        if self.play_again_button.visible:  
            return  

        self.turn_indicator_label.text = "AI'S TURN !"  

        cell_size = 60
        col = int(x // cell_size)  
        if col < 0 or col > 6:  
            return

        for row in range(5, -1, -1):  
            if self.board[row][col] == 0:  
                self.board[row][col] = 1  
                self.draw_board()

                if self.check_winner():
                    return  

                self.play_ai_move()
                return  

    def play_ai_move(self):
        'Sends the board to the AI model and makes the AI move.'
        ai_col = anvil.server.call('get_ai_move', self.board, self.model_choice)  

        for row in range(5, -1, -1):
            if self.board[row][ai_col] == 0:
                self.board[row][ai_col] = -1  
                self.draw_board()

                if self.check_winner():
                    return  

                self.turn_indicator_label.text = "YOUR TURN!"  
                return  

    def check_winner(self):
        'Checks if there is a winner after each move and highlights the winning pieces.'
        rows, cols = 6, 7
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  
        self.winning_discs = []  

        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == 0:
                    continue  

                player = self.board[row][col]  
                
                for dr, dc in directions:
                    count = 1  
                    win_positions = [(row, col)]  

                    for i in range(1, 4):
                        r, c = row + dr * i, col + dc * i
                        if 0 <= r < rows and 0 <= c < cols and self.board[r][c] == player:
                            count += 1
                            win_positions.append((r, c))
                        else:
                            break  

                    if count >= 4:  
                        self.winning_discs = win_positions  
                        self.draw_board()  

                        if player == 1:
                            anvil.alert("Congratulations! You win! 🎉")
                        else:
                            self.show_ai_win_gif()  

                        self.show_endgame_options()  
                        return True

        return False  

    def show_ai_win_gif(self):
        'Displays a GIF when AI wins.'
        ai_win_gif = Image(source="_/theme/lost-the-game-and-you-just-lost-the-game.gif")  
        anvil.alert(content=ai_win_gif, title="AI wins! Better luck next time! 🤖", large=True)

    def show_endgame_options(self):
        'Shows buttons to play again or return to the main menu after a win.'
        self.play_again_button.visible = True
        self.return_home_button.visible = True

    def play_again_button_click(self, **event_args):
        'Resets the board for a new game.'
        self.reset_board()
        self.play_again_button.visible = False
        self.return_home_button.visible = False

    def main_menu_button_click(self, **event_args):
        'Returns to the main menu (HomeScreen).'
        open_form('Form2')

    def canvas_1_reset(self, **event_args):
        "This method is called when the canvas is reset and cleared."
        self.draw_board()

    def reset_board(self):
        'Clears the board for a new game.'
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.winning_discs = []  
        self.draw_board()
        self.turn_indicator_label.text = "Your Turn"  

    def return_home_button_click(self, **event_args):
        'Returns to the main menu.'
        open_form('Form2')

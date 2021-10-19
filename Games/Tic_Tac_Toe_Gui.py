#############################################################################
# Program : Tic Tac Toe game with Gui using Tkinter
# Author : Vinod H
# Date : 19/10/2021
#############################################################################

from tkinter import *



class Ttt_App:

    def __init__(self):
        # This is the list used to build the Tic Tac Toe board
        self.b = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        self.ret = 0
        self.flag = 1
        self.x = 0
        self.y = 40
        self.root = Tk()
        self.root.title('Tic Tac Toe')
        self.root.geometry('300x300')
        self.buttons()
        # Display Headline
        self.l1 = Label(text='First player will be\nX and second will be O ', width=30, bg='grey', font=('Times New '
                                                                                                         'Roman', 15))
        self.l1.place(anchor='center', relx=0.5, rely=0.25)
        self.display()
        self.root.mainloop()

    def dummy(self, choice, button):
        if self.ret in ['x', 'o', 'f']:
            self.l1.configure(text='Match already over, close this and\nRe-run the application to play again', bg='orange')
            return

        if self.b[choice] == 'X' or self.b[choice] == 'O' or button['text'] == 'X' or button['text'] == 'O':
            self.l1.configure(text='Already Key exist\nPlease try other keys')
        else:
            if self.flag == 1:
                self.b[choice] = 'X'
                button['text'] = 'X'
                self.flag = 0
                self.ret = self.board_check()
                if self.ret == 'x':
                    self.l1.configure(text='X has won the match\nCongratulations', bg='blue')
                    # time.sleep(5)
                    # self.l1.configure(text='Please re-run the application\nto play again')
                    # time.sleep(2)
                    # self.root.destroy()
                elif self.b.count('_') <= 1:
                    self.l1.configure(text='Match has a tie', bg='brown')
                    # time.sleep(3)
                    # self.l1.configure(text='Please re-run the application\nto play again')
                    # time.sleep(2)
                    # self.root.destroy()
            else:
                self.b[choice] = 'O'
                button['text'] = 'O'
                self.flag = 1
                self.ret = self.board_check()
                if self.ret == 'o':
                    self.l1.configure(text='O has won the match\nCongratulations', bg='red')
                    # time.sleep(3)
                    # self.l1.configure(text='Please re-run the application\nto play again')
                    # time.sleep(2)
                    # self.root.destroy()
                elif self.b.count('_') <= 1:
                    self.l1.configure(text='Match has a tie', bg='brown')
                    # time.sleep(3)
                    # self.l1.configure(text='Please re-run the application\nto play again')
                    # time.sleep(2)
                    # self.root.destroy()
        print(self.b)  # This is used to check and debug the backend logic from IDE output

    def buttons(self):
        root = self.root
        x = self.x
        y = self.y
        # This are buttons 7, 8 and 9
        button_7 = Button(root, text='7', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(7, button_7))
        button_7.place(x=x + 15, y=y + 100)

        button_8 = Button(root, text='8', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(8, button_8))
        button_8.place(x=x + 105, y=y + 100)

        button_9 = Button(root, text='9', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(9, button_9))
        button_9.place(x=x + 195, y=y + 100)

        # This are buttons 4, 5 and 6
        button_4 = Button(root, text='4', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(4, button_4))
        button_4.place(x=x + 15, y=y + 150)

        button_5 = Button(root, text='5', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(5, button_5))
        button_5.place(x=x + 105, y=y + 150)

        button_6 = Button(root, text='6', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(6, button_6))
        button_6.place(x=x + 195, y=y + 150)

        # This are buttons 1, 2 and 3
        button_1 = Button(root, text='1', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(1, button_1))
        button_1.place(x=x + 15, y=y + 200)

        button_2 = Button(root, text='2', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(2, button_2))
        button_2.place(x=x + 105, y=y + 200)

        button_3 = Button(root, text='3', height=2, width=10, padx=5, pady=5, command=lambda: self.dummy(3, button_3))
        button_3.place(x=x + 195, y=y + 200)

    def display(self):
        # Display output
        t = Label(self.root, text='Welcome to Tic Tac Toe Game', height=1, width=25, bg='grey',
                  font=('Times New Roman', 15))
        t.place(x=10, y=0)

    # This function is used to check whether any conditions met or not either for 'X' or 'O'
    def board_check(self):
        if self.b[1] == 'X' and self.b[2] == 'X' and self.b[3] == 'X' or self.b[4] == 'X' and self.b[5] == 'X' and \
                self.b[6] == 'X' or self.b[7] == 'X' and \
                self.b[8] == 'X' and self.b[9] == 'X' or self.b[7] == 'X' and self.b[4] == 'X' and self.b[1] == 'X' or \
                self.b[8] == 'X' and self.b[
            5] == 'X' and self.b[2] == 'X' or self.b[9] == 'X' and self.b[6] == 'X' and self.b[3] == 'X' or self.b[
            1] == 'X' and self.b[5] == 'X' and \
                self.b[9] == 'X' or self.b[7] == 'X' and self.b[5] == 'X' and self.b[3] == 'X':
            return 'x'
        elif self.b[1] == 'O' and self.b[2] == 'O' and self.b[3] == 'O' or self.b[4] == 'O' and self.b[5] == 'O' and \
                self.b[6] == 'O' or self.b[
            7] == 'O' and self.b[8] == 'O' and self.b[9] == 'O' or self.b[7] == 'O' and self.b[4] == 'O' and self.b[
            1] == 'O' or self.b[8] == 'O' and \
                self.b[5] == 'O' and self.b[2] == 'O' or self.b[9] == 'O' and self.b[6] == 'O' and self.b[3] == 'O' or \
                self.b[1] == 'O' and self.b[
            5] == 'O' and self.b[9] == 'O' or self.b[7] == 'O' and self.b[5] == 'O' and self.b[3] == 'O':
            return 'o'
        elif self.b.count('_') <= 1:
            return 'f'


if __name__ == '__main__':
    Ttt_App()

import tkinter

from src.Models.SecretCode import SecretCode
from src.Views.View import View
import tkinter as tk
import tkinter.messagebox as box
import src.Views.lang_pl as logs


def messagebox(title, text):
    """
    Static function for display popup

    Parameters
    ----------
    title: str
        Title for top label in window
    text: str
        Text to display in popup body
    """
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(title, text)
    root.destroy()


class DisplayResultWindow(object):

    def __init__(self, master):
        """
        Initialize window

        Parameters
        ----------
        master
            Master window
        """
        top = self.top = tkinter.Toplevel(master)
        top.geometry("390x230")
        self.master = master
        self.top.title(logs.lang['result_title'])
        self.result_title_frame = tk.Frame(top, bg="#dfdfdf")
        self.result_title_frame.grid(row=0, column=0, sticky=tk.EW)

        self.result_title = tk.Label(self.result_title_frame, text=logs.lang['result_label'], bg="#dfdfdf")
        self.result_title.pack()

        self.messages_area = tk.Canvas(top, width=450, height=100, background="#ffffff")
        self.messages_area.grid(row=1, column=0)

        master.withdraw()

    def display_results(self, list_of_winners: []):
        """
        Fill result on canvas
        """

        count = 1
        answers = []
        if len(list_of_winners) == 0:
            message = tk.Label(self.messages_area, width=55, background='#666565', text=logs.lang['no_results'])
            message.grid(row=0, column=0, sticky=tk.EW)
            return

        for winner in list_of_winners:
            text = f'{count}' + f'. Imie: {winner.get_name()}' \
                   + f'\tIlość prób: {winner.get_attempt()}' \
                   + f'\tData: {winner.get_date()}'
            answer = tk.Label(self.messages_area, width=55, background="#666565", text=text)
            answers.append(answer)
            count += 1
        count = 0
        for single in answers:
            if count == 10:
                break
            single.grid(row=count, column=0, sticky=tk.EW)
            count += 1


class InputUserNameWindow(object):
    """
    Class for display input for username for save records
    """
    def disable_event(self):
        pass

    def __init__(self, master, title: str):
        """
        Initialize window

        Parameters
        ----------
        master
            Master window
        title: str
            Title in label of window
        """
        top = self.top = tkinter.Toplevel(master)
        top.protocol("WM_DELETE_WINDOW", self.disable_event)
        top.geometry("250x80")
        self.master = master
        self.top.title(title)
        self.l = tkinter.Label(top, text="Wprowadź swoje imie")
        self.l.pack()
        self.e = tkinter.Entry(top)
        self.e.pack()
        self.b = tkinter.Button(top, text='OK', command=self.valid)
        self.b.pack()
        self.error = tkinter.Label(top, text="Wprowadź poprawne imie!", fg='#f00')
        master.withdraw()

    def valid(self):
        """
        Check input
        """
        if self.e.get() == "":
            self.error.pack()
        else:
            self.cleanup()

    def cleanup(self):
        """
        Destroy a window
        """
        self.value = self.e.get()
        self.top.destroy()


class TkinterView(View, tk.Frame):
    """
    A class for interaction with user in GUI
    """
    def __init__(self, parent):
        """
        Initialize main frame of window and assigns frame to main window of App.
        Run a methods to initialize a menu and list of answers

        Parameters
        ----------
        parent: App
            The main window of tkInter
        """
        super().__init__()
        tk.Frame.__init__(self, parent)
        self.count = 1
        self.answers = []

        self.init_left_side_menu()
        self.create_widgets()
        self.init_right_side_menu()
        self.init_status_bar()
        self.init_grids()

    def create_widgets(self):
        """
        Create a widgets in layout

        Fields
        ----------
        guess_code_lbl: tk.Label
            Label with invitation for user
        s_code_var: tk.StringVar
            place for code from user
        check_btn: tk.Button
            button to click with check the code
        reset_btn: tk.Button
            button for reset a game
        about_btn: tk.Button
            button for display about information
        manual_btn: tk.Button
            button for display manual(instructions) about game
        result_btn: tk.Button
            button for display archive result of game
        """
        # labels
        self.guess_code_lbl = tk.Label(self.menu_left_upper, text='Zgadnij kod:')
        self.guess_code_lbl.grid(row=0, columnspan=3, sticky=tk.NSEW)
        self.menu_left_upper.grid_columnconfigure(0, minsize=100, weight=1)
        self.menu_left_upper.grid_columnconfigure(2, weight=50)

        # entries
        self.s_code_var = tk.StringVar()
        self.s_code_ent = tk.Entry(self.menu_left_upper, textvariable=self.s_code_var, width=4)
        self.s_code_ent.grid(row=2, column=0, sticky=tk.NS, pady=10)

        # buttons
        self.check_btn = tk.Button(self.menu_left_upper, text='Sprawdź', command=lambda: self.check_button_clicked())
        self.check_btn.grid(row=2, column=1, padx=10)
        self.cheat_btn = tk.Button(self.menu_left_upper, text='Oszust', command=lambda: self.is_cheater())
        self.cheat_btn.grid(row=3, column=0, padx=10, pady=10)
        self.reset_btn = tk.Button(self.menu_left_upper, text='Reset', command=lambda: self.reset())
        self.reset_btn.grid(row=3, column=1, padx=10, pady=10)

        self.about_btn = tk.Button(self.menu_left_lower, text='O programie',
                                   command=lambda: box.showinfo('O programie', logs.lang['about']))
        self.about_btn.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.manual_btn = tk.Button(self.menu_left_lower, text='Instrukcja',
                                    command=lambda: box.showinfo('Instrukcja gry', logs.lang['manual']))
        self.manual_btn.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

        self.result_btn = tk.Button(self.menu_left_lower, text='Wyniki', command=lambda: self.__display_result(), width=10)
        self.result_btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    def init_left_side_menu(self):
        # left-side:
        """
        initialize left part of program

        Fields:
        menu_left: tk.Frame
            Frame for left part of menu
        menu_left_upper: tk.Frame
            Frame for upper side of menu left
        menu_left_lower: tk.Frame
            Frame for lower side of menu left
        """
        self.menu_left = tk.Frame(self, width=150, bg="#ababab")
        self.menu_left_upper = tk.Frame(self.menu_left, width=150, height=150, bg="red")
        self.menu_left_lower = tk.Frame(self.menu_left, width=150, height=20, bg="blue")

        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="bottom", fill="x", expand=False)

    def init_right_side_menu(self):
        """
        initialize right part of program

        Fields:
        some_title_frame: tk.Frame
            Frame for title with list of answers
        some_title: tk.Label
            Label for text with list of answers
        message_area: tk.Canvas
            Area for list of answers from program
        """
        # right area
        self.some_title_frame = tk.Frame(self, bg="#dfdfdf")

        self.some_title = tk.Label(self.some_title_frame, text="Lista odpowiedzi:", bg="#dfdfdf")
        self.some_title.pack()

        self.messages_area = tk.Canvas(self, width=350, height=100, background="#ffffff")
        self.messages_area.grid(row=1, column=1)

    def init_status_bar(self):
        """
        Status bar for errors and warnings message

        Fields:
        status_frame: tk.Frame
            frame for label with information
        status: Label
            label for information from program to user
        """
        # status bar
        self.status_frame = tk.Frame(self)
        self.status = tk.Label(self.status_frame, text="", foreground='red')
        self.status.pack(fill="both", expand=True)

    def init_grids(self):
        """
        Initialize grids.
        """
        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.some_title_frame.grid(row=0, column=1, sticky="ew")
        self.messages_area.grid(row=1, column=1, sticky="nsew")
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def answer(self, provide_code: SecretCode, count_correct_number, count_incorrect_position):
        text = f'{self.count}' + f'. Wprowadzona liczba: {provide_code}' \
               + f'\nLiczba cyfr poprawnie wprowadzonych: {count_correct_number}' \
               + f'\nLiczba cyfr na niepoprawnych pozycjach: {count_incorrect_position}'
        answer = tk.Label(self.messages_area, width=50, background="#666565", text=text)
        self.answers.append(answer)
        self.count += 1
        count = 0
        for single in self.answers:
            single.grid(row=count, column=0, sticky=tk.EW)
            count += 1

    def win(self):
        messagebox('Wygrałeś!', 'Moje gratulacje!')
        self.controller.save_winner()
        self.reset()

    def game_over(self):
        self.reset()
        messagebox('Przegrałeś.', 'Niestety nie udało się. Może następnym razem?')

    def check_button_clicked(self):
        if self.controller:
            self.controller.check_from_string(self.s_code_var.get())

    def reset(self):
        self.controller.reset()
        self.answers.clear()
        self.count = 1
        self.init_right_side_menu()
        self.init_grids()
        self.status['text'] = 'Zrestartowano grę'
        self.status.after(3000, self.__hide_error)

    def show_error(self, message):
        self.status['text'] = message
        self.status['foreground'] = 'red'
        self.status.after(3000, self.__hide_error)
        self.s_code_ent['foreground'] = 'red'

    def __hide_error(self):
        """
        Hide error
        :return:
        """
        self.status['text'] = ''
        self.s_code_ent['foreground'] = 'black'

    @staticmethod
    def _View__fair_game_message(secret_code: str):
        messagebox('Przegrałeś.', 'Tere fere. Wylosowany kod: ' + secret_code)

    @staticmethod
    def _View__cheat_game_message():
        messagebox('Wygrałeś!', 'Złapałeś/łaś mnie!')

    def provide_name(self, is_test=False):
        self.winner = InputUserNameWindow(self.master, "Wygrałeś")
        self.master.wait_window(self.winner.top)
        self.master.deiconify()
        if hasattr(self.winner, 'value'):
            return self.winner.value
        else:
            return "Anonymous"

    def __display_result(self):
        self.result_window = DisplayResultWindow(self.master)
        self.result_window.display_results(self.controller.get_results())
        self.master.wait_window(self.result_window.top)
        self.master.deiconify()


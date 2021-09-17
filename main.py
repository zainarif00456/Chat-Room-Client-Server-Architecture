#       In this program, we will write code for our project.
"""
        Project Title:  Chat Room Using Client-Server Architecture
        Team Members:
            Zain-Ul-Abdeen (BCSM-F19-154)
            M. Umair Anjum (BCSM-F19-030)
            Fida Hussain (BCSM-F19-128)
        Course: Computer Networks
        Project Type:   Network Programming
"""
from tkinter import *       #       Library for User Interface
class SignUp_Page(Tk):      #       Class of Sign up page.
    """
    This class contains the user interface of signup page of our chat room application.
    """


    def __init__(self):
        self.width = 650
        self.height = 400
        super().__init__()
        self.initialize_components()
    def initialize_components(self):
        """
        This function initialize the user interface of Sign up page.
        :return:
        """
        self.geometry("650x400")
        self.maxsize(self.width, self.height)
        self.minsize(self.width, self.height)
        self.title("Sign Up-Chat Room")
        self.config(bg="grey")


if __name__ == '__main__':
    sp = SignUp_Page()
    sp.mainloop()



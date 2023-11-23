import os
import webbrowser


def open_file(filename):
    webbrowser.open_new_tab(os.path.abspath(f'../draft/{filename}'))



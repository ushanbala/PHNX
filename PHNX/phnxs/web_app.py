import eel

def web_app(directory,html_file):
    eel.init(directory)

    eel.start(html_file)
import subprocess
import webbrowser
import eel


def Open():
    eel.init('web', allowed_extensions=['.js', '.html', '.css'])
    eel.start('html\EDER2.html')


@eel.expose
def Folder_Open(name):
    subprocess.Popen(["explorer", name], shell=True)

@eel.expose
def File_Open(name):
    subprocess.Popen(["start", name], shell=True)


if __name__ == '__main__':
    Open()
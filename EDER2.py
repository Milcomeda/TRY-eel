import subprocess
import webbrowser
import eel

def main():
    eel.init('web', allowed_extensions=['.js', '.html', '.css'])
    eel.start('html\EDER2.html')

@eel.expose
def link_click(name):
    # print('ok')
    # subprocess.Popen(["explorer", r"C:\Users\WAVE\Desktop\TRY"], shell=True)
    subprocess.Popen(["explorer", name], shell=True)

if __name__ == '__main__':
    main()
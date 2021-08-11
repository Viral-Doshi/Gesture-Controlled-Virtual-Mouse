import eel
from threading import Thread

class ChatBot:

    started = False

    def close_callback(route, websockets):
        if not websockets:
            print('Bye!')
            exit()

    @eel.expose
    def getUserInput(msg):
        print(msg)
    
    def addUserMsg(msg):
        eel.addUserMsg(msg)
    
    def addAppMsg(msg):
        eel.addAppMsg(msg)

    def start():
        eel.init('web', allowed_extensions=['.js', '.html'])
        try:
            eel.start('index.html', mode='chrome',
                                    host='localhost',
                                    port=27005,
                                    block=False,
                                    size=(350, 480),
                                    position=(10,100),
                                    disable_cache=True,
                                    close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while True:
                try:
                    eel.sleep(10.0)
                except:
                    #main thread exited
                    break
        except:
            pass
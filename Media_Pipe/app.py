import eel

class ChatBot:

    def close_callback(route, websockets):
        if not websockets:
            print('Bye!')
            exit()

    @eel.expose
    def getUserInput(msg):
        print(msg)
    
    def start():
        eel.init('web')
        try:
            eel.start('index.html', mode='chrome',
                                    host='localhost',
                                    port=27005,
                                    block=True,
                                    size=(350, 480),
                                    position=(10,100),
                                    disable_cache=True,
                                    close_callback=ChatBot.close_callback)
        
        except:
            pass

#ChatBot.start()
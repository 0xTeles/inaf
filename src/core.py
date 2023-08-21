import frida, time
from src.agent import iOS


def wordlistMode(process: str, wordlist: str, device: str):
    device = frida.get_device(device)
    session = device.attach(process)
    f = open(wordlist, "r")
    for w in f:
        deeplink = w.replace("\n", "")
        script = session.create_script(iOS(deeplink))
        initTime = time.process_time()
        print(f"[+] Loading: {deeplink}")
        script.load()
        script.unload()
        finishTime = time.process_time() - initTime
        print(f"\t[+] Opened in: {str(finishTime)[0:8]} seconds")
def oneMode(process: str, deeplink: str, device: str):
    device = frida.get_device(device)
    session = device.attach(process)
    script = session.create_script(iOS(deeplink))
    initTime = time.process_time()
    print(f"[+] Loading: {deeplink}")
    script.load()
    script.unload()
    finishTime = time.process_time() - initTime
    print(f"\t[+] Opened in: {str(finishTime)[0:8]} seconds")
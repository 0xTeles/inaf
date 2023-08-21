## inaf

The "Is Not a Fuzzer", inaf, is like a fuzzer to open deep-links on iOS devices. 


## Why

I've developed the **inaf** to personal use because during an hunting, I"ve noticed the app handle the requests incoming from deep links is different than requests incoming from manual actions. Through this insight, I could made reports and developed this code.


## How to use

To use inaf, you need to install **frida** through ```pip3 install frida```. 

After the installation, you need to:

- Setup frida server in your device;
- Pair your device with idevicepair pair {ios only}. 

And then, you can use the code:

```
$ python3 inaf.py
usage: inaf.py [-h] --process <process> [--wordlist <wordlist>] --device <device> [--deeplink <deeplink>]

Inaf - Is not a Fuzzer

optional arguments:
  -h, --help            show this help message and exit
  --process <process>   Name of process to attach
  --wordlist <wordlist>
                        Wordlist contains deeplinks to open
  --device <device>     Id of device to attach
  --deeplink <deeplink>
                        Deeplink to open
```
## References

- https://gist.github.com/konsumer/373eb18dabd55b931f2087bbe7f891d1/
- https://github.com/frida

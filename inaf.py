import argparse
from src.core import *
parser = argparse.ArgumentParser(description="Inaf - Is not a Fuzzer")
parser.add_argument('--process', metavar='<process>', required=True, type=str,help='Name of process to attach')
parser.add_argument('--wordlist', metavar='<wordlist>', required=False, type=str,help='Wordlist contains deeplinks to open')
parser.add_argument('--device', metavar='<device>', required=True, type=str,help='Id of device to attach')
parser.add_argument('--deeplink', metavar='<deeplink>', required=False, type=str,help='Deeplink to open')

args = parser.parse_args()

if (args.deeplink == None):
    wordlistMode(args.process, args.wordlist, args.device)
elif (args.wordlist == None):
    oneMode(args.process, args.deeplink, args.device)
else:
    parser.print_help()
from subprocess import Popen
import time, datetime, json, platform, requests, sched, sys, argparse
from os import listdir
from os.path import isfile, join

# print(datetime.datetime.now())

event_schedule = sched.scheduler(time.time, time.sleep)

parser = argparse.ArgumentParser()
parser.add_argument("--exe-path", "-e")
parser.add_argument("--api-url", "-a")

args = parser.parse_args()
# print(args)

if args.api_url == None or args.api_url == None:
    print("command-line arguments were not passed. Please provide --exe-path and --api-url")
    exit()


def processJsonOutputs():

    print(datetime.datetime.now())

    exePath = args.exe_path
    # "C:/Users/sonaw/Documents/Intel/OpenVINO/omz_demos_build/intel64/Debug"
    apiUrl = args.api_url
    # "http://127.0.0.1:3900/api/asset/add"
    printingPath = exePath + "/printing"
    printingFiles = [f for f in listdir(printingPath) if isfile(join(printingPath, f))]

    for p in printingFiles:
        filePath = printingPath + "/" + p
        print("Currently processing: % s" % filePath)
        fileText = open(filePath).read()
        jsonData = json.loads(fileText)
        print("---=== Sending request payload with data ===---")
        print(jsonData)

        # call our oculus server api with this json data.

        try:
            response = requests.post(apiUrl, json=jsonData)
            # responseJson = response.json()
            if response.status_code == 400 or response.status_code == 500:
                print("---=== Response message ===---")
                print(response.text)   
                print("File % s was not processed." % p)               
            if response.status_code == 200:
                print("---=== Response message ===---")
                print("File % s processed successfully!." % p)
                responseJson = response.json()
                print(responseJson.message)                
        except ConnectionError:
            print("---=== Exception message ===---")            
            print("Connection error!.")            
        except Exception:
            print("---=== Exception message ===---")
            print("Unknown exception occurred!.")

        print("-------------------===========================--------------------")   
        # finally:
        # print("Unhandled exception occurred!.")

    print("Continue execution?. Will wait for 180 seconds to resume. Press CTRL+C to exit the execution.")
    event_schedule.enter(180, 1, processJsonOutputs)


""" if platform.system() == "Windows":
    Popen("run-commands.bat " + args.exe_path + " printing")
if platform.system() == "Linux":
    Popen("run-commands.sh")
 """

# print("Scanning folder at: " + time.ctime())

event_schedule.enter(10, 1, processJsonOutputs)
event_schedule.run()

import json
from Converter import Convert

def Init():
    print("Powered by RunPX - A library for running PortexJSON code on the go programmatically inside Python")
    converter = Converter.Convert()

def Run(json):
    print("Running the PortexJSON array of " + json)

    ProperDict = json.loads(json)
    print("Converted PortexJSON string array to a proper python dictionary")

    Transpiled = converter.Transpile(ProperDict)
    print("Transpiled the dictionary to python code succesfully")

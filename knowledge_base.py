# File to handle knowledge base creation; currently set to write to a .pl file
from pyswip import Prolog
import pandas as pd
import re


def kb_declare():  # Function to create the knowledge base from the .csv file
    knowledge = pd.read_csv('Dataset_Cell_Phones_Model_Brand.csv')  # Load into pandas df
    pd.options.display.max_rows = None  # Debugging option

    with open('knowledge_base.pl', 'w') as f:
        for row in knowledge.itertuples():
            if isinstance(row[7], str) and isinstance(row[12], str):
                entry = '\'' + row[7].replace('\'', '') + row[12].replace('\'', '') + '\''  # Entries are a
                # combination of the model and brand
                brand = '\'' + row[7].replace('\'', '') + '\''  # Brand is its own fact about a model we would want
                # to let the user query
                f.write("phone(" + entry + ").\n") # Write the format to .pl file. Will use pyswip in final
                f.write("brand(" + entry + "," + brand + ").\n")
            else:
                continue

            storage = row[5]  # Begin handling storage section
            if isinstance(storage, str):  # Make sure we do not receive nan
                match = re.search("((\d+)?/?)+\s*([gm]b)?|\d+\s*([gm]b)?\s*/\d+\s*([gm]b)?", storage.lower())
                if match:
                    if len(match.group(0).split("/")) > 1:
                        for storage_size in match.group(0).split("/"):
                            if "mb".lower() in storage.lower():
                                storage_size = storage_size.split(" ")[0]
                                storage_size = float(storage_size) / 1024
                                f.write("storage(" + entry + "," + str(storage_size) + ").\n")
                                Prolog.assertz("storage(" + entry + "," + str(storage_size) + ")")
                            elif "gb".lower() in storage.lower():
                                storage_size = storage_size.split(" ")[0]
                                f.write("storage(" + entry + "," + storage_size + ").\n")
                                Prolog.assertz("storage(" + entry + "," + storage_size + ")")
                    else:
                        if "mb".lower() in storage.lower():
                            storage = storage.split(" ")[0]
                            storage = float(storage) / 1024
                            f.write("storage(" + entry + "," + str(storage) + ").\n")
                            Prolog.assertz("storage(" + entry + "," + str(storage) + ")")
                        elif "gb".lower() in storage.lower():
                            storage = storage.split(" ")[0]
                            f.write("storage(" + entry + "," + storage + ").\n")
                            Prolog.assertz("storage(" + entry + "," + str(storage) + ")")

            ram = row[43]  # Handle ram
            if isinstance(ram, str):
                match = re.findall("\d+/?\d* [gm]b ram", ram.lower())
                if match:
                    for m in match:
                        for e in m.split("/"):
                            if "mb" in m.lower():
                                ram = e.split(" ")[0]
                                ram = float(ram) / 1024
                                f.write("ram(" + entry + "," + str(ram) + ").\n")
                                Prolog.assertz("ram(" + entry + "," + str(ram) + ")")
                            elif "gb".lower() in m.lower():
                                ram = e.split(" ")[0]
                                f.write("ram(" + entry + "," + str(ram) + ").\n")
                                Prolog.assertz("ram(" + entry + "," + str(ram) + ")")

            cpu = row[8]  # Handle CPU
            if isinstance(cpu, str):
                match = re.search("(\d+\.?\d*)\s*[gm]hz", cpu.lower())
                if match:
                    if "mhz" in match.group(0).lower():
                        cpu = match.group(1).split(" ")[0]
                        cpu = float(cpu) / 1000
                        f.write("cpu(" + entry + "," + str(cpu) + ").\n")
                        Prolog.assertz("cpu(" + entry + "," + str(cpu) + ")")
                    elif "ghz" in match.group(0).lower():
                        cpu = match.group(1).split(" ")[0]
                        f.write("cpu(" + entry + "," + cpu + ").\n")
                        Prolog.assertz("cpu(" + entry + "," + str(cpu) + ")")



            camera = row[3]
            if isinstance(camera, str):
                match = re.search("(\d+\.*\d*)\s*mp", camera.lower())
                if match:
                    camera = match.group(1)
                    f.write("camera(" + entry + "," + str(camera) + ").\n")
                    Prolog.assertz("camera(" + entry + "," + str(camera) + ")")
                else:
                    camera = 0
                    f.write("camera(" + entry + "," + str(camera) + ").\n")
                    Prolog.assertz("camera(" + entry + "," + str(camera) + ")")

            usb = row[6]  # Handle usb

            bluetooth = row[23]

            if isinstance(bluetooth, str):
                if "no".lower() in bluetooth.lower():
                    bluetooth = "no"
                    f.write("bluetooth(" + entry + "," + bluetooth + ").\n")
                    Prolog.assertz("bluetooth(" + entry + "," + bluetooth + ")")
                else:
                    bluetooth = "yes"
                    f.write("bluetooth(" + entry + "," + bluetooth + ").\n")
                    Prolog.assertz("bluetooth(" + entry + "," + bluetooth + ")")

            gps = row[14]  # Handle GPS
            if isinstance(gps, str):
                if "yes".lower() in gps.lower():
                    gps = "yes"
                    f.write("gps(" + entry + "," + gps + ").\n")
                    Prolog.assertz("gps(" + entry + "," + gps + ")")
                else:
                    gps = "no"
                    f.write("gps(" + entry + "," + gps + ").\n")
                    Prolog.assertz("gps(" + entry + "," + gps + ")")


    # print(list(Prolog.query("bluetooth(X, no)")))

    # Begin rule declaration

    Prolog.assertz("good_cpu(X) :- " 
                   "cpu(X, Value), "
                   "Value >= 1")
    Prolog.assertz("choose_cpu(X, Y) :- "
                   "cpu(X, Value), "
                   "Value >= Y")
    Prolog.assertz("good_ram(X) :- "
                   "ram(X, Value), "
                   "Value >= 1")
    Prolog.assertz("choose_ram(X, Y) :- "
                   "ram(X, Value), "
                   "Value >= 6")
    Prolog.assertz("choose_camera(X, Y) :- "
                   "camera(X, Value), "
                   "Value >= Y")
    Prolog.assertz("high-end(X) :- "
                   "good_cpu(X), "
                   "good_ram(X), "
                   "choose_camera(X, 1)")
    #Prolog.assertz("modern(X) :- "
    #               "high-end(X), ")
    print(list(Prolog.query("high-end(X)")))

            # length = row[]  # Handle device dimensions
            # height = row[]
            # width = row[]

            # availability = row[]


            # Begin rule construction

def kb_load():  # Function to consult constructed knowledge in existing Prolog file.
    Prolog.consult('knowledge_base.pl')

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
                Prolog.assertz("phone(" + entry + ")")
                f.write("brand(" + entry + "," + brand + ").\n")
                Prolog.assertz("brand(" + entry + "," + brand + ")")
            else:
                continue

            storage = row[5]  # Begin handling storage section
            if isinstance(storage, str):  # Make sure we do not receive nan
                match = re.search("((\d+)?/?)+\s*([gm]b)?|\d+\s*([gm]b)?\s*/\d+\s*([gm]b)?", storage.lower())
                # Regex to search the entries for the correct storage parameters and convert to storable format
                if match: # If we find the pattern
                    if len(match.group(0).split("/")) > 1: # Split the storage options from each other and insert into
                        # the KB
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
                    else: # If there's only one option
                        if "mb".lower() in storage.lower():
                            storage = storage.split(" ")[0]
                            storage = float(storage) / 1024
                            f.write("storage(" + entry + "," + str(storage) + ").\n")
                            Prolog.assertz("storage(" + entry + "," + str(storage) + ")")
                        elif "gb".lower() in storage.lower():
                            storage = storage.split(" ")[0]
                            f.write("storage(" + entry + "," + storage + ").\n")
                            Prolog.assertz("storage(" + entry + "," + str(storage) + ")")

            ram = row[43]  # Handle ram and input into KB
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

            cpu = row[8]  # Handle CPU and input into KB
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



            camera = row[3]  # Handle camera and input into KB
            if isinstance(camera, str):
                match = re.search("(\d+\.*\d*)\s*mp", camera.lower())
                if match:
                    camera = match.group(1)
                    f.write("camera(" + entry + "," + str(camera) + ").\n")
                    Prolog.assertz("camera(" + entry + "," + str(camera) + ")")
                else:  # Any entry without a MP listing will be assumed to have no camera functionality
                    camera = 0
                    f.write("camera(" + entry + "," + str(camera) + ").\n")
                    Prolog.assertz("camera(" + entry + "," + str(camera) + ")")


            bluetooth = row[23] # Handle bluetooth

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
                    f.write("gps(" + entry + ").\n")
                    Prolog.assertz("gps(" + entry + ")")
                else:
                    gps = "no"
                    f.write("gps(" + entry + "," + gps + ").\n")
                    Prolog.assertz("gps(" + entry + "," + gps + ")")

            volume = row[20]  # Handle device dimensions
            if isinstance(volume, str):
                match = re.search("\((\d+\.*\d*) *x *(\d+\.*\d*) *x *(\d+\.*\d*) in\)", volume.lower())
                if match:
                    length = match.group(1)
                    height = match.group(2)
                    width = match.group(3)
                    if isinstance(length, str) and isinstance(height, str) and isinstance(width, str):
                        f.write("dimensions( " + entry + "," + length + "," + height + "," + width + ").\n")
                        Prolog.assertz("dimensions( " + entry + "," + length + "," + height + "," + width + ")")

            resolution = row[10] # Handle screen size/resolution (it says resolution in the dataset but it's size)
            if isinstance(resolution, str):
                match = re.search("(\d+\.*\d*)\s*inches", resolution.lower())
                if match:
                    screen_size = match.group(1)
                    if isinstance(screen_size, str):
                        f.write("screen_size(" + entry + "," + screen_size + ")\n")
                        Prolog.assertz("screen_size(" + entry + "," + screen_size + ")")

    # Begin rule declaration; many rules are utilized in other rules (particularly the greater/lesser selection rules)
    #   to constrain their results.

    Prolog.assertz("good-cpu(X) :- "
                   "phone(X),"
                   "cpu(X, Value), "
                   "Value >= 1")
    Prolog.assertz("greater-cpu(X, Y) :- "
                   "phone(X),"
                   "cpu(X, Value), "
                   "Value >= Y")
    Prolog.assertz("lesser-cpu(X, Y) :- "
                   "phone(X),"
                   "cpu(X, Value), "
                   "Value < Y")
    Prolog.assertz("good-ram(X) :- "
                   "phone(X),"
                   "ram(X, Value), "
                   "Value >= 1")
    Prolog.assertz("greater-ram(X, Y) :- "
                   "phone(X),"
                   "ram(X, Value), "
                   "Value >= Y")
    Prolog.assertz("lesser-ram(X, Y) :- "
                   "phone(X),"
                   "ram(X, Value), "
                   "Value < Y")
    Prolog.assertz("greater-storage(X, Y) :-"
                   "phone(X),"
                   "storage(X, Value), "
                   "Value >= Y")
    Prolog.assertz("lesser-storage(X, Y) :- "
                   "phone(X),"
                   "storage(X, Value), "
                   "Value < Y")
    Prolog.assertz("greater-width(X, Y) :- "
                   "phone(X),"
                   "dimensions(X, Length, Height, Width), "
                   "Width >= Y")
    Prolog.assertz("lesser-width(X, Y) :- "
                   "phone(X),"
                   "dimensions(X, Length, Height, Width), "
                   "Width < Y")
    Prolog.assertz("greater-screen(X, Y) :- "
                   "phone(X),"
                   "screen_size(X, Value), "
                   "Value >= Y")
    Prolog.assertz("lesser-screen(X, Y) :- "
                   "phone(X),"
                   "screen_size(X, Value), "
                   "Value < Y")
    Prolog.assertz("greater-camera(X, Y) :- "
                   "phone(X),"
                   "camera(X, Value), "
                   "Value >= Y")
    Prolog.assertz("lesser-camera(X, Y) :- "
                   "phone(X),"
                   "camera(X, Value), "
                   "Value < Y")
    Prolog.assertz("multimedia(X) :-"
                   "phone(X),"
                   "greater-camera(X, 10), "
                   "greater-storage(X, 24)")
    Prolog.assertz("high-end(X) :- "
                   "phone(X),"
                   "good-cpu(X), "
                   "good-ram(X), "
                   "greater-camera(X, 5)")
    Prolog.assertz("modern(X) :- "
                   "high-end(X), "
                   "lesser-width(X, 0.5), "
                   "greater-storage(X, 16)")
    Prolog.assertz("old-school(X) :- "
                   "phone(X), "
                   "gps(X, no), "
                   "greater-width(X, 0.6), "
                   "lesser-ram(X, 2), "
                   "lesser-cpu(X, 1)")



def kb_load():  # Function to consult constructed knowledge in existing Prolog file.
    Prolog.consult('knowledge_base.pl')

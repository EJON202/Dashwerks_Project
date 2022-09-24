from fileinput import close
import dashwerks as dw

fn = "exampleArduinoData.txt"
BLUE_RPM = 400

entry_number = 1
with open(fn,"r") as file:
    ln = file.readline()
    sd = dw.SystemData(entry_number, ln)

    if sd.get_rpm() <= BLUE_RPM:
        # add somthing to light up somthing..
        print("Blue")
    else:
        print("Flass Red RPM!!")


# 🔹 Task 6: Read a Log File and Extract Errors
# 🔹 Write a Python script that:

# Reads a log file ("server.log").
# Extracts and saves only the error messages to a new file "errors.log".


#read the server file
readServerFile = open("server.log","r")
textofServerFile = readServerFile.readlines()
readServerFile.close()

#create error.log file to save the errors
errorFile = open("error.log","w")
for line in textofServerFile:
    
    if "error" in line.lower():
        errorFile.write(line)

errorFile.close()
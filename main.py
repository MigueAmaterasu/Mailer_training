from app.director import GoProcess

print("START PROCESS")

print("FILE DONWLOADING")
GoProcess().getFile()
print("SUCCESSFULL")

print("Reading CSV file")
GoProcess().getDataCv()
print("Read CSV file ")

print("Reading Database")
GoProcess().getDataDb()
print("Read Database")

print("Finding Differences")
GoProcess().getDataFailet()
print("Differences found")

print("Sending Email")
GoProcess().getEmail()
print("Email sent")

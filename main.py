from app.director import GoProcess

print("Inicio de procesos de esta pagina")

print("Reading CSV file")
# GoProcess().getDataCv()
print("Read CSV file ")

print("Reading Database")
# GoProcess().getDataDb()
print("Read Database")

print("Finding Differences")
GoProcess().getDataFailet()
print("Differences found")

print("Sending Email")
GoProcess().getEmail()
print("Email sent")

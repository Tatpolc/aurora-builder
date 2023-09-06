from main import c

#create/open airport
apt_file = open("C:\\Project\\Aurora-Builder\\output\\VTBB.apt", "w")

c.execute("""SELECT ident, altitude, transition_altitude, laty, lonx, name
    FROM airport
    WHERE region = "VT"
    """)

airport = c.fetchall()

for item in airport:
    apt_file.write(item[0]+';'+str(item[1])+';'+str(item[2])+';'+str(item[3])+';'+str(item[4])+';'+str(item[5])+';\n')
    print('File created successfully!')
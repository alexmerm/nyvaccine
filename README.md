So what you have to do ian:

is basically copy everything from cvsChecker.py (both functions and the imports) into cvsAutoChecker.py

getCvsStatus()  returns 2 values : asOfTime (the time the results are accurate as of according to CVS website, I can help u format that later) and cities, an array of dicts that have info on every CVS in NY, see below for example of it

, you can call it by using `asOfTime,cities = getCvsStatus()`

You have to implmenet this into the cvsAutoChecker.py, which is currently just a copy of the ny system in nystatechecker.py, basically most of the code ur modifying is in the main, if u have questions ask me but its should be sort of strait forward


Its curr using a remote selenium the IP i put in rn is runnning on a raspberry pi but I'll compile it into a docker container (again u dont need to know what that is) that will run it every 5 min or smth

## and finally: to get everything setup:
```bash
cd into this directory (or open the directory in vs code)
type in pip install -r requirements.txt
```

cities dict:
```
[{'city': 'ALBANY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'AMHERST', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'AMITYVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'AMSTERDAM', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ARDSLEY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ARMONK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ASTORIA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'AUBURNDALE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'AVON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BALDWIN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BARDONIA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BATAVIA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BAY SHORE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BAYSIDE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BEDFORD HILLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BELLEROSE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BELLMORE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BETHPAGE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BINGHAMTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BLASDELL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BOHEMIA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BRIARCLIFF MANOR', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BROCKPORT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BRONX', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BRONXVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BROOKLYN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BUFFALO', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'BURNT HILLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CAIRO', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CAMBRIA HEIGHTS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CARMEL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CEDARHURST', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CENTER MORICHES', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CENTEREACH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CENTRAL ISLIP', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CHEEKTOWAGA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CHESTER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CICERO', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CLIFTON PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CLINTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'COBLESKILL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'COLONIE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'COMMACK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'COOPERSTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'COPIAGUE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CORAM', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CORNWALL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CORTLAND', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'CROTON ON HUDSON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'DANSVILLE', 'state': 'NY', 'status': 'Available'},
 {'city': 'DEER PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'DELMAR', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'DEPEW', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'DOVER PLAINS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'DUNKIRK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EAST GREENBUSH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EAST HAMPTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EAST HILLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EAST NORTHPORT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EAST ROCKAWAY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'EASTCHESTER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ELMIRA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ELMONT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ELMSFORD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ENDICOTT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ENDWELL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FAIRPORT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FALCONER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FARMINGDALE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FARMINGVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FAYETTEVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FLORAL PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FRANKLIN SQUARE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'FREEPORT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GARNERVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GLEN COVE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GLEN HEAD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GLENVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GLOVERSVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GOSHEN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GREAT NECK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GREECE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GREENWICH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'GREENWOOD LAKE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HAMBURG', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HARRISON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HEWLETT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HILTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HONEOYE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HUDSON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HUDSON FALLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HUNTINGTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'HYDE PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'INWOOD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ISLIP TERRACE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ITHACA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'JACKSON HEIGHTS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'JAMAICA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'JAMESTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'JOHNSON CITY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'KATONAH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'KINGS PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'KINGSTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LARCHMONT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LATHAM', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LEVITTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LEWISTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LITTLE FALLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LIVERPOOL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LONG BEACH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LONG ISLAND CITY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'LYNBROOK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MAMARONECK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MANORVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MARGARETVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MATTITUCK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MEDFORD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MIDDLE VILLAGE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MIDDLETOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MILLERTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MINEOLA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MONROE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'MOUNT VERNON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEW CITY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEW HARTFORD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEW HYDE PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEW ROCHELLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEW YORK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NEWBURGH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NIAGARA FALLS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTH BABYLON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTH BALDWIN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTH BAY SHORE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTH BELLMORE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTH TONAWANDA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'NORTHPORT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'OCEANSIDE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'OLEAN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ORANGEBURG', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ORCHARD PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'OSSINING', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'OWEGO', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'OYSTER BAY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PATCHOGUE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PAWLING', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PEEKSKILL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PENFIELD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PENN YAN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PORT JEFFERSON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'PORT JEFFERSON STATION', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'POUGHKEEPSIE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'QUEENS VILLAGE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'QUEENSBURY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RED HOOK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RENSSELAER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RHINEBECK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RIVERHEAD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ROCHESTER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ROCKAWAY BEACH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'ROCKVILLE CENTRE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RONKONKOMA', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RYE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'RYE BROOK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SANBORN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SARATOGA SPRINGS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SAUGERTIES', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SCARSDALE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SCHENECTADY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SELDEN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SETAUKET', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SHIRLEY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SKANEATELES', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SMITHTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SOUTH SETAUKET', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SOUTHAMPTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'STATEN ISLAND', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'STONY POINT', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SUFFERN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'SYRACUSE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'TARRYTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'THORNWOOD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'TROY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'VALATIE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'VALLEY STREAM', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'VESTAL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'VICTOR', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WADING RIVER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WALTON', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WASHINGTONVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WATERTOWN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WATERVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WATKINS GLEN', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WAYLAND', 'state': 'NY', 'status': 'Available'},
 {'city': 'WEBSTER', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WEST HEMPSTEAD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WEST ISLIP', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WEST NYACK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WEST SAYVILLE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WESTBURY', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WESTFIELD', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WESTHAMPTON BEACH', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WHITE PLAINS', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WHITESTONE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WILLISTON PARK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WOODMERE', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WOODSTOCK', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'WYNANTSKILL', 'state': 'NY', 'status': 'Fully Booked'},
 {'city': 'YONKERS', 'state': 'NY', 'status': 'Fully Booked'}]
```


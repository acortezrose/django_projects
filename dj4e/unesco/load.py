import csv

from unesco.models import Site, Category, States, Region, ISO

Category.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
ISO.objects.all().delete()
Site.objects.all().delete()

fh = open('unesco/whc-sites-2018-small.csv')
rows = csv.reader(fh)
i = 0
for row in rows:
	if i > 0:
		if len(row[0]) < 1 : continue
	    # print("NAME", row[0])
	    # print("DESCRIP", row[1])
	    # print("JUST", row[2])
	    # print("YEAR", row[3])
	    # print("LONG", row[4])
	    # print("LAT", row[5])
	    # print("HECTARES", row[6])
	    # print("CATEGORY", row[7])
	    # print("STATES", row[8])
	    # print("REGION", row[9])
	    # print("ISO", row[10])

		try:
			y = row[3]
		except:
			y = None

		try:
			lon = float(row[4])
		except:
			lon = None

		try:
			lat = float(row[5])
		except:
			lat = None

		try:
			ah = float(row[6])
		except:
			ah = None

		try: 
			cat = Category.objects.get(name=row[7])
		except: 
			print("New category", row[7])
			cat = Category(name=row[7])
			cat.save()

		try: 
			st = States.objects.get(name=row[8])
		except: 
			print("New states", row[8])
			st = States(name=row[8])
			st.save()

		try: 
			reg = Region.objects.get(name=row[9])
		except: 
			print("New region", row[9])
			reg = Region(name=row[9])
			reg.save()

		try: 
			io = ISO.objects.get(name=row[10])
		except: 
			print("New iso", row[10])
			io = ISO(name=row[10])
			io.save()

		s = Site(name=row[0], description=row[1], justification=row[2],
			year=y, longitude=lon, latitude=lat, 
			area_hectares=ah, category=cat, states=st, region=reg,
			iso=io)
		s.save()	


	i = i + 1
	# if i > 5 : break
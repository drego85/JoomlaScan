all:

clean:

install:
	chmod 755 joomlascan.py
	chmod 755 joomlascan
	chmod 644 comptotestdb.txt
	chown root:root joomlascan.py
	chown root:root joomlascan
	chown root:root comptotestdb.txt
	mkdir -p $(DESTDIR)/usr/share/joomlascan
	mkdir -p $(DESTDIR)/usr/bin
	cp joomlascan $(DESTDIR)/usr/bin/joomlascan
	cp joomlascan.py $(DESTDIR)/usr/share/joomlascan/joomlascan.py
	cp comptotestdb.txt $(DESTDIR)/usr/share/joomlascan/comptotestdb.txt


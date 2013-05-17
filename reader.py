#**************************************************************
# import all the necessary libraries
#**************************************************************

# library for creating/workingwith/writing to/parsing CSV files.  We're outputting to CSV
import csv

# use to create directories
import os

# regular expressions
import re

# opening files w/ certain encodings
import codecs

# library for working w/ file-like objects
import io

#****************************************************************
# create a place where we can smash all descriptions into one -- creating arrays
#****************************************************************
    
# append text to array each time we cycle through
# each citation is a separate string in the array until very end
fulltext = ''

# create/open the xml file 
g = codecs.open('postcard.xml', encoding='utf-8', mode='w+')
# write the header

fulltext = fulltext + '<?xml version="1.0"?>\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" \n'
fulltext = fulltext + 'xmlns:dc="http://purl.org/dc/elements/1.1" \n'
fulltext = fulltext + 'xmlns:dcmi="http://purl.org/dc/dcmitype/" \n'
#fulltext = fulltext + 'xmlns:loc="http://id.loc.gov/vocabulary/" \n'
fulltext = fulltext + 'xmlns:foaf="http://xmlns.com/foaf/0.1/" \n'
fulltext = fulltext + 'xmlns:schema="http://schema.org/docs/schema_org_rdfa.html">\n'

with open('postcard.csv', 'r+') as f:
    reader = csv.reader(f)
    for row in reader:

        # initialize the variable where you'll build each postcard's description
        description = ''

        # associate data from the row with variables
        url = row[0]
        title = row[1]
        identifier = row[2]
        creator = row[3]
        creatorURI = row[4]
        sendloc = row[5]
        sendlocURI = row[6]
        geocoord = row[7]
        recipient = row[8]
        recipURI = row[9]
        recloc = row[10]
        reclocURI = row[11]
        recipcoord = row[12]
        date = row[13]
        subject = row[14]
        subjURI = row[15]
        rights = row[16]
        dcformat = row[17]
        publisher = row[18]
        language = row[19]
        dctype = row[20]
        collection = row[21]
        
        # start the resource description
        description = description + '<rdf:Description rdf:about="' + url + '">\n'

        #title
        description = description + '<dc:title>' + title + '</dc:title>\n'

        #id
        description = description + '<dc:identifier>' + identifier + '</dc:identifier>\n'
        #date
        description = description + '<dc:date>' + date + '</dc:date>\n'
        #format
        description = description + '<dc:format>' + dcformat + '</dc:format>\n'
        #type
        description = description + '<dc:type rdf:resource="http://purl.org/dc/dcmitype/Image">' + dctype + '</dc:type>\n'
        #collection
        description = description + '<dcmi:collection>' + collection + '</dcmi:collection>\n'
        #language
        description = description + '<dc:language>' + language + '</dc:language>\n'
        #publisher
        description = description + '<dc:publisher>' + publisher + '</dc:publisher>\n'
        #rights
        description = description + '<dc:rights>' + rights + '</dc:rights>\n'
        
        #creator
        description = description + '<dc:creator rdf:resource="' + creatorURI + '">' + creator + '\n'
        #creator location
        description = description + '<dc:location rdf:resource="' + sendlocURI + '">' + sendloc + '</dc:location>\n'
        #creator location
        description = description + '<schema:GeoCoordinates rdf:resource="' + sendlocURI + '">' + geocoord + '</schema:GeoCoordinates>\n'
        description = description + '</dc:creator>\n'

        #recipient
        description = description + '<foaf:addressee rdf:resource="' + recipURI + '">' + recipient + '\n'
        #creator location
        description = description + '<dc:location rdf:resource="' + reclocURI + '">' + recloc + '</dc:location>\n'
        #creator location
        description = description + '<schema:GeoCoordinates rdf:resource="' + reclocURI + '">' + recipcoord + '</schema:GeoCoordinates>\n'
        description = description + '</foaf:addressee>\n'

        #subject
        description = description + '<dc:subject rdf:resource="'+ subjURI +'">' + subject + '</dc:subject>\n'

        # finish the individual description
        description = description + '</rdf:Description>\n'
        fulltext = fulltext + description
       
# close the tags
fulltext = fulltext + '</rdf:RDF>\n'

#un-comment next line for debugging in the shell
#print fulltext

# write string to file and close it
g.write(fulltext)
g.close()                           
                           
                           
        

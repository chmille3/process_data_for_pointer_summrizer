import getopt
import sys
import json
import hashlib
import os

def hashhex(s):
  """Returns a heximal formated SHA1 hash of the input string."""
  h = hashlib.sha1()
  h.update(s)
  return h.hexdigest()

def processJSON(jsonFile,outputDir):

    #Make sure there is an output directory
    if not os.path.exists(outputDir): os.makedirs(outputDir)
    
    URL_FILE = open('all_urls.txt','w')
    
    #go through the JSON and pull each entry into separate line
    lines = []
    for line in open(jsonFile,'r'):
        lines.append(json.loads(line))
    
    #at this point each line is a json dictionary for each entry in the json file
   
    for line in lines:
        
        #define here for URL and article text what the JSON dictionary keys are
        url = line['URL']
        #url = line['URL_s']
        #url = line['originalUrl']

        sentences = line['Sentences']
        #sentences = line['Sentences_t']
        #sentences = line['mergedsent']
        
        h = hashhex(url)
        
        fileName = outputDir + '/' + h+'.story' #create the. story file version of the article
        FILE = open(fileName,'w')
        FILE.write(sentences)
        FILE.close()

        URL_FILE.write(url + '\n')
        
    URL_FILE.close()

if __name__ == '__main__':
        
	print (sys.argv)
	print
	
	try:
	   opts, args = getopt.getopt(sys.argv[1:],"f:h:o:")
	except getopt.GetoptError:
		
		print ("opts:")
		print (opts)
		
		print ('\n')
		print ("args:")
		print (args)
		
		print ("Incorrect usage of command line: ")
		print ('python json_to_hash.py -f <file name> -o <output directory>')
	   
	  
	   
		sys.exit(2)
	   
	#initialize cmd line variables with default calues
	jsonFile = None
	outputDir = None

	
	for opt, arg in opts:
		print (opt,'\t',arg)
		if opt == '-h':
		   print ('python json_to_hash.py -f <file name> -o <output directory>')
		   sys.exit()
		elif opt in ("-f"):
		   jsonFile = arg
		elif opt in ("-o"):
			outputDir = arg
        

           
	print('\n')
	print("JSON file:",jsonFile)
	print("Output directory:", outputDir)
	print('\n')
    
	processJSON(jsonFile,outputDir)

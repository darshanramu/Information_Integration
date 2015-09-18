#!/usr/bin/env python
import sys,re
no_of_docs=0
skip=0
ip=sys.argv[1]
op=sys.argv[2]
with open(ip,"r") as f:
	with open(op,"w") as td:
		for line in f:
			line=line.lower()
			words=line.split()
		
			#print words
			doclen=len(words)
			if doclen<4:
				skip+=1
				continue
			#print doclen
			print "Document no.",no_of_docs+1
			for i,w in enumerate(words):
				#print i
				wshape=0
				if(re.match('[0-9][0-9]?[g][b]',w) or re.match('[0-9][0-9]? [g][b]',w)):
					wshape=1
				else:
					wshape=0
				if i==0:
					td.write("irrelevant	ppw_BOS1	pw_BOS2	w_{0}	nw_{1}	nnw_{2}	ws_{3}\n".format(words[i],words[i+1],words[i+2],wshape))
				if i==1:
					td.write("irrelevant	ppw_BOS1	pw_{0}	w_{1}	nw_{2}	nnw_{3}	ws_{4}\n".format(words[i-1],words[i],words[i+1],words[i+2],wshape))
				elif i==doclen-2:
					td.write("irrelevant	ppw_{0}	pw_{1}	w_{2}	nw_{3}	nnw_EOS2	ws_{4}\n".format(words[i-2],words[i-1],words[i],words[i+1],wshape))
				elif i==doclen-1:
					td.write("irrelevant	ppw_{0}	pw_{1}	w_{2}	nw_EOS1	nnw_EOS2	ws_{3}\n\n".format(words[i-2],words[i-1],words[i],wshape))
				elif i>1:
					td.write("irrelevant	ppw_{0}	pw_{1}	w_{2}	nw_{3}	nnw_{4}	ws_{5}\n".format(words[i-2],words[i-1],words[i],words[i+1],words[i+2],wshape))
			no_of_docs+=1
			#if no_of_docs==2:
				#sys.exit()
		#td.write('\n\n')
	print "Total Document Processed = {0} skipped:{1}".format(no_of_docs,skip)
		
	

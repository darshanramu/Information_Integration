#!/usr/bin/env python
from subprocess import Popen, PIPE
import sys

if len(sys.argv)<5:
	print "Invalid args. Please specify training data to learn from, model file to be generated, testing file to be tagged and output file to dump predicted labels"

training_file = sys.argv[1]
model_file    = sys.argv[2]
testing_file = sys.argv[3]
output_file = sys.argv[4]

def run_command(cmd_list,out,fileout):
        #print cmd_list
        process = Popen(cmd_list, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        out['stdout']=stdout
        out['stderr']=stderr
        if fileout:
        	with open(fileout,"w") as f:
        		f.write(str(out['stdout']))
        #print out

if __name__ == "__main__":
	cmd_list = ['crfsuite','learn',	'-m'+model_file,training_file]
	print cmd_list
	out={}
	print "Learning from the training file: {0} to build model file: {1}".format(training_file,model_file)
	run_command(cmd_list,out,None)	
	cmd_list = ['crfsuite','tag',	'-m'+model_file,testing_file]
	print cmd_list
	out={}
	print "Classifying the test file: {0} using model file: {1} and dumping labels in: {2}".format(testing_file,model_file,output_file)
	run_command(cmd_list,out,output_file)	
	#Verify results with
	#"paste <(awk '{print $1}' "+output_file+" ) <(awk '{print $3,$4,$5}' "+testing_file+" )"
	

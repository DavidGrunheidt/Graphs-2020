import os
import sys
from graphsManager import *

# on the first call to this function you must be SURE that "path" exists in the actual os.listdir()
def buildEachInstance(path: str) -> None:
	graphs = dict()

	# go into folder
	os.chdir(path)

	for item in os.listdir():
		if os.path.isdir(item):
			graphs.update(buildEachInstance(item))
		else: 
			graphs[item] = buildGraphFromFile(item)

	# return to the initial folder
	os.chdir("..")

	return graphs

def main():

	maybePath = sys.argv[len(sys.argv)-1]

	if maybePath == "testAll":
		graphs = buildEachInstance("instances")
		something_wrong = False
		for graph in graphs:
			if len(graphs[graph].vertices) == 0:
				something_wrong = True
				break
		if not something_wrong:
			print("Everything is right with your inputs")
	else:
		graph_path = "./instances/caminho_minimo/fln_pequena.net"
		graph = buildGraphFromFile(graph_path)

if __name__ == "__main__":
	main()
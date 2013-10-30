import test_distribution as td

def find_exclusive_networks():
	list_of_connections = []
	hosts = td.list_of_hosts
	for a in xrange(len(hosts)):
		l = [] + [0]*a
		for b in xrange(a,len(hosts)):
			if a != b:
				x = td.test_connection(hosts[a],hosts[b])
				if x[0]:
					l.append(1)
				else:
					l.append(0)
			else:
				l.append(0)
		list_of_connections.append(l)


	grouped = [0]*len(hosts)
	groups = []
	for a in xrange(len(hosts)):
		print "g ",grouped
		current_grouping = []
		if grouped[a] == 0:
			grouped[a] = 1
			current_grouping.append(a)
			for b in xrange(len(list_of_connections[a])):
				if list_of_connections[a][b] == 1 and grouped[b] == 0:
					current_grouping.append(b)
					grouped[b] = 1
		if current_grouping != []:
			groups.append(current_grouping)
	return groups

if __name__ == "__main__":
	print find_exclusive_networks()

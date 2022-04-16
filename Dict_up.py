#dictionarify 2
from S_format import *

class Dict_up:
	def __init__(self, data):
		self.data = data
		self.error_on_dupe = True
		self.results = {}
		self.dupes = {}
	def d_up(self, key_name):
		for item in self.data:
			if self.results.get(item[key_name], '') and self.error_on_dupe: raise 
			self.results[item[key_name]] = item
		return self.results


class Results:
	def __init__(self):
		self.data = {}
		self.dupe_count = 0
		self.master_crits = set()
		self.res_lst = []
	def add(self, key, item):
		self.master_crits = self.master_crits.union(set(list(self.item.keys())))
		if not self.data.get(key, ''): 
			self.data[key].append(item)
			count += 1
		else:
			self.data[key] = [item]
	def flatten_to_lst(self):
		for key in self.master_crits:
			for vals in key:
				self.res_lst.append(vals)
		return self.res_lst

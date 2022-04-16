
import operator, math
from S_format import *
from C_sort import *
from w_csv import *

class Dict_lst:
	def __init__(self, data= []):
		self.data = []
		self.header = set()
		for element in data:
			#print(element)
			#print(type(element))
			if data and not isinstance(element, dict): raise TypeError("Must be dict")
			else: 
				self.data.append(element)
				crits = list(element.keys())
				for column in crits: 
					#MOVE THE BELOW LOGIC INTO DICTIFY OR DICTIONARIFY
					#if column in self.header: raise Duplicate_header("There is more than 1 \"{0}\" column".format(column))
					self.header.add(column.strip(" "))
	def __repr__(self):
		return repr(self.data)
	def __len__(self):
		return len(self.data)
	def _dc(self):
		item = C_sort(x)
		items = item.contents
		crit = item.contents[0]
		results = []
		for i in range(1, len(items)):
			d = dict.fromkeys(crit, 0)
			for i_2 in range(0, len(items[i])):
				d[crit[i_2]] = items[i][i_2]
			results.append(d)
		return results
	def count_val(self, key, val):
		count = 0
		for i in range(0, len(self.data)):
			if self.data.get(key, 0) == val: count += 1
		return count
	def dupe_count(self, key):
		#self.sort(key)
		val_lst = set()
		count = 0
		for i in range(0, len(self.data)):
			if self.data[i][key] in val_lst and self.data[i][key]: count += 1
			else: val_lst.add(self.data[i][key])
		return count



	def pop_index(self, index):
		return self.data.pop(index)
	def modify_index(self, index, key, val):
		self.data[index][key] = val

	def del_index(self, index):
		del self.data[index]
	def transform_index(self, index, key, func):
		func(self.data[index], key)
	def add(self, element):
		if not isinstance(element, dict): raise TypeError("Must be dict")
		else: self.data.append(element)

	def add_lst(self, lst):
		self.data += lst
	def pull_all(self, key):
		results = []
		for d in self.data:
			if key in d: results.append(d[key])
			else: results.append('')
		return results
	def add_crit(self, crit, value= ''):
		for i in range(0, len(self.data)):
			self.data[i][crit] = value





	def get_index(self, index):
		return self.data[index]
	def sort(self, key):
		self.data.sort(key=operator.itemgetter(key))
	def find_cond(self, func, key, val):
		for i in range(0, len(self.data)):
			res = func(self.data[i], key, val)
			if res: return i
	def mult_search(self, keys, val, match_to_return = 0):
		#returns the first match by default
		#match = 0
		for crit in keys:
			self.sort(crit)
			index = self.b_search(crit, val)
			if index: return index
		return

	def b_search(self, key, val):
		left = 0
		right = len(self.data)-1
		while left <= right:
			mid = math.floor((right + left) / 2)
			if self.data[mid][key] < val: left = mid + 1
			elif self.data[mid][key] > val: right = mid - 1
			else: return mid
		return
	def search(self, key, val):
		for i in range(0, len(self.data)):
			if self.data[i][key].strip(' ') == val: return i

		return -1
	def export(self, c= [], fname = 'report_file.csv' ):
		data = self.data
		#needs an export method
		#doesn't violate immutability (the entire purpose of this object)
		if c: crit = c
		else: crit = list(data[0].keys())
		res = [crit]
		for i in data:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, fname)
		


class Duplicate_header(Exception):
	pass
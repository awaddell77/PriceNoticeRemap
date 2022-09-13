	
import itertools, copy
from Dictify import *
from Dict_lst import *

prod_map = {  
"90TT":'UNL 90',
"90REC":"UNL 90",
"87REG": "UNL 87", 
"87TT":"UNL 87",
"JET A":"JET A",
"K-2":"KERO", 
"ULN1":"#1ULSD C",
"ULN2":"#2ULSD C" ,
"UNL 88.5":"UNL 88.5"}

loc_map = {
"ANCHORAGE T2 DOCK":"ANC",
"ANCHORAGE T2 TSO NET":"ANC", 
"ANCHORAGE T3 DOCK":"ANC", 
'ANCHORAGE T3 TSO NET':"ANC",
"NIKISKI DOCK":"KENAI", 
"NORTH POLE DOCK":"FAIRBANKS",
"NORTH POLE TSO NET": "FAIRBANKS" }

branded_loc_map = {
"ANCHORAGE T3 TSO NET":"B",
"ANCHORAGE T2 TSO NET":"B", 
"NORTH POLE TSO NET":"B"
}
unbranded_prod_filter_by_loc = {"ANC": ("UNL 87","UNL 88.5","UNL 90","#1ULSD C","#2ULSD C","KERO","JET A"),
"FAIRBANKS": ("UNL 87","UNL 88.5","UNL 90","#1ULSD C","#2ULSD C","KERO","JET A"),
"KENAI": ("UNL 87","UNL 90","#1ULSD C","#2ULSD C","KERO","JET A")}

branded_prod_filter_by_loc = {"ANC": ("UNL 87","UNL 88.5","UNL 90","#1ULSD C","#2ULSD C"),
"FAIRBANKS": ("UNL 87","UNL 88.5","UNL 90","#1ULSD C","#2ULSD C"),
"KENAI": ("UNL 87","UNL 90","#1ULSD C","#2ULSD C"
)}
#products that are out of season
#prod_filter = ("#2ULSD C")
prod_filter = ("")

def product_remap(product_name):
	#set() is used to remove duplicate values, list() is used to allow individual elements to be converted into a list + brand value below
	prods = list(set(prod_map.values()))
	locs = list(set(loc_map.values()))
	unbranded_prods = []
	branded_prods = []
	for combo in itertools.product(locs, prods):
		#itertools creates a cartesian product of locs and prods
		#print(combo)
		if combo[1]  not in prod_filter and combo[1] in unbranded_prod_filter_by_loc[combo[0]]: unbranded_prods.append(list(combo)+["U"])
		if combo[1] not in prod_filter and combo[1] in branded_prod_filter_by_loc[combo[0]]: branded_prods.append(list(combo)+ ["B"])

	return (unbranded_prods, branded_prods)


def import_price_notification(fname):
	if '.csv' not in str(fname):raise RuntimeError("Must be csv")
	return Dict_lst(Dictify(fname).main())

def remap_pn(fname):
	pn_datafile = import_price_notification(fname)
	full_defaults = product_remap('')
	default_unbranded, default_branded = full_defaults[0], full_defaults[1]
	pn_data = ''
	dlst = dict_defaults(default_unbranded, default_branded)
	for i in range(0, len(dlst)):
		for i_2 in range(0, len(pn_datafile)):
			pn_row = pn_datafile.get_index(i_2)
			if check_rows(pn_row, dlst[i]):
				#print(dlst[i]["Location"], dlst[i]['TesProduct'], "vs", pn_row["Terminal"], pn_row["Commodity Abbreviation"])
				#print("{0} is dlist, {1} is pn_row".format(dlst[i]["Price"],pn_row["Price"] ))
				#print(dlst[i]["Location"] == loc_map[pn_row["Terminal"]])

				if dlst[i]['Price'] != -100 and float(pn_row['Price']) != float(dlst[i]['Price']) : raise RuntimeError("Possible Discrepancy Between Marathon Locations in {0} for {1}. Price: {2} ".format(dlst[i]['Location'], dlst[i]['TesProduct'], pn_row["Price"])) 
				dlst[i]['Price'] = pn_row['Price']
				dlst[i]['Date_daily'] = pn_row['Effective DateTime']
				if dlst[i]['Brand Indicator'] == 'B': dlst[i]['Tca'] = .05
	return dlst
def check_rows(pn_row, default_row):
	return (default_row['Location'] == loc_map[pn_row["Terminal"]] and default_row['TesProduct'] == prod_map[pn_row['Commodity Abbreviation']] and default_row["Brand Indicator"] == branded_loc_map.get(pn_row['Terminal'],'u'))
def dict_defaults(unbr, branded, crit=[]):
	dlst = []
	temp_arr = unbr + branded
	temp_arr.sort(key=lambda x:x[0])
	print("temp arr: ",temp_arr)
	def_date = ''
	for i in range(0, len(temp_arr)):
		#print(temp_arr[i])
		#print(len(temp_arr[i]))
		d = {'TesID':'', 'Location':temp_arr[i][0], 'TesProduct':temp_arr[i][1], 'Brand Indicator':temp_arr[i][2], 'TesDesignation':'Marathon','Price':-100, 'Tca': 0.05 if temp_arr[i][2] == 'B' else 0.0, 'Date_daily':'', 'OPISProcess':0}
		dlst.append(copy.deepcopy(d))
	print("Dlst:\n",dlst)
	return dlst
	#for i in range(0, temp_arr):




tst_data_fname = "Price_Notice_2022_5_3_22_27_30.csv"
#pn_data = import_price_notification(tst_data_fname)
#print(loc_map)
#print(prod_map)
#print("Remap: \n",product_remap("")[0],"\n","New","\n", product_remap("")[1])
res_data = remap_pn(tst_data_fname)
Dict_lst(res_data).export()
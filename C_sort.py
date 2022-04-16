import csv, codecs
from w_csv import *
class C_sort(object):#for processing CSVs
    def __init__(self, fname, other = 0):
        self.fname = fname
        self.delimiter = ','
        try:
            self.contents = r_csv(self.fname, mode= 'rt', delim= self.delimiter )
        except UnicodeDecodeError as UDE:
            self.contents = r_csv_2(self.fname, mode = 'rb', encoding='ISO-8859-1')
            print("Encountered Unicode Decode Error")
        self.other = other#will be used later for different file formats
    #def contents(self):
        #return r_csv(self.fname)
    def __len__(self):
        return len(self.contents)
    def __getitem__(self, index):
        return self.contents[index]
    def __add__(self, other):
        self.contents += other.contents
    def set_delim(self, x):
        self.delimeter = x
    def column(self, n):
        return self.col_grab(n)
    def row(self, n):
        return self.row_grab(n)
    def rows(self):#enumerate is used in order to ensure that each row has its row number in the first position or "cell"
        return enumerate(self.contents)
    def get_header(self, header_row = 0):
        return self.contents[header_row]
    def add_column(self, col, n ):# col is the list, n is the location of the new column
        pass
    def dict_pair(self, col1, col2):
        #col1 becomes the key, col2 the value
        keys = self.col_grab(col1)
        vals = self.col_grab(col2)
        if len(keys) != len(vals):
            print("The columns are unequal in length")
            return {}
        #the second element in the value list is the position
        return {keys[i]:[vals[i], i] for i in range(0, len(keys))}

        '''for i in self.contents:
            for i_2 in range(0, len(self.contents[i])):
                if i_2 == n:'''
    def fill_column(self, column_number, value, start, end, ignore_empty=True):
        if end > len(self.contents): raise IndexError("Row number is outside of range.")
        for i in range(start, end):
            #there does not appear to be a distinction between empy and non-empty rows currently
            if ignore_empty and not self.row_is_empty(i): self.contents[i][column_number] = value
            if not ignore_empty: self.contents[i][column_number] = value

    def ins_column(self, column_name, value,position, header_pos=0 ):
        
        self.contents[header_pos].insert(position,column_name)
        for i in range(0, header_pos):
            self.contents[i].insert(position, value)
        for i in range(header_pos+1, len(self.contents)):
            self.contents[i].insert(position, value)
            

    def row_is_empty(self, row_number):
        #'empty' in this context means filled with empty spaces
        row = self.row_grab(row_number)[:]
        row.sort(reverse=True)
        if row[0]: return False
        return True
    def empty_cleanse(self):
        new_contents = []
        for i in range(0, len(self.contents)):
            if not self.row_is_empty(i): new_contents.append(self.contents[i])
        self.contents = new_contents
    def export(self, fname):
        w_csv(self.contents, fname)
    def export_column_as_row(self, column_number, fname = 'columnexport.csv'):
        #exports column csv with data as single comma delimited line
        t_data = []
        t_data.append(self.col_grab(column_number))
        w_csv(t_data, fname)



            


        
    
    def col_grab(self, n):#n is the column number
        h = self.contents
        columns = []
        for i in range(0, len(h)):

            new_row = h[i]
            #print(new_row)
            #NOTE: empty columns should be given a space during import via r_csv
            if not new_row: new_col = " "
            else: new_col = new_row[n]
            columns.append(new_col)
        return columns
    def row_grab(self, n):
        #h = self.contents
        return self.contents[n]
                    



    def d_check(x, lump = 0):#finds
        a_list = x
        for i in range(0, len(a_list)):
            if type(a_list[i]) == list:
                new = a_list[i]
                new1 = []
                count = 0
                while type(new[i]) == list:
                    for i_2 in range(0, len(new)):
                        new = list_enum(new)
                        count = count + 1
                        print('Layer #%d' % (count))
                new1.append(new)#
                return new1
            else:
                print("This is not a list")
                return a_list
            
    def l_lumper(x):#lumps all of the elements of a list together (used for searching)
        new1= []
        a_list = x
        for i in range(0, len(a_list)):
            new = a_list[i]
            for i_2 in range(0, len(new)):
                new1.append(new[i_2])          
        return new1
                    
                #return new
            #else:
                #return a_list[i]
    def l_search(x,y):
        if type(x) != list:
            x = [x]
        missing = []
        #for i in range(0, len(x)):
            
    def l_check(x,y):#checks to see if single element x is in list y
        target = x
        for i in range(0, len(y)):
            if x in y[i] or x == y[i]:
                return True
        return False

                    
    def list_enum(x):#simply goes through a list and extracts its elements
        l = []
        for i in range(0 , len(x)):
            l.extend(x[i])
        return l
    

    def f_spaces(self, x, s_item, s_item2 = 0):# splits list according to s_item and eliminates extra spaces
        oldlist = x
        new_list = []
        for i in range(0, len(oldlist)):
            new = oldlist[i].split(' ')
            new2 = new.split(s_item)
            for i_2 in range(0, len(new2)):
                #new2[i] = new2[i].strip(' ')
                for i_2 in range(0, len(new2)):
                    if new2[i_2] != ' ' or ' ' not in new2[i_2]:
                        new
            new3 = s_item.join(new2)
            new_list.append(new3)
        return new_list
    
    def spacesmash(self, x):
        old = x.split(' ')
        l = []
        s = ' '
        for i in range(0, len(old)):
            if old[i] != '':
                l.append(old[i])
        return s.join(l)#every element is returned joined by a single space

    def match(self,x,y):
        matches = []
        for i in enumerate(y):
            if x == i[1]:
                matches.append(i)
        if len(matches) == 1:
            print("%d instance found" % len(matches))
            return matches
        elif len(matches) > 1:
            print("%d instances found" % len(matches))
            return matches
        else:
            print('No match')
            return None

    def p_compare(self, x,y):
        if type(x) != str or type(y) != str:
            return 'Item(s) must be a string'
        new_x = self.p_elementsp(x)
        new_y = self.p_elementsp(y)
        
        #for i in enumerate(x):
    def p_elementsp(x):
        new = []
        for i in range(0, len(x)):
            new.append(x[i])
        return new
    def num_listgrab(self, x, n):#pulls a particular column from a csv along with its row number
        l = []
        for i in enumerate(x):
            num = i[0]
            row = i[1]
            cell = row[n]
            l.append((n,cell))
        return l
    def master_check(self, x,y):
        l = []
        #if type(x) != list:
            
        for i in range(0,len(x)):
            if self.l_check(x[i], y):
                print('%s is there' % (names[i]))
            else:
                l.append(names[i])
        #return 'The following items are in %s but are not in 
        
    def space_norm(self, x):
        l = x
        for i in range(0, len(l)):
            l[i] = self.spacesmash(l[i])
        return l
            
        
    def title_cap(self, x):
        word = x
        for i in range(0, len(x)):
            if i == 0 and type(x[i]) == str:
                x[i]=x[i].upper()
            elif x[i - 1] == '':
                x[i] = x[i].upper()
            #elif x[i] == 
        
def r_csv(x,mode='rt', delim = ','):
    l = []
    csv_in = open(x, mode, encoding = 'utf-8')
    myreader = csv.reader(csv_in, delimiter = delim)
    for row in myreader:
        l.append(row)
    csv_in.close()
    return l
def r_csv_2(x,mode='rt', encoding = 'utf-8'):
    l = []
    csv_in = codecs.open(x, mode, encoding)
    myreader = csv.reader(csv_in)
    for row in myreader:
        l.append(row)
    csv_in.close()
    return l

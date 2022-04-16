from C_sort import *
class Dictify:
    def __init__(self, fname):
        if '.' not in fname: raise FileNameError(fname)
        if '.csv' not in fname: raise IncorrectExtension(fname)
        self.fname = fname
        self.strip_headers = True


    def main(self):
        #should produce list of dictionaries from a csv, with the column headers as the keys
        item = C_sort(self.fname)
        items = item.contents
        crit = item.contents[0]
        if self.strip_headers: crit = [i.strip(" ") for i in crit]
        results = []
        for i in range(1, len(items)):
            d = dict.fromkeys(crit, 0)
            for i_2 in range(0, len(items[i])):
                d[crit[i_2]] = items[i][i_2]
            results.append(d)
        return results
    def just_header(self):
        item = C_sort(self.fname)
        items = item.contents
        crit = item.contents[0]
        if self.strip_headers: crit = [i.strip(" ") for i in crit] 
        return crit

class Duplicate_columns(Exception):
    pass
class FileNameError(Exception):
    def __init__(self,fname):
        self.fname = fname 
    def __str__(self):
        return repr("{0} is not correct.".format(str(self.fname))) 
class IncorrectExtension(FileNameError):
    def __init__(self, fname):
        super().__init__(fname)
        self.ext = fname.split('.')[1]

    def __str__(self):
        return repr("Only .csv files are supported. \"{0}\" cannot be used.".format(str(self.fname)))
        

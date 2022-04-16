class S_format(object):
    def __init__(self, s):
        self.s = s#some bsobject text file or a standalone string

    def linkf(self,n, base = 0, attrs= 0, default = '"'):#x is the item, n = tag takes link tag (MUST BE STRING) and extracts the link
        l =[]
        ln = ''
        x = self.s
        if attrs != 0:
            x = re.sub('<a','', x)#strips the tag from the string, helps in certain situations where the location of the link changes in between elements
        elif type(attrs) == str:
            x = re.sub(attrs, '', x)
        ln_s = x.split(default)
        for i in range(0, len(ln_s)):
            if ln_s[i] == n or ln_s[i] == ' %s' % (n):
                if ln_s[i+1] != 'javascript:void(0);':
                    ln = ln_s[i+1] #ln is the link (still needs to be joined witht the base URL
        if base == 0:
            ln = self.bc_b_url(ln)
            return ln
        else:
            ln = base + ln #MAJOR WORKAROUND!!!! IN THE FUTURE THS SHOULD CALL A FUNCTION THAT FINDS THE BASE
            return ln
    def d_sort(self,c = 0, df = 'N/A'):#takes dictionary, pulls criteria out as list
        d = self.s
        n_l = []
        if c == 0:
            return list(d.values())
        elif c==1:
            criteria = list(d.keys())
            default = df
        else:
            criteria = c
            default = df
        for i in range(0, len(criteria)):
            n_l.append(d.get(criteria[i], default))#removed brackets from d.get()
            #del d[criteria[i]]
        #l = d.keys()
        return n_l
    def bc_b_url(self,x):#x is the url
        if x == '' or x == None:
            return 'None'
    
        base = ''
        url = base + x
        #url = x.split('/',1)
        return url
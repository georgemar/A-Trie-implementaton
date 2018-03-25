#!/usr/bin/python
import sys
import time
class Node :
    def __init__(self, end = False):
        self.ch = {}
        self.end = end
class Trie :
    def __init__(self) :
        self.rt = Node()
    def addword(self,istr,cur,i) :
        if (cur.ch.has_key(istr[i])) and (i == len(istr) - 1) :
            cur.ch[istr[i]].end = True
        elif not(cur.ch.has_key(istr[i])) and (i == len(istr) - 1) :
            cur.ch[istr[i]] = Node(True)
        elif (cur.ch.has_key(istr[i])) and (i < len(istr) -1) :
            self.addword(istr,cur.ch[istr[i]],(i+1))
        elif not(cur.ch.has_key(istr[i])) and (i < len(istr) -1) :
            cur.ch[istr[i]] = Node()
            self.addword(istr,cur.ch[istr[i]],i+1)
    def searchtrie(self,istr,cur,i) :
        if (cur.ch.has_key(istr[i])) and (i == len(istr) - 1) :
            if (cur.ch[istr[i]].end == True) :
                print "Found it"
            else :
                print "Not found"
        elif (cur.ch.has_key(istr[i])) and (i < len(istr) -1) :
            self.searchtrie(istr,cur.ch[istr[i]],(i+1))
        else :
            print "Not found"

if __name__=="__main__" :
    t1 = time.time()
    try :
        f = open(sys.argv[1],"r")
    except IOError :
        print "Unable to open the file %s" %(sys.argv[1])
        sys.exit(0)
    ilist = f.readlines()
    trie = Trie()
    for i in ilist :
        rt = getattr(trie,'rt')
        trie.addword(i.strip('\n'),rt,0)
    print "Added to trie in %fsecs" %(time.time() - t1)
    name = raw_input("Give name to search : ")
    while name != 'exit' :
        t0 = time.time()
        trie.searchtrie(name,rt,0)
        print "Took %fsecs" %(time.time() - t0)
        name = raw_input("Give name to search : ")

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:08:02 2018

@author: ymoshfegh
"""

import sys

def main():
    input = sys.argv[1]
    output = sys.argv[2]
    
    with open(input,'r') as ip:
        drugs = {}
        text = ip.readlines()
        for x in text[1:]:
            sp = x.split(',')
            if len(sp) == 5:
                if sp[3].strip('"') not in drugs.keys():
                    drugs[sp[3].strip('"')] = [1,float(sp[4].strip('"'))]
                else:
                    drugs[sp[3].strip('"')][0] += 1
                    drugs[sp[3].strip('"')][1] += float(sp[4].strip('"'))
                
                
    drugs_sort = [[k,v] for k,v in sorted(drugs.items(), key=lambda(k,v):(-v[1],k))]
    
    
    with open(output,'w') as op:
        op.write('drug_name,num_prescriber,total_cost')
        
        for x in drugs_sort:
            op.write('\n')
            op.write(x[0]+','+str(x[1][0]) + ',' + str(x[1][1]))
        
        
        
        
if __name__ == '__main__':
  main()
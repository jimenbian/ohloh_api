def test(dic):
    
    str=''
    ColumnStyle=' VARCHAR(20)'
    for key in dic.keys():
         str=str+' '+key+ColumnStyle+','
    
    print str[:-1]    





if __name__=='__main__':
   
   dic={'weaf':'ca','haha':'vaer'}
   test(dic)
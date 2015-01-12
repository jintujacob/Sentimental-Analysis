
#from old_fortrans import uni_trans_mal
import unicodedata
import codecs
import string
no_compound=""
unidata=""
first_word=""
sec_wod=""
d=""
g=""
h=""
fr = codecs.open('aaa', encoding='utf-8')
fw = codecs.open('out.txt', 'w')
ft = codecs.open('new.txt', 'w')
count1=""
count2=""
count=0
sentence_id=0
for line in fr:
    #print line
    sentence_id=sentence_id+1
    sentence=str(sentence_id)
    

    fw.write('\n')    
    fw.write(sentence)
    line1=line.encode('UTF-8')
    fw.write(line1)
    
    fw.write('\n')
    line_data=line.split()
    
        for i in range(0,len(line_data)):
            unidata=line_data[i]
   # print unidata
            var=1
        print unidata
            for i in range(0,len(unidata)):
                
                    try:



 #2----- maayirunnu---- #
                           if(unidata[i]==U'\u0d2e'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f'
 and unidata[i+3]==U'\u0d3f' 
and unidata[i+4]==U'\u0d30' ):
                           print "code 2"                                 
                         if(var==1):
                                 
                                            x=unidata[0:i]+U'\u0d02' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                             first_word=unidata[0:i]+U'\u0d02'
                                            sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                        var=0
                                 print "$$$$$$$$$$"
                                 print sec-word
                                     if(len(sec_word) >3):
                                    print "hai"
                                    first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')  
#3.thaamasichchirunna 
                           elif(unidata[i-1]==U'\u0d1a' and  unidata[i]==U'\u0d3f' and unidata[i+1]==U'\u0d30' and unidata[i+2]==U'\u0d41' and unidata[i+3]==U'\u0d28' and unidata[i+4]==U'\u0d4d'):
                        print "code 3" 
                                  if(var==1):
                                        x=unidata[0:i]+U'\u0d4d' +' + '+U'\u0d07'+unidata[i+1:len(unidata)]
                    
                                        
                            first_word=unidata[0:i]+U'\u0d4d'
                                        sec_word=U'\u0d07'+unidata[i+1:len(unidata)]
                            var=0
                            first_word=first_word.encode('UTF-8')
                                         sec_word=sec_word.encode('UTF-8')
            
                    

#4.prathissttichchirikkunnath
                           elif(unidata[i]==U'\u0d1a'and unidata[i+1]==U'\u0d4d'and unidata[i+2]==U'\u0d1a' and  unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' and unidata[i+5]==U'\u0d3f' and unidata[i+6]==U'\u0d15'):
                        print "code 4" 
                                   if(var==1):
                                        x=unidata[0:i+3]+U'\u0d4d' +' + '+U'\u0d07'+unidata[i+4:len(unidata)]
                             first_word=unidata[0:i+3]+U'\u0d4d'
                                        sec_word=U'\u0d07'+unidata[i+4:len(unidata)]
                            var=0
                            first_word=first_word.encode('UTF-8')
                                         sec_word=sec_word.encode('UTF-8')
           

           
                              
                        
                       
#11.vyakthamaakkiyirunnu
                           elif(unidata[i]==U'\u0d2e' and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d15' and unidata[i+3]==U'\u0d4d' 
and unidata[i+4]==U'\u0d15'):
                        print "code 11" 
                                       if(var==1):
                                        x=unidata[0:i]+ U'\u0d02' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                            first_word=unidata[0:i]+U'\u0d02'
                                        sec_word=U'\u0d06'+unidata[i+2:len(unidata)]
                                          var=0
                            first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
                    
                    
#13.iiTaakkunna
                           elif(unidata[i]==U'\u0d3e' and unidata[i+1:i+4]==U'\u0d15\u0d4d\u0d15' and unidata[i+4]==U'\u0d41' and unidata[i+5:i+8]==U'\u0d28\u0d4d\u0d28'):
                           print "code 13" 
                                      if(var==1):
                                                x=unidata[0:i]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+1:len(unidata)]
                                        
                                    first_word=unidata[0:i]+U'\u0d4d'
                                                sec_word=U'\u0d06'+unidata[i+1:len(unidata)]
                    
                                                var=0
                                    first_word=first_word.encode('UTF-8')
                                                sec_word=sec_word.encode('UTF-8')
                    
                    
#15.kaaranhamenthaanhenna
                           elif(unidata[i]==U'\u0d2e' and unidata[i+1]==U'\u0d46' and unidata[i+2]==U'\u0d28' and unidata[i+3]==U'\u0d4d' and unidata[i+4]==U'\u0d24' ):
                           print "code 15" 
                                     if(var==1):
                                            x=unidata[0:i]+ U'\u0d02' + ' + '+ U'\u0d0e'+unidata[i+2:len(unidata)]
                            first_word=unidata[0:i]+U'\u0d02'
                                        sec_word=U'\u0d0e'+unidata[i+2:len(unidata)]
                                           var=0
                            first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
                   
                   
#16.pariganhanaykketuththu
                           elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d4d' and unidata[i+2]==U'\u0d15' and unidata[i+3]==U'\u0d4d' and unidata[i+4]==U'\u0d15' and unidata[i+5]==U'\u0d46' and unidata[i+6]==U'\u0d1f' ):
                           print "code 16" 
                                      if(var==1):
                                         x=unidata[0:i+5]+ U'\u0d4d' + ' + '+ U'\u0d0e'+unidata[i+6:len(unidata)]
                              first_word=unidata[0:i+5]+U'\u0d4d'
                                          sec_word=U'\u0d0e'+unidata[i+6:len(unidata)]
                              var=0
                              first_word=first_word.encode('UTF-8')
                                          sec_word=sec_word.encode('UTF-8')

                                
                            
                        
#19.ninnatooR~ttupooyi
                           elif( unidata[i]==U'\u0d4b' and unidata[i+1]==U'\u0d7c' and unidata[i+2:i+5]==U'\u0d24\u0d4d\u0d24' ):
                                    print "code 19" 
                                     if(var==1):
                                             x=unidata[0:i]+U'\u0d4d' + ' + '+U'\u0d13'+unidata[i+1:len(unidata)]
                              first_word=unidata[0:i]+U'\u0d4d'
                                  sec_word=U'\u0d13'+unidata[i+1:len(unidata)]
                                            var=0
                              first_word=first_word.encode('UTF-8')
                                          sec_word=sec_word.encode('UTF-8')
                
               
#21.praadhaanyamuLLataaN
                           elif( unidata[i]==U'\u0d41' and unidata[i+1:i+4]==U'\u0d33\u0d4d\u0d33' and unidata[i+4]==U'\u0d24'  
and unidata[i+5]==U'\u0d3e'  and unidata[i+6]==U'\u0d23'):
                                   print "code 21" 
                                    if(var==1):
                                             x=unidata[0:i-1]+U'\u0d02' + ' + '+U'\u0d09'+unidata[i+1:len(unidata)]
                                        
                                          first_word=unidata[0:i-1]+U'\u0d02'
                                       sec_word=U'\u0d09'+unidata[i+1:len(unidata)]
                                    var=0
                             first_word=first_word.encode('UTF-8')
                                             sec_word=sec_word.encode('UTF-8')
                
#22.tirakkanubhavappeTunna
                              elif( unidata[i:i+3]==U'\u0d15\u0d4d\u0d15' and unidata[i+3]==U'\u0d28'  and unidata[i+4]==U'\u0d41'  and unidata[i+5]==U'\u0d2d'):
                                print "code 22" 
                                 if(var==1):
                                       x=unidata[0:i+3]+U'\u0d4d' + ' + '+U'\u0d05'+unidata[i+3:len(unidata)]
                                       first_word=unidata[0:i+3]+U'\u0d4d'
                               sec_word=U'\u0d05'+unidata[i+3:len(unidata)]
                                  var=0
                           first_word=first_word.encode('UTF-8')
                                       sec_word=sec_word.encode('UTF-8')
               

#25.--------LaRinjnj
                           elif(unidata[i]==U'\u0d33' and unidata[i+1]==U'\u0d31' and unidata[i+2]==U'\u0d3f' and unidata[i+3:i+6]==U'\u0d1e\u0d4d\u0d1e'):
                                      print "code 25" 
                                      if(var==1):
                                     x=unidata[0:i]+ U'\u0d7e' + ' + '+U'\u0d05'+unidata[i+1:len(unidata)]
                         first_word=unidata[0:i]+ U'\u0d7e'
                             sec_word=U'\u0d05'+unidata[i+1:len(unidata)] 
                            
                       
                                var=0
                          first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
#26---------naRinjnj
                              elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d31' and unidata[i+2]==U'\u0d3f' and unidata[i+3:i+6]==U'\u0d1e\u0d4d\u0d1e'):
                                    print "code 26" 
                                     if(var==1):
                                        x=unidata[0:i]+U'\u0d28'+ U'\u0d4d' + ' + '+U'\u0d05'+unidata[i+1:len(unidata)]
                          first_word=unidata[0:i]+U'\u0d28'+ U'\u0d4d'
                             sec_word=U'\u0d05'+unidata[i+1:len(unidata)] 
                                         var=0
                         first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
#27---------raRinjnj
                           elif(unidata[i]==U'\u0d30' and unidata[i+1]==U'\u0d31' and unidata[i+2]==U'\u0d3f' and unidata[i+3:i+6]==U'\u0d1e\u0d4d\u0d1e'):
                                   print "code 27" 
                                    if(var==1):
                                    x=unidata[0:i+1]+ U'\u0d4d' + ' + '+U'\u0d05'+unidata[i+1:len(unidata)]
                        first_word=unidata[0:i+1]+ U'\u0d4d'
                            sec_word=U'\u0d05'+unidata[i+2:len(unidata)] 
                        var=0
                        first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')

                
#28.kuLiR~mmayeekunna
                           elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d47' and unidata[i+2]==U'\u0d15' and unidata[i+3]==U'\u0d41' and unidata[i+4:i+7]==U'\u0d28\u0d4d\u0d28'):
                                 print "code 28" 
                                  if(var==1):
                                        x=unidata[0:i]+  ' + '+U'\u0d0e'+unidata[i+2:len(unidata)]
                                        first_word=unidata[0:i]
                             sec_word=U'\u0d0e'+unidata[i+2:len(unidata)] 
                                       var=0
                         first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
              
#31.kowtukameeRunna
                                  elif(unidata[i]==U'\u0d2e' and unidata[i+1]==U'\u0d47' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d41' and unidata[i+4:i+7]==U'\u0d28\u0d4d\u0d28'):
                                  print "code 31" 
                                     if(var==1):
                                       x=unidata[0:i]+ U'\u0d02' + ' + '+U'\u0d0f'+unidata[i+2:len(unidata)]
                        first_word=unidata[0:i]+ U'\u0d02'
                            sec_word=U'\u0d0f'+unidata[i+2:len(unidata)] 
                                      var=0
                        first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')
                
#34.striikaLuL~ppeTunna
                               elif(unidata[i]==U'\u0d33' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d7e' and unidata[i+3:i+6]==U'\u0d2a\u0d4d\u0d2a' and unidata[i+6]==U'\u0d46' ):
                                print "code 34" 
                                     if(var==1):
                                         x=unidata[0:i]+U'\u0d7e' + ' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                           first_word=unidata[0:i]+U'\u0d7e'
                              sec_word=U'\u0d09'+unidata[i+2:len(unidata)] 
                       
                              var=0
                           first_word=first_word.encode('UTF-8')
                                      sec_word=sec_word.encode('UTF-8')
                
               
#35.vidyaaR~tthiyumaTangngunna
                               elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d2e'  and unidata[i+3]==U'\u0d1f' and unidata[i+4:i+7]==U'\u0d19\u0d4d\u0d19'  ):
                                print "code 35" 
                                    if(var==1):
                                         x=unidata[0:i+2]+U'\u0d02' + ' + '+U'\u0d05'+unidata[i+3:len(unidata)]
                            
                                         first_word=unidata[0:i+2]+U'\u0d02'
                              sec_word=U'\u0d05'+unidata[i+3:len(unidata)] 
                                 var=0
                           first_word=first_word.encode('UTF-8')
                                      sec_word=sec_word.encode('UTF-8')
               
                
#36.maatrikayaakkiyirunnu
                               elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d3e' and unidata[i+2:i+5]==U'\u0d15\u0d4d\u0d15'  and unidata[i+5]==U'\u0d3f'  ):
                                print "code 36" 
                                     if(var==1):
                                      x=unidata[0:i]+ ' + '+U'\u0d06'+unidata[i+2:len(unidata)]
                            
                                       first_word=unidata[0:i]
                              sec_word=U'\u0d06'+unidata[i+2:len(unidata)] 
                              var=0
                           first_word=first_word.encode('UTF-8')
                                      sec_word=sec_word.encode('UTF-8')
                
#37.naayakanaakkiya
                               elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d3e' and unidata[i+2:i+5]==U'\u0d15\u0d4d\u0d15'  and unidata[i+5]==U'\u0d3f'  ):
                                print "code 37" 
                                     if(var==1):
                                        x=unidata[0:i]+ U'\u0d7b' + ' + '+U'\u0d06'+unidata[i+2:len(unidata)]
                            
                                        first_word=unidata[0:i]+U'\u0d7b'
                             sec_word=U'\u0d06'+unidata[i+2:len(unidata)] 
                                var=0
                                first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
               

                
#38.etiR~ppaayirunnu
                                   elif(unidata[i:i+3]==U'\u0d2a\u0d4d\u0d2a' and unidata[i+3]==U'\u0d3e' and unidata[i+4]==U'\u0d2f' and unidata[i+5]==U'\u0d3f'  and unidata[i+6]==U'\u0d30'  and unidata[i+7]==U'\u0d41' ):
                                print "code 38" 
                                         if(var==1):
                                      x=unidata[0:i+3]+ U'\u0d4d' + ' + '+U'\u0d06'+unidata[i+4:len(unidata)]
                            
                                       first_word=unidata[0:i+3]+U'\u0d4d'
                              sec_word=U'\u0d06'+unidata[i+4:len(unidata)] 
                                 var=0
                              first_word=first_word.encode('UTF-8')
                                      sec_word=sec_word.encode('UTF-8')
                
                
#41. putumukhamavatarippikkunna
                                   elif(unidata[i]==U'\u0d2e' and unidata[i+1]==U'\u0d35' and unidata[i+2]==U'\u0d24'  and unidata[i+3]==U'\u0d30' and unidata[i+4]==U'\u0d3f' and unidata[i+5:i+8]==U'\u0d2a\u0d4d\u0d2a'):
                                print "code 41" 
                                         if(var==1):
                                           x=unidata[0:i]+U'\u0d02' + ' + '+U'\u0d06'+unidata[i+1:len(unidata)]
                            
                                         first_word=unidata[0:i]+U'\u0d02'
                                  sec_word=U'\u0d06'+unidata[i+1:len(unidata)] 
                                  var=0
                                  first_word=first_word.encode('UTF-8')
                                          sec_word=sec_word.encode('UTF-8')
                
#51.kaTattiyirunnat
                           elif(unidata[i-1]==U'\u0d3f' and unidata[i]==U'\u0d2f' and  unidata[i+1]==U'\u0d3f' and unidata[i+2]==U'\u0d30'  and unidata[i+3]==U'\u0d41' and unidata[i+4:i+7]==U'\u0d28\u0d4d\u0d28'):
                                 print "code 51"
                                 if(var==1):
                                      x=unidata[0:i]+  ' + '+U'\u0d07'+unidata[i+2:len(unidata)]
                        
                                    first_word=unidata[0:i]
                           sec_word=U'\u0d07'+unidata[i+2:len(unidata)] 
                           var=0
                              first_word=first_word.encode('UTF-8')
                                   sec_word=sec_word.encode('UTF-8')
                
        
#59.nadiyilengnguM
                           elif(unidata[i]==U'\u0d32' and unidata[i+1]==U'\u0d46' and unidata[i+2:i+5]==U'\u0d19\u0d4d\u0d19' and  unidata[i+5]==U'\u0d41'):
                         print "code 59"
                                   if(var==1):
                                         x=unidata[0:i]+U'\u0d7d' ' + ' +  U'\u0d0e'+unidata[i+2:len(unidata)]
                     
                                         first_word=unidata[0:i]+U'\u0d7d'
                                        sec_word=U'\u0d0e'+unidata[i+2:len(unidata)]
                                 var=0
                    
                                first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')

#63.iiRanaNiyunnu
                           elif(unidata[i-1]==U'\u0d28' and unidata[i]==U'\u0d23' and unidata[i+1]==U'\u0d3f' and unidata[i+2]==U'\u0d2f' ):
                         print "code 63"
                                if(var==1):
                                        x=unidata[0:i-1]+U'\u0d7b' ' + ' +  U'\u0d05'+unidata[i:len(unidata)]
                                        first_word=unidata[0:i-1]+U'\u0d7b'
                                     sec_word=U'\u0d05'+unidata[i:len(unidata)]
                                     var=0
                        
                                     first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')  

#76.kuLiraNiyikkunnu
                           elif(unidata[i-1]==U'\u0d30' and unidata[i]==U'\u0d23' and unidata[i+1]==U'\u0d3f' and unidata[i+2]==U'\u0d2f' ):
                        print "code 76"
                                if(var==1):
                                        x=unidata[0:i]+U'\u0d4d' ' + ' +  U'\u0d05'+unidata[i:len(unidata)]
                                        first_word=unidata[0:i]+U'\u0d4d'
                                     sec_word=U'\u0d05'+unidata[i:len(unidata)] 
                                     var=0
                        
                                     first_word=first_word.encode('UTF-8')
                                      sec_word=sec_word.encode('UTF-8')  


#81.manassiniNangngiya
                           elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d3f'  and unidata[i+2]==U'\u0d23'  and  unidata[i+3:i+6]==U'\u0d19\u0d4d\u0d19' and unidata[i+6]==U'\u0d3f'):
                                   print "code 81"
                                    if(var==1):
                                            x=unidata[0:i+1]+ U'\u0d4d' + ' + '+U'\u0d07'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i+1]+ U'\u0d4d'
                                    sec_word=U'\u0d07'+unidata[i+2:len(unidata)]  
                                       var=0
                        
                                 first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')

#84.oraana
                           elif(unidata[i-1]==U'\u0d12' and unidata[i]==U'\u0d30' and unidata[i+1]==U'\u0d3e'):
                                    print "code 84"
                                    if(var==1):
                                            x=unidata[0:i+1]+ U'\u0d41' + ' + '+U'\u0d06'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i]
                                    sec_word=U'\u0d07'+unidata[i+2:len(unidata)]  
                                    var=0
                        
                                    first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
#96. Avaganikkaanavaatha
                       elif(unidata[i]==U'\u0d3e' and unidata[i-1]==U'\u0d28'  and unidata[i+1]==U'\u0d35' and unidata[i+2]==U'\u0d3e'):
                        print "code 96"
                        if(var==1):
                  
                                        x=unidata[0:i-1]+U'\u0d7b'+ ' + '+U'\u0d06'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i-1]+U'\u0d7b'
                                        sec_word=U'\u0d06'+unidata[i+1:len(unidata)]  
                                           var=0
                        
                                       first_word=first_word.encode('UTF-8')
                                       sec_word=sec_word.encode('UTF-8')
#99.-------lluyaRththi----#

                           elif(unidata[i]==U'\u0d2f' and unidata[i-1]==U'\u0d41'  and unidata[i-2]==U'\u0d33' and unidata[i+1]==U'\u0d7c'):
                         print "code 99"
                                 if(var==1):
                     
                                         x=unidata[0:i-2]+U'\u0d7e'+ ' + '+U'\u0d09'+unidata[i:len(unidata)]
                                          first_word=unidata[0:i-2]+U'\u0d7e'
                                         sec_word=U'\u0d09'+unidata[i+2:len(unidata)] 
                                         var=0
                 
                                first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
#100.----- suyaRththi-----#
                           elif(unidata[i]==U'\u0d38' and unidata[i+1]==U'\u0d41'  and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d7c' ):
                        print "code 100"
                                 if(var==1):
                                         x=unidata[0:i+1]+U'\u0d4d'+ ' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i+1]+U'\u0d4d'
                                        sec_word=U'\u0d09'+unidata[i+2:len(unidata)]  
                                        var=0
                 
                                first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')    
#105...veththunna
                           elif((unidata[i]==U'\u0d46' and unidata[i-1]==U'\u0d35' and unidata[i+1]==U'\u0d24' and unidata[i+2]==U'\u0d4d' and unidata[i+3]==U'\u0d24')):
                        print "code 105"
                                if(var==1):
                    
                                        x=unidata[0:i]+U'\u0d4d' + ' + '+ U'\u0d0e'+unidata[i+1:len(unidata)]
                                         first_word=unidata[0:i]+U'\u0d4d'
                                       sec_word=U'\u0d0e'+unidata[i+2:len(unidata)]  
                                var=0
                
                                first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
                   
#106...seththunna
                           elif((unidata[i]==U'\u0d46' and unidata[i-1]==U'\u0d38' and unidata[i+1]==U'\u0d24' and unidata[i+2]==U'\u0d4d' and unidata[i+3]==U'\u0d24')):
                         print "code 106"
                                    if(var==1):
                    
                                        x=unidata[0:i]+U'\u0d4d' + ' + '+ U'\u0d0e'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i]+U'\u0d4d' 
                                        sec_word=U'\u0d0e'+unidata[i+2:len(unidata)]  
                                 var=0
                
                                first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
#107.---- yaayirunnu----#
                           elif(unidata[i]==U'\u0d2f'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' ):
                                   print "code 107"
                                     if(var==1):
                             print "****************"
                                            x=unidata[0:i]+ ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i]
                                           sec_word=U'\u0d06'+unidata[i+2:len(unidata)] 
                                 var=0
                             print sec_word
                             print len(sec_word)
                                 if(len(sec_word)> 4):
                                for j in range(0,len(sec_word)):
                                    if(sec_word[j]==U'\u0d2f'  and sec_word[j+1]==U'\u0d3f'and sec_word[j+2]==U'\u0d30'):
                                        print "match"
                                        g=sec_word[0:j+2]
                                        print g
                                        h=U'\u0d07'+sec_word[j+2:]
                                        print h
                                        g=g.encode('UTF-8')
                                        h=h.encode('UTF-8')
                                    first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')
                       
 #108---- kkaayirunnu----#
                           elif(unidata[i]==U'\u0d15'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' ):
                                       print "code 108"
                                        if(var==1):
                                                    x=unidata[0:i+1]+ ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                        
                                    first_word=unidata[0:i+1]
                                    sec_word=U'\u0d06'+unidata[i+2:len(unidata)] 
                    
                                         var=0
                                          
                                           first_word=first_word.encode('UTF-8')
                                           sec_word=sec_word.encode('UTF-8')
                                       


                                      
#109----- raayirunnu---- #
                              elif(unidata[i]==U'\u0d30 \u0d31'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' ):
                              print "code 109"
                                        if(var==1):
                                            x=unidata[0:i]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                           first_word=unidata[0:i]+U'\u0d4d'
                                           sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                    var=0
                
                                   first_word=first_word.encode('UTF-8')
                                   sec_word=sec_word.encode('UTF-8')

#110----- thaayirunnu---- #
                           elif(unidata[i]==U'\u0d24'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' ):
                                print "code 110"
                                       if(var==1):
                                            x=unidata[0:i+1]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                             first_word=unidata[0:i+1]+U'\u0d4d'
                                            sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                     var=0
                
                                    first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')
                    

#111.----- vaayirunnu---- #
                           elif(unidata[i]==U'\u0d35'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' ):
                            print "code 111"
                                       if(var==1):
                                                 x=unidata[0:i]+ U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                            
                                                first_word=unidata[0:i]+ U'\u0d4d'
                                                sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                            var=0
                
                                        first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')


#112.----- naayirunnu---- #
                           elif(unidata[i]==U'\u0d28'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' ):
                            print "code 112"
                                       if(var==1):
                                            x=unidata[0:i]+U'\u0d7b' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                            
                        
                                            first_word=unidata[0:i]+U'\u0d7b'
                                           sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                    
                                    var=0
                
                                   first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8')
#113.----- laayirunnu----#

                           elif(unidata[i]==U'\u0d32'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' ):
                            print "code 113"
                                       if(var==1):
                                            x=unidata[0:i-1]+ U'\u0d3f' + U'\u0d7d' +' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i-1]+ U'\u0d3f'+ U'\u0d7d'
                                           sec_word=U'\u0d06'+unidata[i+2:len(unidata)] 
                                     var=0
                
                                    first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')
                    
 

#114---- Saayirunnu....#
                           elif(unidata[i]==U'\u0d36'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' ):
                            print "code 114"

                                       if(var==1):
                                            x=unidata[0:i+1]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                      
                                            first_word=unidata[0:i+1]+U'\u0d4d'
                                            sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                     var=0
                
                                    first_word=first_word.encode('UTF-8')
                                    sec_word=sec_word.encode('UTF-8')
#115.---yunntaayirunna----#
                              elif(unidata[i]==U'\u0d2f'  and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d28' and unidata[i+3]==U'\u0d4d'  and unidata[i+6]==U'\u0d1f' ):
                             print "code 115"
                                        if(var==1):
                                            x=unidata[0:i]+ ' + '+ U'\u0d09'+unidata[i+2:len(unidata)]
                    
                                             first_word=unidata[0:i]
                                            sec_word=U'\u0d09'+unidata[i+2:len(unidata)]  
                                    var=0
                
                                    first_word=first_word.encode('UTF-8')
                                   sec_word=sec_word.encode('UTF-8')
                   
                     
#116.---munntaayirunna----#
                           elif(unidata[i]==U'\u0d2e'  and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d28' and unidata[i+3]==U'\u0d4d'  and unidata[i+6]==U'\u0d1f' ):
                            print "code 116"
                                       if(var==1):
                                            x=unidata[0:i]+U'\u0d02'+ ' + '+ U'\u0d09'+unidata[i+2:len(unidata)]
                    
                                            first_word=unidata[0:i]+U'\u0d02'
                                           sec_word=U'\u0d09'+unidata[i+2:len(unidata)] 
                                    var=0
    
            
                                  first_word=first_word.encode('UTF-8')
                                   sec_word=sec_word.encode('UTF-8')
                   
                     

#123.kanakkaakkappetunnu
                           elif(unidata[i]==U'\u0d3e' and unidata[i+1]==U'\u0d15' and unidata[i+2]==U'\u0d4d' and unidata[i+3]==U'\u0d15' and unidata[i+4]==U'\u0d2a'):
                         print "code 123"
                                   if(var==1):
                                        x=unidata[0:i]+ U'\u0d4d'+ ' + ' +U'\u0d06'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i]+ U'\u0d4d'
                                       sec_word=U'\u0d06'+unidata[i+1:len(unidata)]  
                               var=0
                
                               first_word=first_word.encode('UTF-8')
                              sec_word=sec_word.encode('UTF-8')
                   


                    

#-126-- mennarriyappettunna----
                           elif(unidata[i-4]==U'\u0d2e' and unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d31' and unidata[i+2]==U'\u0d3f' and unidata[i+3]==U'\u0d2f'):
                        print "code 126"
                                   if(var==1):
                    
                            x=unidata[0:i-4]+ U'\u0d02'+ ' + ' +U'\u0d0e'+unidata[i-2:len(unidata)]
                                       first_word=unidata[0:i-4]+ U'\u0d02'
                    
                                      sec_word=U'\u0d0e'+unidata[i-2:len(unidata)]   
                                var=0
                
                              first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')
                   
#127--- nnarriyappettunna----
                           elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d31' and unidata[i+2]==U'\u0d3f' and unidata[i+3]==U'\u0d2f'):
                        print "code 127"
                                   if(var==1):
                   
                                        x=unidata[0:i+1]+ U'\u0d4d'+ ' + ' +U'\u0d05'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i+1]+ U'\u0d4d'
                    
                                       sec_word=U'\u0d05'+unidata[i+1:len(unidata)]  
                                var=0
                
                               first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')
                                       

                    
#137---munhtengilum----
                           elif(unidata[i-1]==U'\u0d2e' and unidata[i]==U'\u0d41' and unidata[i+1]==U'\u0d23' and unidata[i+2]==U'\u0d4d' and unidata[i+3]==U'\u0d1f'):
                        print "code 137"
                                   if(var==1):
                                        x=unidata[0:i-1]+U'\u0d02' +' + '+U'\u0d09'+unidata[i+1:len(unidata)]
                                         first_word=unidata[0:i-1]+U'\u0d02'
                   
                                        sec_word=U'\u0d09'+unidata[i+1:len(unidata)]  
                                var=0
                
                                first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
                    
#138---llunhtengilum----
          
                              elif(unidata[i-1]==U'\u0d33' and unidata[i]==U'\u0d41' and unidata[i+1]==U'\u0d23' and unidata[i+2]==U'\u0d4d' and unidata[i+3]==U'\u0d1f'):
                        print "code 138"
                                   if(var==1):
                                        x=unidata[0:i-1]+U'\u0d7e' +' + '+U'\u0d09'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i-1]+U'\u0d7e'
                   
                                       sec_word=U'\u0d09'+unidata[i+1:len(unidata)]  
                                var=0
                
                               first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')
                    
                           
                  
       
                                       

#143.---mazhiyunnu
                           elif(unidata[i]==U'\u0d2e' and unidata[i+1]==U'\u0d34' and unidata[i+2]==U'\u0d3f' ):
                        print "code 143"
                                   if(var==1):
                                       x=unidata[0:i]+U'\u0d02'+ ' + '+ U'\u0d05'+unidata[i+1:len(unidata)]
                                        first_word=unidata[0:i]+U'\u0d02'
                            
                                       sec_word=U'\u0d05'+unidata[i+1:len(unidata)]  
                                        var=0
                
                               first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')
                    

                    
                    

#151.---zhutunnath
                           elif(unidata[i]==U'\u0d34' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d24' and unidata[i+3]==U'\u0d41' and unidata[i+4]==U'\u0d28' and unidata[i+5]==U'\u0d4d' and unidata[i+6]==U'\u0d28'):
                         print "code 151"
                                   if(var==1):
                                        x=unidata[0:i-1] +U'\u0d4d'+' + '+ U'\u0d0e'+ unidata[i:len(unidata)]
                    
                                        first_word=unidata[0:i-1]+U'\u0d4d'
                                        sec_word=U'\u0d0e'+unidata[i:len(unidata)]  
                                        var=0
                        
                               first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
                   
#157.-----yunhaRththunna
                           elif(unidata[i]==U'\u0d2f' and  unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d23'and unidata[i+3]==U'\u0d7c' and unidata[i+4:i+7]==U'\u0d24\u0d4d\u0d24'):
                        print "code 157"
                                if(var==1):
                                        x=unidata[0:i]+  ' + '+U'\u0d09'+  unidata[i+2:len(unidata)]
                                       first_word=unidata[0:i]
                                      sec_word=U'\u0d09'+unidata[i+2:len(unidata)]  
                                        var=0
                        
                               first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')

#158.-----vunhaRththunna
                           elif(unidata[i]==U'\u0d35' and  unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d23'and unidata[i+3]==U'\u0d7c' and unidata[i+4:i+7]==U'\u0d24\u0d4d\u0d24'):
                        print "code 158"
                                if(var==1):
                                        x=unidata[0:i]+ U'\u0d4d'+ ' + '+U'\u0d09'+  unidata[i+2:len(unidata)]
                                       first_word=unidata[0:i]+ U'\u0d4d'
                                       sec_word=U'\u0d09'+unidata[i+2:len(unidata)]  
                                        var=0
                        
                               first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')
#159-----llunhaRththunna
                              elif(unidata[i]==U'\u0d33' and  unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d23'and unidata[i+3]==U'\u0d7c' and unidata[i+4:i+7]==U'\u0d24\u0d4d\u0d24'):
                         print "code 159"
                                if(var==1):
                                        x=unidata[0:i]+ U'\u0d7e'+ ' + '+U'\u0d09'+  unidata[i+2:len(unidata)]
                                        first_word=unidata[0:i]
                                       sec_word=U'\u0d06'+unidata[i+2:len(unidata)]  
                                        var=0
                        
                              first_word=first_word.encode('UTF-8')
                               sec_word=sec_word.encode('UTF-8')

# 166.vaSyatayaaR~nna
                           elif(unidata[i]==U'\u0d3e' and  unidata[i+1]==U'\u0d7c' and unidata[i+2:i+5]==U'\u0d28\u0d4d\u0d28'):
                        print "code 166"
                                if(var==1):
                                   if(unidata[i-1]==U'\u0d2f'):
                                        x=unidata[0:i-1]+ ' + '+U'\u0d06'+  unidata[i+1:len(unidata)]
                                           if(unidata[i-1]==U'\u0d2e'):
                                             x=unidata[0:i-1]+ U'\u0d02' + '+ '+U'\u0d06'+  unidata[i+1:len(unidata)]
                                             first_word=unidata[0:i-1]+ U'\u0d02' 
                                              sec_word=U'\u0d06'+  unidata[i:len(unidata)] 
                                            var=0
                          
                                     first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
# 169.ettippeTaavunna
                           elif(unidata[i-1]==U'\u0d3f' and unidata[i:i+3]==U'\u0d2a\u0d4d\u0d2a' and unidata[i+3]==U'\u0d46' and unidata[i+4]==U'\u0d1f'):
                      print "code 169"
                              if(var==1):
                    
                                   x=unidata[0:i]+ ' + ' +   unidata[i+2:len(unidata)]
                                    if(unidata[i+4:i+7]==U'\u0d1f\u0d4d\u0d1f'):
                         
                                         x=unidata[0:i+7]+U'\u0d4d' + ' + ' +U'\u0d07' +   unidata[i+8:len(unidata)]
                                          first_word=unidata[0:i+7]+U'\u0d4d' 
                                           sec_word=U'\u0d07'+  unidata[i:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8')
#176.viLiccootunna
                           elif(unidata[i:i+3]==U'\u0d1a\u0d4d\u0d1a' and unidata[i+3]==U'\u0d4b' and unidata[i+4]==U'\u0d24' and unidata[i+5]==U'\u0d41' and unidata[i+6:i+9]==U'\u0d28\u0d4d\u0d28'         ):
                      print "code 176"
                              if(var==1):
                    
                                    x=unidata[0:i+3]+U'\u0d4d'+ ' + ' +U'\u0d13' +   unidata[i+4:len(unidata)]
                                    first_word=unidata[0:i+3]+U'\u0d4d' 
                                       sec_word=U'\u0d06'+  unidata[i:len(unidata)] 
                                    var=0
                          
                             first_word=first_word.encode('UTF-8')
                             sec_word=sec_word.encode('UTF-8')
#180.  kaattirunna
                                  elif(unidata[i:i+3]==U'\u0d24\u0d4d\u0d24' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' and unidata[i+5]==U'\u0d41'):
                      print "code 180"
                                      if(var==1):
                   
                                        x=unidata[0:i+3]+ U'\u0d4d' + ' + '+U'\u0d07' +   unidata[i+4:len(unidata)]
                   
                                        first_word=unidata[0:i+3]+ U'\u0d4d' 
                                           sec_word=U'\u0d07'+  unidata[i+4:len(unidata)] 
                                        var=0
                          
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
 #202.naTakkaanirikkunna
                           elif(unidata[i]==U'\u0d3e' and unidata[i+1]==U'\u0d28' and unidata[i+2]==U'\u0d3f' and unidata[i+3]==U'\u0d30' and unidata[i+4]==U'\u0d3f'):
                       print "code 202"
                               if(var==1):
                    
                                        x=unidata[0:i+1]+ U'\u0d7b '+' + '+ U'\u0d07'+unidata[i+3:len(unidata)]
                                         first_word=unidata[0:i+1]+ U'\u0d7b ' 
                                          sec_word=U'\u0d07'+  unidata[i+3:len(unidata)] 
                                       var=0
                          
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
#204.---- varumpoozhaayirunnu.#
                           elif(unidata[i]==U'\u0d34'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' ):
                        print "code 204"
                                   if(var==1):
                                        x=unidata[0:i+1]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                     
                      
                                        first_word=unidata[0:i+1]+U'\u0d4d' 
                                           sec_word=U'\u0d06'+  unidata[i+2:len(unidata)] 
                                var=0
                  
                                 first_word=first_word.encode('UTF-8')
                                sec_word=sec_word.encode('UTF-8')
 #209.ozhivaayat
                           elif(unidata[i]==U'\u0d35'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d24'):
                        print "code 209"
                                   if(var==1):
                                        x=unidata[0:i+1]+ U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i+1]+ U'\u0d4d' 
                                           sec_word=U'\u0d06'+  unidata[i+2:len(unidata)] 
                    
                                var=0
                  
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
 #213. mumpaayirunnu
                           elif(unidata[i:i+3]==U'\u0d2e\u0d4d\u0d2a'  and unidata[i+3]==U'\u0d3e' and unidata[i+4]==U'\u0d2f' and unidata[i+5]==U'\u0d3f' ):
                        print "code 213"
                                   if(var==1):
                                        x=unidata[0:i+3]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+4:len(unidata)]
                                   
                      
                                         first_word=unidata[0:i+3]+U'\u0d4d' 
                                           sec_word=U'\u0d06'+  unidata[i+4:len(unidata)] 
                                var=0
                  
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
#218---- saayirunnu----#
                           elif(unidata[i]==U'\u0d38'  and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3f' and unidata[i+4]==U'\u0d30' ):
                        print "code 218"
                   
                                    if(var==1):
                                        x=unidata[0:i+1]+U'\u0d4d' + ' + '+ U'\u0d06'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i+1]+U'\u0d4d' 
                                           sec_word=U'\u0d06'+  unidata[i+2:len(unidata)] 
                                var=0
                      
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
  #220.vipaNiyiliRakki
                              elif(unidata[i]==U'\u0d32' and unidata[i+1]==U'\u0d3f'  and unidata[i+2]==U'\u0d31' and unidata[i+3:i+6]==U'\u0d15\u0d4d\u0d15' ):
                                   print "code 220"
                                    if(var==1):
                                        x=unidata[0:i]+U'\u0d7d' + ' + '+ U'\u0d07'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i]+U'\u0d7d' 
                                           sec_word=U'\u0d07'+  unidata[i+2:len(unidata)] 
                                var=0
                      
                                 first_word=first_word.encode('UTF-8')
                                 sec_word=sec_word.encode('UTF-8')
#234.munnileekkettikkunna
                           elif(unidata[i:i+3]==U'\u0d15\u0d4d\u0d15' and unidata[i+3]==U'\u0d46'  and unidata[i+4:i+7]==U'\u0d24\u0d4d\u0d24'  and unidata[i+7]==U'\u0d3f' ):
                                    print "code 234"
                                    if(var==1):
                                            x=unidata[0:i+3]+U'\u0d4d' + ' + '+ U'\u0d0e'+unidata[i+4:len(unidata)]
                                             first_word=unidata[0:i+3]+U'\u0d4d'  
                                              sec_word=U'\u0d0e'+  unidata[i+4:len(unidata)] 
                                       var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
#238. manassaRiyunna
                           elif(unidata[i:i+3]==U'\u0d38\u0d4d\u0d38' and unidata[i+3]==U'\u0d31'    and unidata[i+4]==U'\u0d3f' and unidata[i+5]==U'\u0d2f'):
                                    print "code 238"
                                    if(var==1):
                                            x=unidata[0:i+3]+U'\u0d4d' + ' + '+ U'\u0d05'+unidata[i+3:len(unidata)]
                                             first_word=unidata[0:i+3]+U'\u0d4d' 
                                               sec_word=U'\u0d05'+ unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                     sec_word=sec_word.encode('UTF-8')
# 255.cuuNTikkaaTTunnu
                           elif(unidata[i]==U'\u0d23' and unidata[i+1]==U'\u0d4d'and unidata[i+2]==U'\u0d1f' and unidata[i+3]==U'\u0d3f'  and unidata[i+4:i+7]==U'\u0d15\u0d4d\u0d15' and unidata[i+7]==U'\u0d3e'):
                                    print "code 255"
                                    if(var==1):
                                            x=unidata[0:i+4]+  ' + '+unidata[i+6:len(unidata)]
                                             first_word=unidata[0:i+4] 
                                               sec_word= unidata[i+6:len(unidata)] 
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
# 257.tiriccetti
                           elif(unidata[i-2]==U'\u0d1a' and unidata[i-1]==U'\u0d4d' and unidata[i]==U'\u0d1a' and unidata[i+1]==U'\u0d46' and unidata[i+2:i+5]==U'\u0d24\u0d4d\u0d24' ):
                                      print "code 257"
                                       if(var==1):
                                            x=unidata[0:i+1]+U'\u0d4d'+' + '+U'\u0d0e'+unidata[i+2:len(unidata)]
                                             first_word=unidata[0:i+1]+U'\u0d4d' 
                                               sec_word=U'\u0d0e'+  unidata[i+2:len(unidata)] 
                                       var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')

#265.ellathinumupari

                  
                           elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d2e' and unidata[i+3]==U'\u0d41' and unidata[i+4]==U'\u0d2a'):
                        print "code 265"
                                 if(var==1):
                                         x=unidata[0:i+2]+U'\u0d02'+' + '+U'\u0d09'+unidata[i+4:len(unidata)]
                                          first_word=unidata[0:i+2]+U'\u0d02' 
                                         sec_word=U'\u0d09'+  unidata[i+4:len(unidata)]  
                                 var=0
             
                                  first_word=first_word.encode('UTF-8')
    
                                  sec_word=sec_word.encode('UTF-8')
#267.ishtamaayi
                                  elif(unidata[i]==U'\u0d1f' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f' and unidata[i+4]==U'\u0d3f'):
                                    print "code 266"
                                    if(var==1):
                                                    x=unidata[0:i+1] +U'\u0d02'+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#268.moshtichathaano

                           elif(unidata[i]==U'\u0d24' and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d23' and unidata[i+3]==U'\u0d4b'):
                        print "code 265"
                                 if(var==1):
                                         x=unidata[0:i+1]+U'\u0d4d'+' + '+U'\u0d06'+unidata[i+2:len(unidata)]
                                          first_word=unidata[0:i+1]+U'\u0d4d' 
                                         sec_word=U'\u0d06'+  unidata[i+2:len(unidata)]  
                                 var=0
             
                                  first_word=first_word.encode('UTF-8')
    
                                  sec_word=sec_word.encode('UTF-8')
                              elif(unidata[i]==U'\u0d32' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d19' and unidata[i+4]==U'\u0d4d' and unidata[i+5]==U'\u0d19'):
                        print "code 270"
                                 if(var==1):
                                         x=unidata[0:i]+U'\u0d7d'+' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                          first_word=unidata[0:i]+U'\u0d7d' 
                                         sec_word=U'\u0d09'+  unidata[i+2:len(unidata)]  
                                  var=0
             
                                  first_word=first_word.encode('UTF-8')
    
                                  sec_word=sec_word.encode('UTF-8')
           
                           elif(unidata[i]==U'\u0d35' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d19' and unidata[i+4]==U'\u0d4d' and unidata[i+5]==U'\u0d19'):
                         print "code 271"
                                 if(var==1):
                                         x=unidata[0:i+1]+U'\u0d4d'+' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i+1]+U'\u0d4d' 
                                        sec_word=U'\u0d09'+  unidata[i+5:len(unidata)]  
                                 var=0
             
                                 first_word=first_word.encode('UTF-8')
    
                                 sec_word=sec_word.encode('UTF-8')
                 
              
                           elif(unidata[i]==U'\u0d30' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d19' and unidata[i+4]==U'\u0d4d' and unidata[i+5]==U'\u0d19'):
                         print "code 272"
                                 if(var==1):
                                         x=unidata[0:i]+U'\u0d7c'+' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i]+U'\u0d7c' 
                                        sec_word=U'\u0d09'+  unidata[i+2:len(unidata)]  
                                var=0
             
                                first_word=first_word.encode('UTF-8')
    
                                 sec_word=sec_word.encode('UTF-8')
               
                           elif(unidata[i]==U'\u0d33' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d19' and unidata[i+4]==U'\u0d4d' and unidata[i+5]==U'\u0d19'):
                        print "code 273"
                                 if(var==1):
                                         x=unidata[0:i]+U'\u0d7e'+' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i]+U'\u0d7e' 
                                           sec_word=U'\u0d09'+  unidata[i+2:len(unidata)]  
                                 var=0
             
                                 first_word=first_word.encode('UTF-8')
    
                                 sec_word=sec_word.encode('UTF-8')
                
                           elif(unidata[i]==U'\u0d15' and unidata[i+1]==U'\u0d41' and unidata[i+2]==U'\u0d31' and unidata[i+3]==U'\u0d19' and unidata[i+4]==U'\u0d4d' and unidata[i+5]==U'\u0d19'):
                        print "code 274"
                                 if(var==1):
                                         x=unidata[0:i+1]+U'\u0d4d'+' + '+U'\u0d09'+unidata[i+2:len(unidata)]
                                         first_word=unidata[0:i+1]+U'\u0d4d' 
                                        sec_word=U'\u0d7e'+  unidata[i+3:len(unidata)]  
                                 var=0
             
                                 first_word=first_word.encode('UTF-8')
    
                                sec_word=sec_word.encode('UTF-8')
               

       
#278.aayirikkunnu
                                  elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d3f' and unidata[i+2]==U'\u0d30' and unidata[i+3]==U'\u0d3f'):
                                    print "code 278"
                                    if(var==1):
                                            x=unidata[0:i]+' + '+U'\u0d07'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i] 
                                               sec_word=U'\u0d07'+  unidata[i+2:len(unidata)] 
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#280.palayidathayi
                                  elif(unidata[i-1]==U'\u0d2a' and unidata[i]==U'\u0d32' and unidata[i+1]==U'\u0d2f' and unidata[i+2]==U'\u0d3f' and unidata[i+3]==U'\u0d1f'):
                                    print "code 280"
                                    if(var==1):
                                            x=unidata[0:i+1]+' + '+U'\u0d07'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] 
                                               sec_word=U'\u0d07'+  unidata[i+3:len(unidata)] 
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#283.manoharamaayi
                              elif(unidata[i]==U'\u0d39' and  unidata[i+1]==U'\u0d30' and  unidata[i+2]==U'\u0d2e'  and unidata[i+3]==U'\u0d3e' and unidata[i+3]==U'\u0d2f'):
                                   print "code 283"
                                    if(var==1):
                                        x=unidata[0:i+1]+ U'\u0d02' + ' + '+U'\u0d06'+unidata[i+3:len(unidata)]
 
                                 
                                        first_word=unidata[0:i+1]+U'\u0d02'
                                           

                            sec_word=U'\u0d06'+unidata[i+3:len(unidata)]
                    
                        
                       
                                var=0
                                first_word=first_word.encode('UTF-8')
        
                               sec_word=sec_word.encode('UTF-8')
#285.nalloru
                              elif(unidata[i]==U'\u0d32' and  unidata[i+1]==U'\u0d4d' and  unidata[i+2]==U'\u0d4a'):
                                   print "code 285"
                                    if(var==1):
                                        x=unidata[0:i+1]+ U'\u0d32' +' + '+U'\u0d12'+unidata[i+3:len(unidata)]
                                        
                            first_word=unidata[0:i+1]+ U'\u0d32' 
                                           

                            sec_word=U'\u0d12'+unidata[i+3:len(unidata)]
                    
                        
                       
                                var=0
                                first_word=first_word.encode('UTF-8')
        
                               sec_word=sec_word.encode('UTF-8')

#287.aakarshakamaayi

                              elif(unidata[i]==U'\u0d37' and  unidata[i+1]==U'\u0d15' and  unidata[i+2]==U'\u0d2e' and  unidata[i+3]==U'\u0d3e' and  unidata[i+4]==U'\u0d2f'):
                                   print "code 287"
                                    if(var==1):
                                        x=unidata[0:i+2]+ U'\u0d02'  +' + '+U'\u0d06'+unidata[i+4:len(unidata)]
                                        
                            first_word=unidata[0:i+2]+ U'\u0d02'
                                           

                            sec_word=U'\u0d06'+unidata[i+4:len(unidata)]
                    
                        
                       
                                var=0
                                first_word=first_word.encode('UTF-8')
        
                               sec_word=sec_word.encode('UTF-8')
#288.poorthiyaakkan
                               elif(unidata[i]==U'\u0d3f' and unidata[i+1]==U'\u0d2f' and unidata[i+2]==U'\u0d3e'):
                       print "code 288"
                                  if(var==1):
                    
                                        x=unidata[0:i+1]+ ' + ' +U'\u0d06' +   unidata[i+3:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i+1] 
                                            sec_word=U'\u0d06'+  unidata[i+3:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8')
#290.sundaramaaya
                               elif(unidata[i]==U'\u0d30' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e'  and unidata[i+3]==U'\u0d2f'):
                       print "code 290"
                                  if(var==1):
                    
                                        x=unidata[0:i+1]+ U'\u0d02' + ' + ' +U'\u0d06' +   unidata[i+3:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i+1]+ U'\u0d02'  
                                            sec_word=U'\u0d06'+  unidata[i+3:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8') 
#291.sathyasandhamaaya
                               elif(unidata[i]==U'\u0d27' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e'  and unidata[i+3]==U'\u0d2f'):
                       print "code 291"
                                  if(var==1):
                    
                                        x=unidata[0:i+1]+ U'\u0d02' + ' + ' +U'\u0d06' +   unidata[i+3:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i+1]+ U'\u0d02'  
                                            sec_word=U'\u0d06'+  unidata[i+3:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8') 

#293.vasyathayund
                               elif(unidata[i]==U'\u0d24' and unidata[i+1]==U'\u0d2f' and unidata[i+2]==U'\u0d41'):
                       print "code 293"
                                  if(var==1):
                    
                                        x=unidata[0:i+1] + ' + ' +U'\u0d09' +   unidata[i+3:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i+1]  
                                            sec_word=U'\u0d09'+  unidata[i+3:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8') 
#294.ithuvareyulla
                               elif(unidata[i]==U'\u0d46' and unidata[i+1]==U'\u0d30' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d41' and unidata[i+4]==U'\u0d33' and unidata[i+5]==U'\u0d4d' and unidata[i+6]==U'\u0d33'):
                       print "code 294"
                                  if(var==1):
                    
                                        x=unidata[0:i+2] + ' + ' +U'\u0d09' +   unidata[i+2:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i+2]  
                                            sec_word=U'\u0d09'+  unidata[i+2:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8') 
#295.kathayil
                               elif(unidata[i]==U'\u0d46' and unidata[i+1]==U'\u0d30' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d41'):
                       print "code 295"
                                  if(var==1):
                    
                                        x=unidata[0:i] + ' + ' +U'\u0d09' +   unidata[i+4:len(unidata)]
                                   
                        
                                          first_word=unidata[0:i]  
                                            sec_word=U'\u0d09'+  unidata[i+4:len(unidata)] 
                                        var=0
                          
                                  first_word=first_word.encode('UTF-8')
                                  sec_word=sec_word.encode('UTF-8') 
#297.nerkaazhchayyanu
                                  elif(unidata[i]==U'\u0d1a' and unidata[i+1]==U'\u0d2f' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d23' and unidata[i+4]==U'\u0d4d'):
                                    print "code 297"
                                    if(var==1):
                                            x=unidata[0:i+1]+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] 
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#298.korthinakkiya
                                  elif(unidata[i]==U'\u0d24' and unidata[i+1]==U'\u0d3f' and unidata[i+2]==U'\u0d23'):
                                    print "code 298"
                                    if(var==1):
                                            x=unidata[0:i+1]+ U'\u0d4d'+' + '+U'\u0d07'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i+1] + U'\u0d4d'
                                               sec_word=U'\u0d07'+  unidata[i+2:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#299.ithaanu
                                  elif(unidata[i]==U'\u0d24' and unidata[i+1]==U'\u0d3e' and unidata[i+2]==U'\u0d23'):
                                    print "code 298"
                                    if(var==1):
                                            x=unidata[0:i+1]+U'\u0d4d'+' + '+U'\u0d06'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d4d'
                                               sec_word=U'\u0d06'+  unidata[i+2:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#301.dayaneeyaavastha
                                  elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d40' and unidata[i+2]==U'\u0d2f' and unidata[i+3]==U'\u0d3e' and unidata[i+4]==U'\u0d35'):
                                    print "code 301"
                                    if(var==1):
                                            x=unidata[0:i+3]+' + '+U'\u0d05'+unidata[i+4:len(unidata)]
                                            first_word=unidata[0:i+3] 
                                               sec_word=U'\u0d05'+  unidata[i+4:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#302moshamaayilla
                                  elif(unidata[i]==U'\u0d36' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f' and unidata[i+4]==U'\u0d3f'):
                                    print "code 302"
                                    if(var==1):
                                                    x=unidata[0:i+1] +U'\u0d02'+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#304theekshnamaayi
                                  elif(unidata[i]==U'\u0d23' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f' and unidata[i+4]==U'\u0d3f'):
                                    print "code 304"
                                    if(var==1):
                                                    x=unidata[0:i+1] +U'\u0d02'+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#305moshamallathe
                                  elif(unidata[i]==U'\u0d36' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d32' and unidata[i+3]==U'\u0d4d' and unidata[i+4]==U'\u0d32'):
                                    print "code 305"
                                    if(var==1):
                                                    x=unidata[0:i+1] +U'\u0d02'+' + '+U'\u0d05'+unidata[i+2:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d02'
                                               sec_word=U'\u0d05'+  unidata[i+2:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#311prasakthamaaya
                           elif(unidata[i]==U'\u0d24' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f'):
                       print "code 311"
                                if(var==1):
                    
                                                    x=unidata[0:i+1] +U'\u0d02'+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1] +U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#312.nannayi
                           elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d4d' and unidata[i+2]==U'\u0d28' and unidata[i+3]==U'\u0d3e' and unidata[i+4]==U'\u0d2f'):
                       print "code 312"
                                if(var==1):
                    
                                                    x=unidata[0:i+2] +' + '+U'\u0d06'+unidata[i+4:len(unidata)]
                                            first_word=unidata[0:i+2]
                                               sec_word=U'\u0d06'+  unidata[i+4:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#315.thanneyaanu
                           elif(unidata[i]==U'\u0d28' and unidata[i+1]==U'\u0d4d' and unidata[i+2]==U'\u0d46' and unidata[i+3]==U'\u0d28' and unidata[i+4]==U'\u0d2f' and unidata[i+5]==U'\u0d3e' and unidata[i+6]==U'\u0d23' and unidata[i+7]==U'\u0d4d'):
                       print "code 315"
                                if(var==1):
                    
                                                    x=unidata[0:i+3] +' + '+U'\u0d06'+unidata[i+6:len(unidata)]
                                            first_word=unidata[0:i+3]
                                               sec_word=U'\u0d06'+  unidata[i+6:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#316.aakarshaneeyamaayi
                           elif(unidata[i]==U'\u0d2f' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f' and unidata[i+4]==U'\u0d3f'):
                       print "code 316"
                                if(var==1):
                    
                                                    x=unidata[0:i+1]+U'\u0d02' +' + '+U'\u0d06'+unidata[i+4:len(unidata)]
                                            first_word=unidata[0:i+1]+U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#317.onnantharamoru
                           elif(unidata[i]==U'\u0d30' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d4a' and unidata[i+3]==U'\u0d30' and unidata[i+4]==U'\u0d41'):
                       print "code 317"
                                if(var==1):
                    
                                                    x=unidata[0:i+1]+U'\u0d02' +' + '+U'\u0d12'+unidata[i+4:len(unidata)]
                                            first_word=unidata[0:i+1]+U'\u0d02'
                                               sec_word=U'\u0d12'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#319.nirmalamaaya
                           elif(unidata[i]==U'\u0d32' and unidata[i+1]==U'\u0d2e' and unidata[i+2]==U'\u0d3e' and unidata[i+3]==U'\u0d2f'):
                       print "code 319"
                                if(var==1):
                    
                                                    x=unidata[0:i+1]+U'\u0d02'+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                            first_word=unidata[0:i+1]+U'\u0d02'
                                               sec_word=U'\u0d06'+  unidata[i+3:len(unidata)]
                                    var=0
                      
                                     first_word=first_word.encode('UTF-8')
                                        sec_word=sec_word.encode('UTF-8')
#325.ennoru

                              elif(unidata[i]==U'\u0d28' and  unidata[i+1]==U'\u0d4d' and  unidata[i+2]==U'\u0d28'and  unidata[i+3]==U'\u0d4a' and  unidata[i+4]==U'\u0d30' and  unidata[i+5]==U'\u0d41'):
                                   print "code 325"
                                    if(var==1):
                                        x=unidata[0:i+3] +U'\u0d4d'+' + '+U'\u0d12'+unidata[i+4:len(unidata)]
                                        
                            first_word=unidata[0:i+3]+U'\u0d4d'
                                           

                            sec_word=U'\u0d12'+unidata[i+4:len(unidata)]
                    
                        
                       
                                var=0
                                first_word=first_word.encode('UTF-8')
        
                               sec_word=sec_word.encode('UTF-8')
#326.idayaayi
                              elif(unidata[i]==U'\u0d1f' and  unidata[i+1]==U'\u0d2f' and  unidata[i+2]==U'\u0d3e'and  unidata[i+3]==U'\u0d2f' and  unidata[i+4]==U'\u0d3f'):
                                   print "code 326"
                                    if(var==1):
                                        x=unidata[0:i+1]+' + '+U'\u0d06'+unidata[i+3:len(unidata)]
                                        
                            first_word=unidata[0:i+1]
                                           

                            sec_word=U'\u0d06'+unidata[i+3:len(unidata)]
                    
                        
                       
                                var=0
                                first_word=first_word.encode('UTF-8')
        
                               sec_word=sec_word.encode('UTF-8')
                 
                except IndexError ,  e:
                           err=""
      
        if(var!=0):
                 #print unidata
                   no_compound=unidata
            
                fw.write('\t')
                fw.write(no_compound.encode('UTF-8'))
                fw.write('\t')
            fw.write('\n')
            ft.write('\t')
                ft.write(no_compound.encode('UTF-8'))
                ft.write('\t')
            ft.write('\n')
        
        
        if(var==0):
        
                #print first_word
                       #print sec_word
            
                
                fw.write('\t')
                fw.write(first_word)
                       fw.write('\t')
   
                fw.write('\n')
                   ft.write('\t')
                ft.write(first_word)
                       ft.write('\t')
               
            fw.write('\t')
                fw.write(g)
                       fw.write('\t')
            fw.write('\t')
                fw.write(h)
                       fw.write('\t')
   
                ft.write('\n')
                
                fw.write('\t')
                fw.write(sec_word)
                fw.write('\t')
     
                fw.write('\n')
            ft.write('\t')
                ft.write(sec_word)
                ft.write('\t')
     
                ft.write('\n')
       
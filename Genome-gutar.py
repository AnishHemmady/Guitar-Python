'''
Main file



Copyright@BMRSoftwareGroupUSA 2017
'''
from Noder import Node
from algorithm import Skipping_method
from algorithm import Fretboard_mapping_algorithm

import pdb
class Genome(object):
	def __init__(self,arry_size):
		self.__inpt_arry_size=arry_size
		self.__inpt_arry=[None]*self.__inpt_arry_size
		
	def get_arry(self):
		return self.__inpt_arry
	
	def get_arry_size(self):
		return self.__inpt_arry_size
		
	def set_arry_size(self,size):
		self.__inpt_arry_size=size
		
	def set_new_arry(self):
		self.__inpt_arry=[None]*self.__inpt_arry_size
		
		
class Functionality():
	def __init__(self,new_input_arry,size):
		self.musical_node_array=new_input_arry
		self.musical_node_array_size=size
		
	def __enforce_rules(self,rule_lst):
		self.rules_lst=rule_lst
		self.val=len(self.rules_lst)
		return self.val
	
	def add_nodes_to_arry(self,lsty):
		value=len(lsty)
		for i in xrange(0,self.musical_node_array_size):
			rule_arry_loctn=i%value
			charctr=lsty[rule_arry_loctn]
			nde=Node(i)
			nde.set_name(charctr)
			self.musical_node_array[i]=nde
			
		return self.musical_node_array
			
class Work_it():
	
	def genome_runner(self,arry,strtgy,name):
		self.finl_arry=arry
		self.strtgy=strtgy
		self.nme=name
		skppng=Skipping_method(self.strtgy,self.nme)
		fnl_pstns=skppng.Skipping(self.finl_arry)
		return fnl_pstns
		

class Fretboard():
	def __init__(self):
		self.fretboard_array=[]
		self.rows=6
		self.columns=24
		self.guitar_string_postns=[0,24,48,72,96,120] #guitar string starting positions in the fretboard_array,0->(6-0,6-1,...),24->(5-0,5-1,...),...,116->(1-0,1-1,1-2,...)
		self.standard_tuning=[44,39,35,30,25,20]
		self.mapping_gitr_std_tune={}
		self.countr=[0,0,0,0,0,0]
		
	def insert_into_strng(self,postn,fret_arry,v):
		
		base=self.guitar_string_postns[v]
		if v==0 and self.countr[0]<24:
			#pdb.set_trace()
			offset_from_base=self.countr[0]+base
			fret_arry[offset_from_base]=postn
			self.countr[0]+=1
			
		if v==1 and self.countr[1]<24:
			offset_from_base=self.countr[1]+base
			fret_arry[offset_from_base]=postn
			self.countr[1]+=1
		if v==2 and self.countr[2]<24:
			offset_from_base=self.countr[2]+base
			fret_arry[offset_from_base]=postn
			self.countr[2]+=1
			
		if v==3 and self.countr[3]<24:
			offset_from_base=self.countr[3]+base
			fret_arry[offset_from_base]=postn
			self.countr[3]+=1
			
		if v==4 and self.countr[4]<24:
			offset_from_base=self.countr[4]+base
			fret_arry[offset_from_base]=postn
			self.countr[4]+=1
			
		if v==5 and self.countr[5]<24:
			offset_from_base=self.countr[5]+base
			fret_arry[offset_from_base]=postn
			self.countr[5]+=1
				
		
	def create_fretboard(self,fret_array,points,F_objct):
		
		
		fretboard_grid=[[0 for i in xrange(0,self.columns)]for j in xrange(0,self.rows)]
		
		
		
		for i in range(0,len(self.guitar_string_postns)):
			self.mapping_gitr_std_tune[self.guitar_string_postns[i]]=self.standard_tuning[i]
			
		#print self.mapping_gitr_std_tune
		v=None
		
		for m in points:
			n=m.get_id()
			if n>=44:
				v=0
				self.insert_into_strng(m,fret_array,v)
			elif (n-self.mapping_gitr_std_tune[24])<=4 and (n-self.mapping_gitr_std_tune[24])>=0:
				v=1
				self.insert_into_strng(m,fret_array,v)
			elif (n-self.mapping_gitr_std_tune[48])<=5 and (n-self.mapping_gitr_std_tune[48])>=0:
				v=2
				self.insert_into_strng(m,fret_array,v)
			elif (n-self.mapping_gitr_std_tune[72])<=5 and (n-self.mapping_gitr_std_tune[72])>=0:
				v=3
				self.insert_into_strng(m,fret_array,v)
			elif (n-self.mapping_gitr_std_tune[96])<=5 and (n-self.mapping_gitr_std_tune[96])>=0:
				v=4
				self.insert_into_strng(m,fret_array,v)
			elif (n-self.mapping_gitr_std_tune[120])<=5 and (n-self.mapping_gitr_std_tune[120])>=0:
				v=5
				self.insert_into_strng(m,fret_array,v)
			
		offset=None
		k=24
		
		gutr_potns=self.guitar_string_postns[2:]
		while(k<len(fret_array)):
			if k==24:
				offset=4
				k+=offset
				base=0
			elif k in gutr_potns:
				offset=5
				k+=offset
			else:
				rem=k%24
				prev_strng_pos=(k/24)-1
				valu=rem-offset+self.guitar_string_postns[prev_strng_pos]
				if fret_array[valu]!=None:
					fret_array[k]=fret_array[valu]
				k+=1
				
		#print fret_array
			
		for i in range(0,len(fret_array)):
			x_y_pair=F_objct.rmo_x_y(i)
			x1=x_y_pair[0]
			y1=x_y_pair[1]
			if fret_array[i]!=None:
				fretboard_grid[x1][y1]=fret_array[i].get_id()
				fret_array[i].set_x(x1)
				fret_array[i].set_y(y1)
			else:
				fretboard_grid[x1][y1]=fret_array[i]
			
			
			
		for i in fretboard_grid:
			print(i)
			
				
		
		
		
				
def main():
	arry_size=int(raw_input("enter size: "))
	scale=raw_input("enter scale:")
	G=Genome(arry_size)
	arry=G.get_arry()
	F=Functionality(arry,arry_size)
	rule=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
	new_arry=F.add_nodes_to_arry(rule)
	for m in new_arry:
		print m.get_name(),
	print(' ')
	W=Work_it()
	fnl=W.genome_runner(new_arry,'Major',scale)
	
	fret_map=Fretboard_mapping_algorithm(6,24)
	fret_array_1d=fret_map.create_1d_map()
	F=Fretboard()
	F.create_fretboard(fret_array_1d,fnl,fret_map)
	
if __name__=='__main__':
	main()
	
	
		
		
		
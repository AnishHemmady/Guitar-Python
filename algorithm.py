'''
Developing different algorithms for the main file.



Copyright@BMRSoftwareGroup USA 2017
'''
#Here we make use of strategy pattern since its family of algorithms.
import pdb
class Skipper(object):
	def algorithm(self,inp,user_inpt):
		return "Not Implemented"
		
class Major(Skipper):
	def seek_solver(self,inp_arry,strt_pos,rev,seq):
		#pdb.set_trace()
		if rev==0:
			self.sequence=seq
			self.leng_seq=len(self.sequence)
			i=strt_pos
			out_postns=[]
			k=0
			while(i<len(inp_arry)):
				if(k>len(self.sequence)):
					k=0
				else:
					seq_pos=k%self.leng_seq
					if self.sequence[seq_pos]=='W':
						out_postns.append(inp_arry[i])
						i+=2
					elif self.sequence[seq_pos]=='H':
						out_postns.append(inp_arry[i])
						i+=1
					k+=1
		else:
			#pdb.set_trace()
			self.sequence=seq[::-1]
			self.leng_seq=len(self.sequence)
			i=strt_pos
			out_postns=[]
			k=0
			while(i>=0):
				if(k>len(self.sequence)):
					k=0
				else:
					seq_pos=k%self.leng_seq
					if self.sequence[seq_pos]=='W':
						if i!=strt_pos:
							out_postns.append(inp_arry[i])
						i-=2
					elif self.sequence[seq_pos]=='H':
						if i!=strt_pos:
							out_postns.append(inp_arry[i])
						i-=1
					k+=1
		return out_postns
			
	def seek_forward_bckwrd(self,inp_arry,strt_pos):
		self.seq_major=['W','W','H','W','W','W','H']
		frwd_postns_arry=self.seek_solver(inp_arry,strt_pos,0,self.seq_major)
		bckwrd_postns_arry=self.seek_solver(inp_arry,strt_pos,1,self.seq_major)
		totl_postns=frwd_postns_arry+bckwrd_postns_arry
		return totl_postns
		
	
	def algorithm(self,inp_arry,user_inpt):
		for nde in inp_arry:
			if nde.get_name()==user_inpt:
				strtng_pos=nde.get_id()
				break
		posns=self.seek_forward_bckwrd(inp_arry,strtng_pos)
		return posns
	

class Fretboard_mapping_algorithm():
	def __init__(self,rows,cols):
		self.rows=rows
		self.cols=cols
		
		
	def create_1d_map(self):
		self.one_map=[None]*self.rows*self.cols
		return self.one_map
		
	#get index using row-major order in one dimensional map
	def rmo_indx(self,x,y):
		indx=self.cols*x+y
		return indx
	
	#getting x,y coordinates translated from fretboard array [1-d array]
	def rmo_x_y(self,indx):
		x=int(indx/self.cols)
		y=indx-(x*self.cols)
		return[x,y]
			
class Skipping_method:
	def __init__(self,strategy,user_inpt):
		if strategy=='Major':
			self.strategy=Major()
		else:
			self.strategy=Skipper()
		
		self.user_inp=user_inpt
		
	def Skipping(self,inpt_arry):
		postns=self.strategy.algorithm(inpt_arry,self.user_inp)
		return postns
		
	def change_algo(self,strategy):
		if strategy=='Major':
			self.strategy=Major()
		else:
			self.strategy=Skipper()
			
def main():
	skp=Skipping_method()
	
if __name__=='__main__':
	main()
		
		
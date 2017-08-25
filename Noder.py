'''
This file controls individual Node properties,You can have getters and setters here and various functions for Node Object.


 
Copyright@BMRSoftwareGroupUSA 2017

'''

class Node(object):
	def __init__(self,id):
		#make variables private
		self.__id=id
		self.__name=None
		self.__x=None
		self.__y=None
		
	#setter to set the symbol associated with each node
	def set_name(self,name):
		self.__name=name
		
	#getter to get name associated with that node
	def get_name(self):
		return self.__name
		
	def get_id(self):
		return self.__id
	
	def set_id(self,id):
		self.__id=id
		
	def set_x(self,x):
		self.__x=x
		
	def set_y(self,y):
		self.__y=y
		
	def get_x(self):
		return self.__x
		
	def get_y(self):
		return self.__y
	
	
def main():
	nde=Node(0)
	
if __name__=='__main__':
	main()
		
		
	
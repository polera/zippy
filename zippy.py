from zipfile import ZipFile, ZIP_STORED
from os.path import isdir
from os import walk, sep

class Zip(ZipFile):
	def __init__(self, filename, noisy=False, compression=ZIP_STORED):
		self.file  = ZipFile(filename, "w", compression)
		self.noisy = noisy

	def add_files(self, files=[]):
	    if self.noisy:
	        print files
		for filename in files:
			if self.noisy:
				print "Adding file %s" % filename
            
			if isdir(filename):
				for (dirname,dirs,filenames) in walk(filename):
					self.add_files(map(lambda x: "%s%s%s" % (dirname,sep,x),filenames))
			else:
			    self.file.write(filename)

class Unzip(ZipFile):
	def get_contents(self):
		return self.namelist()
	contents = property(get_contents)
	
	def to_path(self, path):
		try:
			self.extractall(path)
			return True
		except (IOError, WindowsError):
			print "Could not extract %s to %s" % (self.filename, path)
			return False
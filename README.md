zippy
==
Zippy is a wrapper library for the Python ZipFile library. Makes things a little easier.

Author
==
James Polera <james@listbot.org>

Usage
==

zipping files and/or directories
--
* Zippy's Zip takes the name of a .zip file to create.
* The add_files method takes a list of files and/or directories.
i.e.:

    from zippy.zippy import Zip
    Zip('name_of_zipfile.zip').add_files(['your_directory'])
    Zip('name_of_other_zipfile.zip').add_files(['file3.txt'])
  
unzipping files
--
* Zippy's Unzip takes the name of a .zip file to open.
* The "contents" property returns a list of the .zip file's contents.
* The to_path method takes the name of a path to extract the .zip file to.  It returns
  True on success, False on failure.
i.e.:

    from zippy.zippy import Unzip
    Unzip('name_of_zipfile.zip').to_path('/home/you/your_extracted_files')
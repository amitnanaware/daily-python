# Repository for adding daily functions required in python e.g. get files from directory  

# File iterator-generator

get_files_from_directory() will iterate in the given folder and return the files with full path. The function take two parameters 1st is dirname and 2nd is exclude_dirs which is optional.

This function uses python's own os.walk() function. This is generator which is faster in bigger folders.

If exclude dirs is provided then files from the dirs are excluded from the output.
usage:

```
for filename in get_files_from_directory(dirname, exclude_dirs = []):
   print filename
```

Feel free to add such functions.

Its open to all!

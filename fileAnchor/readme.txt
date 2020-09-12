questions to determine version

0.0.0.0.0

0.1/1.0/1.
0.11.01.011.microversion

release
architecture/sectionCount
fileadded/filemodified
bugfix/enhancement/milestone
microversion

to get insert comment into devtask relating
to the reason the file was created or modified
retrieve the taskID, etc...

FILETRACKER
-----------

siteName=$parentDirectory

if the file has this on any page, extracts value
check if file exists in version database &  modify value is incremented+1

if not, the record is inserted & fileAdded is incremented

If you want other factors to be affected add other fields to top
use a pipe separator and explode later for multiple values


FILE STATES
----------
s = stable, p = work in progress, b = broken, 

*default fileLable
siteName = $parentDirectory | p 

*options - exploded on pipe
siteName = $parentDirectory | p | $addMore = likeThis


VISUAL & INTERACTION
--------------------
window inside sublime to toggle the values
value window can be auto toggled on during file open process
but only if topLevel directory matches the $siteName

TOGGLEABLE
----------
When creating a new file, how can we know if the 
autoStamp at top of page should be applied?

Problem: New Files have no location, no way to know where the user
will save it in the long run

Question: Is there a way to detect a non-existent string in a monitored
directory AFTER the save?  Any way to check the surrounding files and perform operation after save?

TESTS
-----

Make a new repo for sublimeFiles | Package in Sublime

ALTERNATIVE NAMES
-----------------

fileCraft,fileFanatic,fileTastic,fileDroid,

ALGORITHM CONSIDERATIONS
------------------------

To start local versioning, save a copy of a file into the a0ld directory named 

## python how to get current extension from filename
-- print(os.path.splitext("/path/to/some/file.txt")[0])

currentFile.'_v1n_'.current extension
anchorTrack=os.path.splitext(currentFile)




currentFile.'_v1n_'.$extension

check for existence of 
and after so much time auto resave it with current fileState depending on keystrokes logged on that 
particular file

	* Auto shutoff
		after X time frame
		the file is saved in stalled status

	* Can be woken up after keyStrokes to the file

	* Needs to have setting to complete disable if desired


IMPORTANT FEATURE
-----------------
need a way to remark if file is good
example of something harder to remember
needs like a sticky attribute


STATUSES
--------




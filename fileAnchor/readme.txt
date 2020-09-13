#<! 30 !>#
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


IMPORTANT FEATURES
-----------------
need a way to remark if file is good
example of something harder to remember
needs like a sticky attribute
-----------------
Precreate version# as far ahead as you can,
after version expectation is created, add the change
as a ticket, that when completed will follow up 
and add tags to git as well
-----------------


OUTLINE OF LOGIC
----------------
Releases are comprised of x number of milestones
milestones include all associated devtasks for that milestone

Begin by adding a milestone and a description of the end result
and insert into milestone database

The milestone will have an ID.  ALL devtasks should be required
to have milestoneID to generate

Example.
________


GENERAL:
	
	COMMENT: A General category will help to notate 
	things that dont belong to part of versioning 
	or milestones

	STALLED_NOTE: Contemplation of the iteration of 
	the line by line read of a file to determine the ID# 
	and which tag belongs to which.  Also, I'm really wanting to 
	see this data in graphical, interactive vew, but also
	need to keep writing to identify patterns that need to be
	accounted for.  Also, rather than just creating tables manually in mySQL,
	I want to use the exercise to create a programmatic way
	for the future.

	DO_THIS: 
		TASK: Manually make the tables needed for the 
		mySQLuv plugin
			

	Q: How can I insert a task that is wrapped inside a metatag?
	
	PONDERING: 
		OPTION: Best way to parse through a text document
		for insertion into mySQL
		OPTION: Need easy way to create mySQL tables from
		within sublime text
		OPTION: Need Notation for anchor brackets when 
		its an enhancement vs a new feature

	IDEA: When ideas metatag is populated outside of a Version parent
	have option to use it as a launch point for a new version
	template if warranted

	ISSUE: Need to correct the starting point in the v.012
	to basically register fileAnchor itself as a plugin
		NOTE: This would be a good way to expore how
		to retrieve a version number from a file stored in
		the a0ld folder.

	Q: Do comments need to be setup to show by default? Or should they 
	be set up more like hidden with a notice indicator badge?
		COMMENT: Too soon to tell, you dont even have a single
		visual idea of how this thing looks, slow down about this
		idea for now


VERSION: v.012

	RELEASE_NOTES: New Feature <! fileAnchor !> Create a new interface and/or script to interact 
	with versions & milestones.  Version should be topLevel and dispay outstanding milestones.  You could
	enter into a milestone by clicking to examine the status and progress.
	When milestones are completed, a part of the version # is incremented, and the milestone 
	is sorted away from active milestones.  When ALL milestones are complete, the VERSION is released
	Follow through to git with tags,versions,etc.

	MILESTONE: Initial Setup
		LEARN: How to get a clean right click menu with customized options
		
	IDEA: Architecture must have relationships in models
	ISSUE: The architecture should account for each <! New Feature !> having its own version number.
	
	ISSUE:Need a way to isolate entirety of site from its counterparts
		NOTE: When saving files, check the a0ld folder for a file for most recent modified date
		STALL:1
		RESOLVED:1

	Q: Is it necessary to store the saved masterPlan file that was already 
	imported into mysql for any reason?
		Comment: As a just in case, you could archive them.

	ISSUE: For the stalled, resolved situation, keep count somewhere, somehow

	ISSUE: Must have a way to properly escape colons in order to figure out a
	working regex.
		COMMENT: This seems to happen most frequently when the tag is mimicked
		in an example to reference the metatags and illustrate the point.

	MILESTONE: Right click menu from sublime to offer new menu options

		ISSUE: Can the default right click menu be wiped clean for full customization?

		TASK: Create rule to be sure only if current directory is enabled

		TASK: Bug Report should accept highlighted text and add to errorLog
			COMMENT: mplnerror.log for file

		TASK: Add Versioner Menu Option
			IDEA: When clicked, versioner scans the a0ld folder within its
			own directory for a file named `$currentFile.'_v1n_'.$currentExtension`
			if its not there, it add it.  If so, determine the current state

		TASK: Add MasterPlanner Menu Option
			IDEA: clicking will initiate an upload to mysql and render
			a the text into an interactive format

		TASK: Add mySQLuv Feature
			IDEA: Right click to create, edit tables inside sublime text
			Q: Can full forms be created or are only simple text fields 
			available one at a time?

	MILESTONE: Make the keyTracker increment how many times the file was saved
	and include it in the keystroke data reports

		TASK: Need fields for lastSaveDate,totalSaveCount,currentSaveCount

	ISSUE: How to include a synapsis of which FILES belong to which milestones?


VERSION: v.013

	RELEASE NOTES: Detect if current file is being versioned in a0ld folder
	If so, determine what state its at by scanning for various possiblities. 
	Depending on the state, the program will react with an appropriate response.
	
	COMMENT: Local versioning sytem that handles files locally.  
	Stores copies of the main file in various states to avoid useless commits
	for every minor detail.

	IDEA: log the URLS's visited in firefox or chrome
		Q: Can a script be written to extract text in the browser address bar?
		Q: What about extracting history from browsers
		for a specific timespan rather than monitor browser bar?

	IDEA: Each Keystroke should capture the file it was typed into, and a
	separate function will collect the data at specified intervals. Logic
	will react after so many keystrokes are typed into a file.

		COMMENT: function should be triggered from the keyTracker as 
		soon as the specified number is hit.  The files saved named
		should have an indicator as to whether it was saved by keytracker 
		or autotracker.

	MILESTONE: When file has had no keystrokes for a certain period,
	an auto version is saved as stalled, if one isnt already there,  
	One could manually review the stalled files and mark them as final version.


VERSION: v.014

	RELEASE_NOTES: New Feature <! Master Planner !> Parse text in readme.fanch to be prepped for addition to mysql database.
	Once inserted into the database a view can be created to show the text file as interactive tickets.
	Certain tickets will be recognized as release tickets.  When release tickets are marked as done,
	logic is set in motion to increment version locally as well as github.
	
	IDEA: The way to handle the Q: tag should be to show them somewhere conspicuous
	maybe even something like a rolling feed.  When you find the answer to an outstanding
	question, mark as such and keep daily track on things like questions answered, 
	issues resolved, etc.

	IDEA: When masterPlanner reads the data it can suggest the first 
	LEARN: tag or Q: tag it encounters to offer you a beneficial distraction
	of things that need figurin' out.  Warning, may trigger episodes of manic overachievement, 
	followed by long periods of extreme lethargy and burnout.

	NOTE: The initial import will serve to set up new entries for the plugins and the versions
	at the time of the call, but afterwards, enhancements,bugfixes,etc will need to trigger incrementing
	the version
		STALL:1

	MILESTONE: Create a master pluginData mysql table that includes every occurrence of 
	<! New Feature Name !>  Check against the pluginData table to see if a row 
	exists for the name.  If it does, enter the current version of that plugin.

		TASK: Make a table for pluginData and include all necessary fields

		NOTE: Since the example above uses the regex pattern, exclude it 
		from results that would otherwise create a record in the plugin module
		
		NOTE: To determine version go into files own a0ld directory folder
		and scan files.  Files will be setup with $fileName__$fileState.$extension
		By exploding the filename string you can read the variable after 
		the __ and before the next period.
	
	MILESTONE: INITIAL SETUP

		TASK: Make a database to include all fields needed for master planner
		TASK: Parse the sitePlan.mpln file and convert to json
		TASK: Take working json file and import into mysql database
		TASK: Make the system aware when all milestones are completed
			IDEA: If all milestones are completed, notification should prompt 
			if new version should be released.

	ENHANCE: Create Syntax for .mpln files
		LEARN: How to create syntax file for sublime text
		ACTIVE: 1

	Q: Does each module need its own version number for anything?
		A: No, the files themselves would have version references in their names
		when using the a0ld versioning plugin.
	Q: Can the file be parsed while open?

	IDEA: In addition to a right click option, file can be 
	scanned on demand, or possibly a timed function?
		COMMENT: Give option to turn off timed function
	IDEA: Issues should be classified as foreseen or unforeseen
		Q: Is there any way to detect this automatically?

	IDEA: Start by taking a simple file and converting to JSON
		Q:Does anything already exist to conver plain text to JSON?

	IDEA: Text between two sets of --- above and below should be stored in database as
	examples and as text not varchar(255)
		COMMENT: Best way would be to store the --- content in a new file, and 
		save in db to be associated with the milestone/version its in.

	Q: Is there a way to link a milestone that is created from an idea?

	NOTE: The logic of this may work by reading each new line and counting tabs.
	If the next lines tab count is higher than the current one, then you have stepped
	down into a tag the current tag "owns". Conversely, if the tab count decreases,
	you are now on a new tag that does NOT belong to the current one.
		COMMENT: Much of this is solved by doing the JSON conversion, 
		as after its converted there are plenty of ways to traverse the content.
		Dont reinvent the wheel.

	IDEA: Color code each topic
	IDEA: Create a syntax specific to masterPlan files
	IDEA: .mpln file extension
	IDEA: Easiest pattern for writing is a simple rule that all words preceding a color are the metatags
	IDEA: Have a separate category for Questions
	ISSUE: How to escape the colon when necessary to avoid choosing wrong metatag
		Q: Is there a way count capitals, would that be reliable?
			LEARN: Count number of capitals in a string regex
	all blocks of text followed by a colon belong to that tag
		ISSUE: How to know when a block is done and a new metatag begins?
			COMMENT: All metatags wil begin on new line, but may or may not have tabs, or spaces in front.
			If you can count preceding tabs or spaces on every new line, you could also determine
			the level of the nest and do something with that info.
		ISSUE: How to detect if word on first line has a tag at all.  Would I need to regex
		a certain number of capitals?
			COMMENT: Anything between a RETURN and colon is the metatag, from there you will
			have to further process the strings for final values.
	
	IDEA: To swat any applicable metatag means the thought was deliberated and rejected
	IDEA: Need a way to add general tasks not attached to versioning or any website
		COMMENT: Have a top level general tasks separate from the sitePlan for additional notes

	ISSUE: How to do inserts on the actual data and reference the ID's and relationships?
		COMMENT:

	ISSUE: Need a plan to avoid conflicts with external entries.
		Q: Are there repercussions to deleting the entry from the file
		itself after inserted?
			LEARN: How to read file line by line and delete line after its read
		COMMENT: Be sure to disable any type of interval script so it doesnt
		read and delete simultaneously
		COMMENT: If file contents are deleted after import, new files wont have a way
		to append to things in the database
			Q: Is there a function to reconvert mysql back into the text file?
			Comment: Seems like a rabbit hole, using processing power to contanstly 
			shift back & forth is not a good idea
			STALL:1

	ISSUE: How to determine next & previous from current line # in text file?
	ISSUE: Need to learn more about detection of invisible characters text file & regexes
	ISSUE: Is it necessary to update the json file in the root dir?  
	ISSUE: How to deal with nested comments like shown below?
	ISSUE: What if you change the text file after its already been commited to mysql?
		COMMENT: A process to compare mysql data to masterPlan contents would be cumbersome
		and prohibitive to doing it at all. No reason to maintain 2 versions anyway
		Q: Should a process be implemented to delete info from text file
		after successfully extracted?
		IDEA: Possibly creating the table in isolation would allow for
		a fast reliable delete & recreate
			ISSUE: Designing that type of database would contain too many tables
	
	Q: Spotting a pattern in this outline of too many comments 
	within comments.  Seemingly could go on endlessly.  May need to rule out
	comments belonging to comments?
		A: If there is one table for each possible metatag the relationships
		can help keep it all in order.  IE questions,answers,comments,task,idea,issue,etc

	Q: Whats the best way to retrieve updated info about the file itelf
		A: Thought process was that maybe than needing to make frequent mysql calls
		to update the file and parse for it, but it sounds unnecessary

VERSION: 1.015
	
	RELEASE_NOTES: New Feature <! ErrorBuddy !> Shaking it up by starting with the number 1.
	With ErrorBuddy in place, you have all you need to get out of this repetitive hellhole.
	You can right click the message, search in stack overflow and commentate resolutions

	IDEAS: Consider building errorBuddy sooner so you can use it during 
	the development of itself

VERSION: 1.016

	RELEASE_NOTES: New Feature <! MySQLuv !> Create new tables from within sublime text
		LEARN: How to get a panel showing with multiple input fields in sublime text

VERSION: 1.017

	RELEASE_NOTES: New Feature <! AlgoHuxley !> is an algorithm builder that outlines
	conditions and what behaviors they would trigger to better help you 
	map out paths of logic before you start.  When you have complex conditions, it can 
	be exhausting repetitively retesting / refreshing.  So plan ahead and make your life easy
		COMMENTS: I think this would be easier where the map is visually represented.
		Q: 
		the text version is too hard to comprehend and is redundant
		---
		START: Is fileAnchor loaded

			YES:
				C: Is site enabled
					YES: *
					NO: Exit

				C: Is folder qualified
					YES: *
					NO: Exit
 
				R: *tagCheck*  

			NO: Exit

		fileFound:
			YES:
				*tagCheck*
			NO:
				Exit
		---
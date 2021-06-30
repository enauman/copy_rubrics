# copy_rubrics
a quick way to make copies of a rubric document for studetns on a class roster
<ol>
  <li>Fill project rubric with standards and points as a google doc or Word doc, add to folder with main.py</li>
  <li>Create txt doc with roster for class rubric will be copied for, simple list of students firstname lastname separated by return.</li>
  <li>Edit main.py to include logic for user input for which roster to use, and roster file names</li>
</ol>
<p>Edit this line with user input that triggers which roster to use</p>
<code>
  whichClass = input("intro, advanced, or ei? ")
</code>
<p>Edit this section with roster conditionals to match whichClass input</p>
<pre>
  if(whichClass == "intro"):
	  students = open("students9-10.txt", "r")
  elif(whichClass == "advanced"):
	  students = open("students11-12.txt", "r")
  elif(whichClass == "ei"):
	  students = open("studentsEI.txt", "r")
</pre>

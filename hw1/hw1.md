```python

```

\begin{center}
\begin{huge}
DATA203 Foundational Python (Prof. Maull) / Fall 2025 / HW1
\end{huge}
\end{center}

| Points <br/>Possible | Due Date | Time Commitment <br/>(estimated) |
|:---------------:|:--------:|:---------------:|
| 10 | Friday, September 19 @ midnight | _up to_ 15 hours |


* **GRADING:** Grading will be aligned with the completeness of the objectives.

* **INDEPENDENT WORK:** Copying, cheating, plagiarism  and academic dishonesty _are not tolerated_ by University or course policy.  Please see the syllabus for the full departmental and University statement on the academic code of honor.

## OBJECTIVES
* Explore JupyterHub Python _shell_ commands inside cells

* Understand and use dictionaries for complex data.

## WHAT TO TURN IN
You are being encouraged to turn the assignment in using the provided
Jupyter Notebook.  To do so, make a directory in your Lab environment called
`homework/hw1`.   Put all of your files in that directory.  Then zip or tar that directory,
rename it with your name as the first part of the filename (e.g. `maull_hw1_files.zip`, `maull_hw1_files.tar.gz`), then
download it to your local machine, then upload the `.zip` to Canvas.

If you do not know how to do this, please ask, or visit one of the many tutorials out there
on the basics of using zip in Linux.  

If you choose not to use the provided notebook, you will still need to turn in a
`.ipynb` Jupyter Notebook and corresponding files according to the instructions in
this homework.


## ASSIGNMENT TASKS
### (0%) Explore JupyterHub Python _shell_ commands inside cells 

In the last time we learned to run the terminal console commands
in JupyterLab, which is a great way to perform command-line tasks and is an essential tool
for basic scripting that is part of a data scientist's toolkit.  Last time we used a 
terminal console in the lab environment
this time we familiarize ourselves with Jupyter
_shell_ escape commands **within** a notebook.

Study:

  * [Python Data Science Handbook: IPython and Shell Commands](https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html)

for full documentation on _shell_ ... they are **very** useful!

**&#167; Task:**  **Use Jupyter _shell_ commands to perform the same commands as last time.**

   Basic file operations go a long way to understand
   the way Linux works.  In this part, you will understand
   folders, files and making revisions to a file.  These files
   will be visible within Jupyter, which makes moving from
   one platform to another seamless.  We will create a folder, file
   and make edits.             
   
   - type `!mkdir your_folder_name` to create a folder in filesystem _in the current folder where you are_
   - create a file by type `touch README.md` the `touch` command creates a file if it does not already exist, otherwise it will change the timestamp of that file when it is "touched"
   - edit the file in Jupyter with the text editor
   - to see the contents of your file typing `!cat README.md` 


**&#167; Task:**  **Use _shell_ command `wget` to quickly obtain remote files in Linux** 

   As before get a remote file this time it will be from the [Internet Archive](https://archive.org):

   - in a cell type `!wget https://ia801306.us.archive.org/15/items/fouraddressesats00howa/fouraddressesats00howa.pdf`
   - execute the cell
   - verify the file was retrieved by opening it



### (100%) Understand and use dictionaries for complex data. 

We learned in lecture that function are necessary
tools in Python.

I have provided a starter notebook for you to use, 
which will greatly enhance you ability to complete
the assignment.  See that in the folder here.  The 
name of the notebook is `hw1/hw1_starter.ipynb`:

* [https://github.com/kmhuads/f25_data203/tree/main/hw1/hw1_starter.ipynb](https://github.com/kmhuads/s25_data203/tree/main/hw1/hw1_starter.ipynb)

Look at this file and see what is in it -- use it since
in the notebook are some scaffolding code.  You will 
need to study it and use it in the solutions
being asked.


We learned in lecture that dictionaries are very flexible
data structures in Python.  The assignment will
focus on the dictionary mapping type.

**&#167; Task:**  **Use the starter notebook and answer write the Python code required to complete it.**





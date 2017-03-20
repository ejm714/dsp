# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> * **pwd** - show current working directory path
> * **cd** - change working directory
> * **mkdir** - create a directory
> * **rmdir** - delete a directory
> * **touch** - creates new file (ex. touch test.txt)
> * **rm** - delete a file
> * **mv** - rename a file (can also be used to move a file)
> * **cp** - copying a file from one directory to another
> * **cat** - print the whole file
> * **grep** - find things inside files
> * **m`*`** - selects all files starting with m (or whichever letter is specified)
> * **`*`** - selects all files in working directory
> * **ls -a** - lists hidden files and directories (i.e. those that start with a dot)
> * **ls -t** - orders files and directories by time modified
> * **cd ..** - moves up one level in the directory


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> - `ls` - lists files and directories
> - `ls -a` - displays all files 
> - `ls -l`  - displays long format listing
> - `ls -lh` - print human readable sizes
> - `ls -lah` - displays all files in long format in human readable size
> - `ls -t` - displays files based on timestamp (newest first)
> - `ls -Glp`- displays files without group names but with /

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> - `ls -d` - displays only directories
> - `ls -m`- displays names as comma-separated list
> - `ls -R` - displays subdirectories as well
> - `ls -r` - displays files in reverse order
> - `ls -1` - displays each entry on a line

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> “Xargs builds and executes command lines from standard input. Xargs reads items from the standard input, delimited by blanks, and executes the command one or more times with any initial-arguments followed by items read from standard input.” 
>  
> For example, xargs can be used to find and delete the text files in or below the /dec directory (the `–print0` ensures spaces and newlines don't cause problems).  
>  
> `find /home/ccuser/workspace/blog/2014/dec –name “*.txt” –type f –print0 | xargs -0 /bin/rm -f`

 


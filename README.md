# elf-crumble solve
This is my solution to the 2018 DefCon CTF Quals elf crumble problem.

The description of this problem stated that "The binary was dropped and broke into a bunch of pieces. But not to worry, the pieces would all fit back together if you put them back in the correct order." (or something like that.)

## My approach was as follows:

* Take a look at the `broken` file and see what it looked like. 
* I noticed a lot of 58s (X in ascii) in one section of the file. I took a guess that this is where the broken fragments should go.
* Next I loaded the broken binary into two parts, brokena and brokenb. brokena was the data before the 58s' and brokenb was the data after the 58s. I did not load the 58's into anything, they were omitted.
* After that I loaded the file fragments. 
* I then created each possible permutation of the fragment files, and inserted them in between brokena and brokenb, and then wrote them.
* I finished the rest of the solution with some bash commands. I executed each of the generated files, and printed if it wasn't a segfault. 

## To run this, do the following:

`python broken.py`

This will write all of the possible permutations of the broken binary into bin/. Next run the following:
```
cd bin; chmod +x *; for i in {0..40319}; do if OUTPUT="$(./$i | grep -v "Segmentation fault")"; then echo $i $OUTPUT; fi  done
```
Binary iteration number: 39690 was the solution. When ran it will print the flag: `welcOOOme`.

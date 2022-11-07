A graphical user interface for the steganographer from Priyansh Anand (https://github.com/priyansh-anand) 

This program allows you to hide files in a picture. A detail description of how the program works can be found here: https://github.com/priyansh-anand/steganographer.

In addition this program ask you if the original file should be removed. 
If your file is stored on a HDD this is done by shred-command.  Shred is a safe way to permanently delete files from a HDD so that they cant be recovered

If your file is stored on a SSD the program will overwrite the file and then delete it. This is not as safe as the process on a HDD.

The program will auto-detect the type of your drive.  
EXCEPTION: if your a running a virtual machine the program will always assume you re using a HDD. So don’t use the deleting function if you run this program on a VM with SSD.



# CleanHPLC
Easy software to clean HPLC outcomes from our loved HPLC in lab N229. I know you love spending a couple of hours mining your data, but in case you have even funnier things to do just use this software to speed it up. 

To use this software just run the it from your teminal using the name of your data retrieval file as a variable argument (e.g: python program_name.py data_retrieval_file). This software works with the output file generated if you perform the data retrieval as described in the hardcopy manual next to the HPLC (selecting the first 3 options choosing "tabs" as separation method). 

Please always use the last version to ensure a good analysis. Just in case you're curious you've got the characteristics of each version following. 

-------------------------------------------------------------------------------

Version 1.0
Only valid to obrain the concentrations of Glucose and Ethanol
If the name of your sample contains an space, everything after the first space will not appear in the output file. 

Version 2.0 
Valid to obtain the concentration of any metabolit you included with in your method
If the name of your sample contains an space, everything after the first space will not appear in the output file. 

Version 2.1
Valid to obtain the concentration of any metabolit you included with in your method
Sample names with spaces also accepted

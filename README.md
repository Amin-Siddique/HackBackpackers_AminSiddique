# HackBackpackers_AminSiddique

Problem Statements

 

Problem Statement 1 - Lineage problem statement

# Description

The python code is used to extract the tablenames and columns from a sql query which is provided to us a string. 
The code is build using the regular expression module and most logic is dependent on string match and index searching to pull out the tablenames and columnnames



# Prerequisite

One Input parameter to be provided which is a sql query.

 

# How to run

The code can be executed with python on machine. For my purpose i've used databricks community version to spin up a python cluster which is free of cost.
 

# Any other points to mention

The code couldn't cover all the edge cases as sql syntax is vast and every developer has a different style of scripting. 

 

Problem Statement 2 - Functions problem statement

# Description

The solution for each function in datastage is translated in the same manner to azure data factory expressions with available adf functions to provide the same output as Datastage.

 

# Prerequisite

The code is written in python which acts as a wrapper function to the azure data flow expression and functions.
  

# How to run

The expressions can be run directly from ADF


# Any other points to mention

The function definations are provided for each functions all with few examples.

 

Problem Statement 3 - XML problem statement

# Description

The python code parses XML file to get the tranformed column and its related expressions in a lineage.

In order to work, the xml file was uploaded to git, then using python's request module I was able to fetch the raw xml data from git and save it in databricks dbfs, Once file was preset. XML was parsed with python.
 

# Prerequisite

Python Module

  
# How to run

The code can be executed with python on machine. For my purpose i've used databricks community version to spin up a python cluster which is free of cost.
 


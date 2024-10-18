# Survey for Cultural Estrangement

This is the code for the survey for the project: "Alienated at Home: How Cultural Estrangement Drives Populist Votes."

Contact: 
Nicolas Roever
University of Cologne
Email: nicolas.roever@wiso.uni-koeln.de
Website: www.nicolasroever.com


# Structure of the Code

The main code is implemented in the survey folder. Here, there are the html files and one python file for functions, models, and pages. These are the standard files needed for otree pages. I also added a file python_functions, where I write functions needed for this survey. 


## Page: Political Opinions

This page asks for opinions on 9 different issues clearly ordered among conservative vs. liberal lines (see Enke et al., 2024). 
The participant can only click next, if all questions are answered. 



## To-Dos

- Make sure consent form is correct
- Make sure that you can deselct the radio buttons in the statement pages. 
- Check the thing on mobile devices.
- Check on different browsers. 
- Randomize the order of the politicians (this is another "treatment"), you need to make new videos here as well
- I have the problem in Primer, that the text is not redisplayed if there was an error. 
- Wahrnehmung der Parteien sollte sich durch den Primer nicht ändern. 
- Estimation Question bank=True fuer echte Survey rausnehmen. 
- Beium zweiten Video erscheinen die Fragen schon vor Ende. 

## Server Commands

These are the commands for the university server we are using to run the experiment.

- Remember that you need to be one folder above bargaining_experiment when you do the rsync command

- This command deletes the current project: 

> rsync --delete -Pa bargaining_experiment  otree15@otree2.uni-koeln.de:Projects/

-  This command starts the server
> ssh otree15@otree2.uni-koeln.de

# ID Number Generator

## About project
It's a my second  project, I make it more **advanced** and **complex** than my first project.
`app.py` will launch the ID Number Generator and you will be asked to fill some fields and as a result you will get ID number which will be initialized according Lithuanin ID number regulation RST 1185-91.

## Rules
You can read all rules here: https://lt.wikipedia.org/wiki/Asmens_kodas.

## What the code does
<ol>
<li>Start of the program</li>
<li>Person will be asked to fill all necessary information</li>
<li>APP will initialize ID Number generator</li>
<li>1st digit: depends on gender and century person born. 3/4 for male/female borned in XX century and 5/6 for male/female borned in XXI century</li>
<li>From 2nd to 6th: date of birth with format YYYYMMDD</li>
<li>From 7th to 10th: ascending order of the all borned that day in country</li>
<li>11th: checksum digit calculated by special algorithm</li>
</ol>

## Installing
Run `app.py`

## Acknowledgments
Vilnius School of AI
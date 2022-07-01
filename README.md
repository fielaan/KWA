RU: _Чтобы посмотреть этот файл на русском, откройте_ __README_RU.md__

EN: _To view this file in Russian, open_ __README_RU.md__

#KWA - a new revolutionary programming language

###Why?

* Short syntax
* Ability to write comments directly in the code without designations
* Availability of [online interpreter](https://kwa-online.herokuapp.com ) <tr>
This list will be updated in the future

___


###Syntax

syntax | notation
:---------|-----------:
KwA |Add one to the variable x
Kwa |Subtract one from variable x
kwA |Add one to the variable y
kwa |Subtract one KWA from variable y
KWA|Set variable x to the value of the square of variable x
KWAA |Set variable y to the value of the square of variable y
kWa |If x < y go back 3 commands
Kwaa |Output the UNICODE table character corresponding to x
Kwaaa |Output the UNICODE table character corresponding to y

All commands are separated by a space or a line break(enter button)

To write comments or empty commands, any word not specified in the table is used

#####Code example:
``angular2
KwA Kwa <comment>
``
In the above code snippet, only the first two commands will be executed, the third one will be perceived as empty

Empty commands __are taken into account by__ command __kWa__

###Code Examples:
####Copying the _y_ variable to _x_
```angular2
kwA kwA KWAA
Kwaaa
pass
pass
KwA
kWa

Kwaa
```
In the above code snippet, two identical characters will be output. You will be able to perform any operations with the variable y in the first line and the same characters will always be output, since the variable x equals y

In this fragment, pass is used as an empty command

##You can try this programming language at [this link](https://kwa-online.herokuapp.com )
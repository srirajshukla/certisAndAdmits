# certisAndAdmits

Generate certificate and admit cards from a spreadsheet of data.



# dependencies

1. pandas
2. cv2 (opencv)
3. qrcode

# Input data format

By default, a spreadsheet with the name data.xlsx has to be placed in the safe folder as `main.py`. However, this can be changed in the source code to any other name or format readable by pandas. 

Inside the spreadsheet, there should be four columns - `UID`, `Name`, `Branch` and `Transaction Id`. 

Place the format for admit card and certificates inside the format folder, and you're good to go. 



If there is a need to use a format where data field are at different positions, the source code can be changed accordingly. More fields can be added in same way. Most of the times it is a single line edit. 



# Output

The generated certificates are stored in `genadmit` folder and the generated admit cards are stored in `gencert` folder. 

# Uses

Often while conducting workshops, seminars and other sessions, we need to mass generate  admit card for all the participants. After the event is finished, we have to supply a certificate of completion as well. This python script is helpful in automating these tasks. 



# Sample Use

A sample admit card generated using this application - 

![A Sample admit card generated using this application. ](https://github.com/srirajshukla/certisAndAdmits/blob/master/genadmit/ABCDEFG20.png) 

# Further Scope of Improvement

1.  I was planning on adding a Tkinter based GUI interface to select the various data fields and their position.
2. A mail can be sent to the participants in their provided email ids containing the admit cards and certificates.  




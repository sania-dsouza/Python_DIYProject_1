#Write the result of the webpge decoded text to a file

import decodeAWebpage

with open('testFileToWrite.txt', 'w') as open_file:
    resStr = str(decodeAWebpage.resList)
    open_file.write(resStr)
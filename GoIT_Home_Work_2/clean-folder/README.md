
## DESCRIPTION

Many people have a folder on their desktop called something like "Disassemble". As a rule, hands never reach this folder.

This application will parse this folder. To do this, our application will check the file extension (the last characters
in the file name, usually after the dot) and, depending on the extension, decide which category to categorize this file.

The application goes through the folder specified during the call and sorts all the files into groups:

images('JPEG', 'PNG', 'JPG', 'SVG'); video files ('AVI', 'MP4', 'MOV', 'MKV');
documents('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'); music('MP3', 'OGG', 'WAV', 'AMR');
archives ('ZIP', 'GZ', 'TAR');
unknown extensions.

## LICENSE

Copyright 2022 Sergii_O

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of 
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
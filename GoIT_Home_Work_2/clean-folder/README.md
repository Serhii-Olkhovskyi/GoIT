# clean-folder

Many people have a folder on their desktop called something like "Disassemble". As a rule, hands never reach this folder.

This application will parse this folder. To do this, our application will check the file extension (the last characters
in the file name, usually after the dot) and, depending on the extension, decide which category to categorize this file.

The application goes through the folder specified during the call and sorts all the files into groups:

images('JPEG', 'PNG', 'JPG', 'SVG');
video files ('AVI', 'MP4', 'MOV', 'MKV');
documents('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
music('MP3', 'OGG', 'WAV', 'AMR');
archives ('ZIP', 'GZ', 'TAR');
unknown extensions.

# unix_hacks

Some scripts for Unix use

* isgd.py
  - Summary: URL shortening for the desktop GUI copy buffer
  - Use: This is a short python script that works to replace the current GUI copy buffer by a shortened version. It takes the contents of your desktop GUI copy buffer and obtains a shortened version from the https://is.gd/ URL shortener service, then uses the new shorter URL result to overwrite the contents of the GUI copy buffer
  - Depends on: gdshortener [pip3 install gdshortener] and Unix desktop pbpaste and pbcopy commands (available on macOS desktop or use xclip aliases [sudo apt-get install xclip -y])
  - Rationale: allows a user to switch between different tools (such as browsers) and not need to reorganise URL shorteners in each tools every time

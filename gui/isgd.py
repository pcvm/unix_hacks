# File isgd.py provides a portable URL shortener for the desktop copy buffer
#
# . reads and then replaces the copy buffer contents with a shortened URL
# . this portable approach means independence from user apps that interact with the copy
#   buffer i.e. you can change browsers and still use the same URL shortener
# . access to the is.gd URL shortener is via python3 and gdshortener
#   (standard pip3 package with web site https://pypi.org/project/gdshortener/)
# . access to the copy buffer is via calls to pbcopy and pbpaste in a python3 subprocess
#   (pbcopy and pbpaste are part of macOS and xclip provides equivalents in *BSD/Linux)
#
# p.musumeci@ieee.org

# Pre-requisites:
# . using gdshortener (install: pip3 install gdshortener)
# . using pbpaste and pbcopy which exchange data between the clipboard and stdin/stdout respectively on macOS
# . install xclip on *BSD (see pkg or ports) and Linux (sudo apt-get install xclip -y)
#     pbcopy='xclip -selection clipboard'
#     pbpaste='xclip -selection clipboard -o'
#   (notes https://garywoodfine.com/use-pbcopy-on-ubuntu/)

# Convenient access:
# . macOS keystroke: use automator to create a service to "Run Shell" (no input) that runs
#   this script and assign it to a keystroke via
#   System Preferences -> Keyboard -> Services -> General: isgd => Cmd-`
# . X-windows menu item: add a menu item e.g. "/usr/local/bin/python3 ~/bin/isgd.py &"

# Debugging:
# . can maintain last conversion details in file /tmp/pb_copy_paste_url.txt

import gdshortener
import subprocess

proc = subprocess.Popen('pbpaste', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#             (read bytes)       (convert to ascii)       (cleanup)
the_url = str(proc.stdout.read().decode(encoding='UTF-8').strip())
print(the_url, file=open("/tmp/pb_copy_paste_url.txt", "w"))

# quit with error message if URL is already from is.gd
if the_url[0:14] in 'https://is.gd/':
    print('? found is.gid is already in URL '+the_url, file=open("/tmp/pb_copy_paste_url.txt", "a"))
else:
    s = gdshortener.ISGDShortener()
    (new_url, tag) = s.shorten(the_url)
    print(str(new_url), file=open("/tmp/pb_copy_paste_url.txt", "a"))

    proc = subprocess.Popen('pbcopy', stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.stdin.write(new_url.encode(encoding='UTF-8'))

# end

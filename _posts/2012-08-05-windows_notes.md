---
title: "Windows Notes"
date: 2012-08-05 10:22:16 +0000
categories: ["windows"]
permalink: /windows_notes
---
Just some random notes about using Windows

### Backup batch script

Below is the batch script I use to achieve the following behaviour:

-   Copy files from hard disk to a USB disk.
-   The backup procress must never delete a file from either source or
    destination, except for the Photos director.
-   The end result is that the destination ends up having more files
    than the source because files are never deleted by the
    backup process. But the Photos directory on both disks should be
    exact copies.

{% highlight bat %}
REM tutorial: http://www.sevenforums.com/tutorials/187346-robocopy-create-backup-script.html
REM options: http://technet.microsoft.com/en-us/library/cc733145%28WS.10%29.aspx
REM
REM /e    = copy all sub-folders, even empty ones
REM /mir  = mirror (check the files in the destination, and only copy newer files)
REM /np   = no progress counter
REM /log: = create a logfile
REM /xo   = exclude older files
REM /xd   = exclude directory

robocopy D:\ I:\Backup\Storage /e /np /log:backup_log.txt /xo /xd $RECYCLE.BIN RECYCLER "System 
Volume Information" Photos

robocopy D:\Photos I:\Backup\Storage\Photos /e /mir /np /log:backup_photos_log.txt

pause
{% endhighlight %}


<!--break-->


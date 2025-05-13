# osint-resources
organizing osint resources

The gist for web tools:

1. Add information to a profile in basset-hound
2. Open the osint tab from the profile
3. Modify the autopopulate form from the osint tab
   1. This will change the information that you can select to populate the osint tools webpage with
   2. when you click ***Open*** on a web tool, it will open the webpage
4. Click on the Basset-Hound Autopopulate extension icon
5. Select the information you want to populate
6. Click on the ***Autopopulate*** button
7. The information will be populated in the fields of the webpage 

The gist for command line tools:
1. Add information to a profile in basset-hound
2. Open the osint tab from the profile
3. Modify the autopopulate form from the osint tab
   1. This will change the information that you can select to populate the osint tools command line with
   2. when you click ***Copy*** on a command line tool, it will copy a bash script to the clipboard
4. Open the terminal application, or whatever terminal you use
5. Make a new bash file
6. Paste the copied bash script into the bash file

## ref_formatter.py
> Python script to help format Markdown files with OSINT Resources 

Perform formatting on all markdown file in a given directory.

```
for file in ./references/*.md; do python3 ./references/ref_formatter.py -o ./new_refs/tmp_refs/ -f ${file}; done
```

## ref_checker.py
> Python script to help check that a url has not been mentioned amongst other OSINT Resources

Following the local folder example of **ref_formatter.py** for this repo

```
for file in ./new_refs/tmp_refs/*.md; do python3 ./references/ref_checker.py -c ./src/ -o ./new_refs/tmp_ref_checks/ -f ${file}; done
```
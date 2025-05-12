# osint-resources
organizing osint resources


## ref_formatter.py
> Python script to help format Markdown files with OSINT Resources 

Perform formatting on all markdown file in a given directory.

```
for file in ./folder/*.md; do python3 ref_formatter.py -o ./tmp_references/ -f "$file"; done
```

or local folder

```
for file in ./*.md; do python3 ref_formatter.py -o ./tmp_references/ -f "$file"; done
```
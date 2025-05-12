# osint-resources
organizing osint resources


## ref_formatter.py
> Python script to help format Markdown files with OSINT Resources 

Perform formatting on all markdown file in a given directory.

```
for file in ./references/*.md; do python3 ./references/ref_formatter.py -o ./new_refs/tmp_refs/ -f ${file}; done
```

## ref_checker.py

Following the local folder example of **ref_formatter.py** for this repo

```
for file in ./new_refs/tmp_refs/*.md; do python3 ./references/ref_checker.py -c ./src/ -o ./new_refs/tmp_ref_checks/ -f ${file}; done
```


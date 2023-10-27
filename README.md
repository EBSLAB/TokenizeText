# TokenizeText

- Installed the following python module:
    ```
    langid==1.1.6
    Morfessor==2.0.6
    numpy==1.26.1
    pbr==2.1.0
    polyglot==16.7.4
    polyglot-tokenizer==2.0.2
    pycld2==0.41
    PyICU==2.11
    six==1.16.0
    ```

- If found the below error:
```
ImportError: cannot import name 'Locale' from 'icu' (/home/vilal/allenv/lib/python3.10/site-packages/icu/__init__.py)
```
- Then install this:
```
sudo apt-get install python3-tk
```


- Run the below command: to run script:
```
python dropFunctionWords.py --input_file in.txt --lang hi --word_list_file funtionWordlist.txt --output_file output.txt
```


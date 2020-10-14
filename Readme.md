# Market Indicators

A simple calculator which builds the Aroon indicator for a given data set in a csv file

## Aroon Calculator

```
Aroon up = 25 - Periods since 25 period high
          ---------------------------------- x 100
                        25  

Aroon down = 25 - Periods since 25 period low
          ---------------------------------- x 100
                        25  
```

## How to use the project
1. Pull the repo and create a local virtual environment with

2. Switch to your venv using:
    ```
    source <name of env>/bin/activate 
    ```
3. Run `pip install` with the requirements.txt file
    ```
    pip install -r requirements.txt
    ```

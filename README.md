# Mockup
Python script to create mockup data for chimney sensor readings.

<!-- ![](pipe.png) -->

## Getting started
[Install python](https://www.python.org/downloads/).  
Clone the repo and cd into the directory.  
Run these commands.
```
pip install -r requirements.txt
python src/index.py 100
```

This will generate 100 points per house.  

## Commands:
```
python src/index.py <POINT-COUNT>
```

`<POINT-COUNT>`: Number of points to generate per house


## Files  
- **locations.csv**: Script finds the komtek locations from a file named `locations.csv` in the main directory.

- **output.csv**: The output is a new file named `output.csv` in the main directory.
# CSC 480: Artiﬁcial Intelligence I: 2024 Spring, Assignment #1

## 1. Student Info.
- Name: Ayden Deng
- E-mail: ydeng24@depaul.edu

## 2. Assignment1 Project
```
|___assignment1
    |___data
    |___src
        |___BidirectionalSearch.py
        |___graph.py
        |___IDDFS.py
    |___graph.sh
    |___README
```

## 3. Usage
❗️Note: this assignment project is implemented with Python3

### 3.1 `Python3` is Required
Make sure that Python3 is installed in your device: https://www.python.org/downloads/

### 3.2 Run `IDDFS.py` (Iterative Deepening Depth First Search)
Use command like: python3 src/IDDFS.py data/ctaTrain.json (python3 <filepath> <datapath>) in terminal
```
python3 src/IDDFS.py data/ctaTrain.json
```

### 3.3 Run `BidirectionalSearch.py` (Bidirectional Search)
Use command like: python3 src/BidirectionalSearch.py data/ctaTrain.json (python3 <filepath> <datapath>) in terminal
```
python3 src/BidirectionalSearch.py data/ctaTrain.json
```

### 3.4 Run Iterative Deepening Depth First Search and Bidirectional Search at once
#### 3.4.1 Run `graph.py`
Use command like: python3 src/graph.py data/ctaTrain.json (python3 <filepath> <datapath>)
```
python3 src/graph.py data/ctaTrain.json
```

#### 3.4.2 Run shell script `graph.sh`
Use command like: ./graph.sh data/ctaTrain.json (<filepath> <datapath>)"
```
./graph.sh data/ctaTrain.json
```

## 4. Example Output
```
aydendeng@Aydens-MacBook-Pro assignment1 % python3 src/IDDFS.py data/ctaTrain.json
1st name (or 'quit' to quit): 43rd
2nd name (or 'quit' to quit): Main
43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
1865543 calls
1st name (or 'quit' to quit): quit

aydendeng@Aydens-MacBook-Pro assignment1 % python3 src/BidirectionalSearch.py data/ctaTrain.json
1st name (or 'quit' to quit): 43rd
2nd name (or 'quit' to quit): Main
43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
2761 calls
1st name (or 'quit' to quit): quit

aydendeng@Aydens-MacBook-Pro assignment1 % python3 src/graph.py data/ctaTrain.json
1st name (or 'quit' to quit): 43rd
2nd name (or 'quit' to quit): Main
IDDFS Path: 43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
IDDFS Calls: 1865543
Bi-Directional Search Path: 43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
Bi-Directional Search Calls: 2761
1st name (or 'quit' to quit): quit

aydendeng@Aydens-MacBook-Pro assignment1 % ./graph.sh data/ctaTrain.json
1st name (or 'quit' to quit): 43rd
2nd name (or 'quit' to quit): Main
IDDFS Path: 43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
IDDFS Calls: 1865543
Bi-Directional Search Path: 43rd -> Indiana -> 35th-Bronzeville -> Cermak-McCormick Place -> Roosevelt -> Harrison -> Jackson -> Red Monroe -> Lake -> Red Grand -> Red Chicago -> Clark/Division -> North/Clybourn -> Fullerton -> Brown Red Belmont -> Howard -> South Blvd -> Main
Bi-Directional Search Calls: 2761
1st name (or 'quit' to quit): quit
```

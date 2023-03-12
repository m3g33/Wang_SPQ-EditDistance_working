# Forked Version
Modified version that works with both Python2 and Python3, JDK 17, and Windows.\
I still recommend to use an IDE (IntelliJ) since Java command-line commands are likely broken for you. 

## Performed changes
* Added some comments to the code
* Added some instructions to this README
* Made `run.py` code compatible with Python3
* Fixed errors when using JDK 17

---

# Private-Edit-Distance-Approximation
Link to the paper: http://www.cs.umd.edu/~wangxiao/papers/ped.pdf

## Compilation and Setup:

1.Get the code

`git clone git@github.com:SPQ-EditDistance/code.git`

`cd code`

`git submodule init && git submodule update`

2.Compile and preprocess data

`./compile.sh`

`mkdir processed`

`java -cp bin/ offline.DataPreprocessor listOfGenome processed/`

**If you run into _class not found_ errors, e.g. use an IDE. In IntelliJ:**
1. Right click on *DataPreprocessor* → More Run/Debug → Modify Run Configuration...
2. In the field *Program arguments* paste `listOfGenome processed/`
3. Run configuration

## Run the protocols
3.Run Protocols

`./run.py gen ptcl1  & ./run.py eva ptcl1`

or

`./run.py gen ptcl2  & ./run.py eva ptcl2`

**On Windows you might have to use `python3 run.py` instead of `./run.py`.**\
**Also, if you again run into _class not found_ errors, e.g. directly use an IDE instead of the `run.py`file. In IntelliJ:**
1. Open the file *Protocol1* (or *Protocol2*)
2. Click on the green play button of the *Generator* class → Modify Run Configuration...
3. In the field *Program arguments* paste `online.Protocol1` (or `online.Protocol2`)
4. Repeat step 2 + 3 for the *Evaluator* class
5. Run both configurations simultaneously

4.Try to change parameters in Conf.conf and rerun

More data can be obtained from PGP project: http://www.personalgenomes.org/
Certains genome files has slightly different format and may need slightly changes on preprocessing
code.

To run over internet, update the address in Conf.conf to generator's ip address. Make sure each party has their own files.


### Question about the code?

please email me at wangxiao (aT) cs (Dot) umd (dOt) edu

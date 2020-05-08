# bitlib

**bitlib** -- bitlib Python3 Library API Bindings V3.0

## Install

- clone this repository using
    ```bash
    $ git clone git@github.com:codenio/python3-bindings-2.0-DC01L.git
    ```
- install `bitlib` library from ./src directory
    
    ```bash
    # cd into src/ directory
    $ cd src/
    
    # install the bitscope-library_2.0 debian package
    $ sudo apt-get install bitlib-library_2.0.FE26B_amd64.deb
    
    # install bitlib using the python-binding script 
    $ sudo python3 setup-bitlib.py install
    
    # in case of errors.. try
    $ sudo BASECFLAGS="" OPT="" CFLAGS="-O3" python3 setup-bitlib.py install
    ```

- connect your bitscope micro to your pc and test the functionality using
the example file at `test-bitlib.py`
    ```bash
    $ python3 test-bitlib.py 
        Starting: Attempting to open one device...
        Library: 2.0 FE26B (Python DC01L)
            Link: USB:/dev/ttyUSB0
        BitScope: BS000501 (*****)
        Channels: 10 (2 analog + 8 logic)
        Modes: FAST DUAL MIXED LOGIC STREAM
        Capture: 12288 @ 40000000Hz = 0.000307s (LOGIC)
        Offset: +2.917V to -6.217V
            POD:  9.20V  5.20V  3.50V  1.10V
        Data(5): 1.689062, 1.689062, 1.689062, 1.689062, 1.689062
        Finished: Library closed, resources released.
    ```
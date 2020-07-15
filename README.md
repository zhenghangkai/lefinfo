# lefinfo
lefinfo - LEF file Information

## Import lefinfo
```Python
from lefinfo import lef_info, macro_info, pin_info
```

## Read Single LEF

### macro1.lef for test
```txt
VERSION 5.7 ;

MACRO macro1
  CLASS CORE ;
  ORIGIN 0 0 ;
  SIZE 10 BY 20.0 ;
  PIN pin1 ;
    DIRECTION INPUT ;
    USE SIGNAL ;
    PORT
      LAYER M1 ;
        RECT 1 2 3 4 ;
      LAYER M2 ;
        RECT 2 1 4 3 ;
    END
  END pin1 ;
  PIN pin2 ;
    DIRECTION OUTPUT ;
    USE POWER ;
  END pin2 ;
  PIN pin3 ;
    DIRECTION INOUT ;
    USE GROUND ;
  END pin3 ;
END macro1
```

### lef_info usage
```Python
p='macro1.lef'
lef=lef_info(p)
print(lef.version)
print(lef.nmacro)
print(lef.macros)
print(lef.macros[0])
print(lef.macronames)
```
5.7<br>
1<br>
[['macro1', 'CORE', '0 0', '10 20.0', ['pin1', 'INPUT', 'SIGNAL', ['M1', 'M2']], ['pin2', 'OUTPUT', 'POWER', []], ['pin3', 'INOUT', 'GROUND', []]]]<br>
['macro1', 'CORE', '0 0', '10 20.0', ['pin1', 'INPUT', 'SIGNAL', ['M1', 'M2']], ['pin2', 'OUTPUT', 'POWER', []], ['pin3', 'INOUT', 'GROUND', []]]<br>
['macro1']\<br>

### macro_info usage
```Python
mcr=macro_info(lef.macros[0])
print(mcr.name)
print(mcr.classname)
print(mcr.origin)
print(mcr.sizex)
print(mcr.sizey)
print(mcr.size)
print(mcr.area)
print(mcr.npin)
print(mcr.pins)
print(mcr.pins[0])
print(mcr.pinnames)
print(mcr.pindirections)
print(mcr.pinuses)
```
macro1<br>
CORE<br>
[0.0, 0.0]<br>
10.0<br>
20.0<br>
[10.0, 20.0]<br>
200.0<br>
3<br>
[['pin1', 'INPUT', 'SIGNAL', ['M1', 'M2']], ['pin2', 'OUTPUT', 'POWER', []], ['pin3', 'INOUT', 'GROUND', []]]<br>
['pin1', 'INPUT', 'SIGNAL', ['M1', 'M2']]<br>
['pin1', 'pin2', 'pin3']<br>
['INPUT', 'OUTPUT', 'INOUT']<br>
['SIGNAL', 'POWER', 'GROUND']\<br>

### pin_info usage
```Python
pin=pin_info(mcr.pins[0])
print(pin.name)
print(pin.direction)
print(pin.use)
print(pin.layers)
```
pin1<br>
INPUT<br>
SIGNAL<br>
['M1', 'M2']

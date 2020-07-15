#-*- coding:utf-8 -*-

def lefinfo_linesplit(line,keyword):
    lineleft=line[line.find(keyword)+len(keyword):line.rfind(';')]
    return lineleft.strip()


def lefinfo_readlines(linelist):
    """ read in LEF file line list, and transfer to lef info list
    Input: LEF line list
    Output: lef information list
    Output lef info list format:
    [VERSION,
        [MACRO A,
        CLASS,
        ORIGIN,
        SIZE,
            [PIN A,
            DIRECTION,
            USE
            [LAYER 1, LAYER2, ...]
            ]
            [PIN B,...
            ]
        ]
        [MACRO B,...
        ]
    ]
    """
    version = ''
    macro = ''
    classname = ''
    origin = ''
    size = ''
    pin = ''
    direction = ''
    use = ''
    leflist = []
    for line in linelist:
        if 'VERSION' in line:
            version = lefinfo_linesplit(line,'VERSION')
        if 'MACRO' in line:
            macrolist = []
            macro = line[line.find('MACRO')+5:]
        if 'CLASS' in line:
            classname = lefinfo_linesplit(line,'CLASS')
        if 'ORIGIN' in line:
            origin = lefinfo_linesplit(line,'ORIGIN')
        if 'SIZE' in line:
            size = lefinfo_linesplit(line,'SIZE').replace('BY ','')
        if 'PIN' in line:
            layerlist = []
            pin = lefinfo_linesplit(line,'PIN')
        if 'DIRECTION' in line:
            direction = lefinfo_linesplit(line,'DIRECTION')
        if 'USE' in line:
            use = lefinfo_linesplit(line,'USE')
        if 'LAYER' in line:
            layerlist.append(lefinfo_linesplit(line,'LAYER'))
        if 'END' in line:
            if pin in line:
                macrolist.append([pin,direction,use,layerlist])
            if macro in line:
                macrolist.insert(0,size)
                macrolist.insert(0,origin)
                macrolist.insert(0,classname)
                macrolist.insert(0,macro.strip())
                leflist.append(macrolist)
    leflist.insert(0,version)
    return leflist


def lefinfo_openlef(filename):
    """
    :param filename: The path of LEF file to be opened
    """
    with open(filename, "r") as f:
        linelist = f.readlines()
    lef = lefinfo_readlines(linelist)
    return lef


class lef_info:
    """ lef format:
    [VERSION,            # LEF version
        [MACRO A, ... ]  # macro info list
        [MACRO B, ... ]
    ]
    """
    def __init__(
                self,
                lef):
        li = lefinfo_openlef(lef)
        self.version = li[0]
        self.nmacro = len(li)-1
        self.macros = li[1:]
        self.macronames = [item[0] for item in li[1:]]


class macro_info:
    """ macro format:
    [MACRO A,  # macro name
    CLASS,     # macro class: CORE / MACRO / PAD
    ORIGIN,    # macro origin: '0 0' -> [0, 0]
    SIZE,      # macro size: '10 20' -> [10, 20]
        [PIN A, ... ]  # pin info list
        [PIN B, ... ]
    ]
    """
    def __init__(
                self,
                mcr):
        self.name = mcr[0]
        self.classname = mcr[1]
        self.origin = [float(mcr[2].split()[0]),float(mcr[2].split()[1])]
        self.sizex = float(mcr[3].split()[0])
        self.sizey = float(mcr[3].split()[1])
        self.size = [float(mcr[3].split()[0]),float(mcr[3].split()[1])]
        self.area = float(mcr[3].split()[0])*float(mcr[3].split()[1])
        self.npin = len(mcr)-4
        self.pins = mcr[4:]
        self.pinnames = [item[0] for item in mcr[4:]]
        self.pindirections = [item[1] for item in mcr[4:]]
        self.pinuses = [item[2] for item in mcr[4:]]


class pin_info:
    """ pin format:
    [PIN A,     # pin name
    DIRECTION,  # pin direction: INPUT / OUTPUT / INOUT
    USE         # pin use: SIGNAL / POWER / GROUND
        [LAYER 1, LAYER2, ...]
    ]
    """
    def __init__(
                self,
                pin):
        self.name = pin[0]
        self.direction = pin[1]
        self.use = pin[2]
        self.layers = pin[3]


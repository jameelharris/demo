
variableUINames = { 
    'heroStackDepths': 'Hero Stack Depths',
    'heroPositions': 'Hero Positions',
    'heroUseCaseVariants': 'Villain Positions'
    }

horizontalfilter = { 



    }

verticalfilter = {

    'RFI-polar': { 
        'heroActions': (),
        'heroStackDepths': (),
        'heroPositions': (),
        },

    'RFI-altStrat': { 
        'heroActions': (),
        'heroStackDepths': (),
        'heroPositions': (),
        },


    'RFI-linear': { 
        'heroActions': (),
        'heroPositions': (),
        'heroStackDepths': (),
        },


    'RFI-linear-alternative': { 
        'heroActions': (),
        'heroStackDepths': (),
        'heroPositions': (),
        },


    'BBdefends': { 
        'heroActions': (),
        'heroStackDepths': (),
        'heroUseCaseVariants': (),
        
        },

    'BBdefends-alternative': { 
        'heroActions': (),
        'heroUseCaseVariants': (),
        'heroStackDepths': (),
        
        },
        

    'blindvsblind-SB': { 
        #'heroUseCaseVariants': ('Unopened', 'LimpvsISO', 'vs3bet'),
        'heroUseCaseVariants': (),
        'heroActions': (),
        'heroPositions': ('SB',),
        'heroStackDepths': (),
        },

    'blindvsblind-BB': { 
        #'heroUseCaseVariants': ('vsLimp', 'vsRaise',),
        'heroUseCaseVariants': (),
        'heroActions': (),
        'heroPositions': ('BB',),
        'heroStackDepths': (),
        },

    'vsOpen': { 
        'heroActions': (),
        'heroStackDepths': (),
        #'heroPositions': ('EP', 'MP', 'HJ', 'CO', 'BTN', 'SB'),
        'heroPositions': ('SB',),
        'heroUseCaseVariants': (),
        
        },

    'vsOpen-alternative': { 
        'heroActions': (),
        'heroStackDepths': (),
        #'heroUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroUseCaseVariants': ('vsEP',),
        'heroPositions': (),

        },
    
    'vs3bet': { 
        'heroActions': (),
        'heroStackDepths': (),
        #'heroPositions': ('MP', 'HJ', 'CO', 'BTN'),
        'heroPositions': ('MP',),
        'heroUseCaseVariants': (),
        
        },

    'vs3bet-alternative': { 
        'heroActions': (),
        'heroStackDepths': (),
        #'heroUseCaseVariants': ('vsHJ', 'vsCO', 'vsBTN', 'vsSB', 'vsBB'),
        'heroUseCaseVariants': ('vsBB',),
        'heroPositions': (),
        
        },

    'sqz': { 
        'heroActions': (),
        #'heroPositions': ('CO', 'BTN', 'SB', 'BB'),
        'heroStackDepths': (),
        'heroPositions': ('BB',),
        'heroUseCaseVariants': (),
        
        },

    }

formats = {'comboFormat': '.1f', 'frequencyFormat': '.2f'}

components = {'heroPosition': 1, 'heroUseCaseVariant': 2, 'heroAction': 3, 'heroAction-alt': 2, 'discount': 1}

useCaseVizTypes = { 
    'positionDriven': ('RFI-polar'),
    'stackDepthDriven': ('RFI-altStrat', 'RFI-linear'),
    'useCaseVariantDriven': ('BBdefends', 'blindvsblind', 'vsOpen', 'vs3bet', 'sqz')
}

delimiters = { 
    'handListDelimiter': ',',
    'discountedHandDelimiter': ':',
    'fileNameDelimiter': '-',
    'columnHeaderDelimiter': '-',
    }

handProperties = {
    'offsuit': 'o',
    'suited': 's',
    }

preFlopUseCases = {
    'RFI-polar': {
        'fileDirPattern': '**/*RFIpolar/*.txt', 
        'heroPositions': ('EP', 'MP', 'LJ', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('15BB',),
        'heroActions': ( 'jam', 'open'), 
        'subplotcolors': {'jam': 'Reds', 'open': 'Blues'}, 
        'xaxistitle': 'position (open size),  frequency',
        'viztitle': 'RAISE FIRST IN - POLARIZED',
        'mixedstrategyflag': 'false',  
        'purpose': 'straightforward push fold strategy vs tougher opponents in the blinds',
        },

    'RFI-altStrat': {
        'fileDirPattern': '**/*altStrat/*.txt', 
        'heroPositions': ('LJ', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('15BB', '20BB'),
        'heroActions': ('jam', 'open', 'limp'),
        'subplotcolors': {'jam': 'Reds', 'open': 'Blues', 'limp': 'Greys'},   
        'xaxistitle': 'stack depth (open size),  frequency',
        'viztitle': 'RAISE FIRST IN - ALTERNATIVE STRATEGY', 
        'mixedstrategyflag': 'true',
        'purpose': 'to vpp more',
        },

    'RFI-linear': {
        'fileDirPattern': '**/*RFI/*.txt', 
        'heroPositions': ('EP', 'MP', 'LJ', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('20BB', '25BB', '30BB', '40-50BB', '60-100BB'),
        'heroActions': ('jam', 'open'),
        'subplotcolors': {'jam': 'Reds', 'open': 'Blues'},
        'defaultOpenSize': '2-2.3x',
        'viztitle': 'RAISE FIRST IN - LINEAR',
        'mixedstrategyflag': 'false',
        'factor-1': 'what are the weakest offsuit hands I open in any given scenario',
        'factor-2': 'what are the weakest offsuit hands I call with versus a 3-bet',
        }, 
 
    'BBdefends': {
        'fileDirPattern': '**/*BBdefends/*.txt', 
        'heroPositions': ('BB',),
        'heroStackDepths': ('15BB', '20BB', '25BB', '30BB', '50BB', '100BB'),
        #'heroStackDepths': ('100BB', '50BB', '30BB', '25BB', '20BB', '15BB'),
        'heroActions': ('jam', '3bet', 'call'),
        'heroUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'subplotcolors': {'jam': 'Reds', '3bet': 'Greens', 'call': 'Greys'},
        'viztitle': 'BIG BLIND DEFENSE',
        'mixedstrategyflag': 'true',
        'purpose': 'to vpp more',
        }, 
    
    'blindvsblind': {
        'fileDirPattern': '**/*blindvsblind/**/*.txt', 
        'heroPositions': ('SB', 'BB'),
        'heroStackDepths': ('20BB', '25BB', '30BB', '50BB', '100BB'),
        'heroActions': ('jam', '3bet', '4bet', 'reraise', 'open', 'limpcheckcall', 'call'),
        'heroUseCaseVariants': ('Unopened', 'LimpvsISO', 'vs3bet', 'vsLimp', 'vsRaise'),
        'subplotcolors': {'jam': 'Reds', '3bet': 'Greens', 'call': 'Greys', 'limpcheckcall': 'Greys', 'open': 'Blues', 'reraise': 'Greens', '4bet':'Purples'},
        'viztitle': 'BLIND VERSUS BLIND',
        'mixedstrategyflag': 'true',
        'purpose': 'to vpp more',
        }, 
    
    'vsOpen': {
        'fileDirPattern': '**/*vsOpen/*.txt', 
        'heroPositions': ('EP', 'MP', 'HJ', 'CO', 'BTN', 'SB'),
        'heroStackDepths': ('15BB', '20BB', '25BB', '30BB', '50BB', '100BB'),
        'heroActions': ('jam', '3bet', 'call'),
        'heroUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'subplotcolors': {'jam': 'Reds', '3bet': 'Greens', 'call': 'Greys'},
        'viztitle': 'VERSUS OPEN',
        'mixedstrategyflag': 'true',
        'purpose': 'to vpp more',
        }, 
    
    'vs3bet': {
        'fileDirPattern': '**/*vs3bet/*.txt',
        'heroPositions': ('MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('30BB', '50BB', '100BB'),
        'heroActions': ('jam', '4bet', 'call'),
        'heroUseCaseVariants': ('vsSB', 'vsBB', 'vsHJ', 'vsCO', 'vsBTN'),
        'subplotcolors': {'jam': 'Reds', '4bet': 'Purples', 'call': 'Greys'},
        'viztitle': 'VERSUS 3BET',
        'mixedstrategyflag': 'false',
        },
    
    'sqz': {
        'fileDirPattern': '**/*sqz/*.txt',
        'heroPositions': ('CO', 'BTN', 'SB', 'BB'),
        'heroStackDepths': ('30BB', '50BB', '100BB'),
        'heroActions': ('jam', 'sqz', 'call'),
        'heroUseCaseVariants': ('vsMPandHJ', 
                            'vsMPandCO', 
                            'vsMPandBTN', 
                            'vsMPandSB', 
                            'vsHJandCO', 
                            'vsHJandBTN', 
                            'vsHJandSB', 
                            'vsCOandBTN', 
                            'vsCOandSB',
                            'vsBTNandSB'
                            ),

        'subplotcolors': {'jam': 'Reds', 'sqz': 'Greens', 'call': 'Greys'},
        'viztitle': 'SQUEEZE',
        'mixedstrategyflag': 'true',
        'purpose': 'to vpp more',

        },
        
    }

betSizes = {
    'RFI-polar-2-2.3x': {
        'parentUseCase': 'RFI-polar',
        'heroPositions': ('EP', 'MP', 'LJ', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('15BB',),
        'heroActions': ('open',),    
        'heroBetSize': '2x-2.3x',
        },

    'RFI-altStrat-2-2.3x': {
        'parentUseCase': 'RFI-altStrat',
        'heroPositions': ('LJ', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('15BB', '20BB'),
        'heroActions': ('open',),    
        'heroBetSize': '2x-2.3x',
        },

    'RFI-linear-2.5x': {
        'parentUseCase': 'RFI-linear',
        'heroPositions': ('BTN',),
        'heroStackDepths': ('40-50BB',),
        'heroActions': ('open',),    
        'heroBetSize': '2.5x',
        },
    
    'RFI-linear-2.8x': {
        'parentUseCase': 'RFI-linear',
        'heroPositions': ('BTN',),
        'heroStackDepths': ('60-100BB',),
        'heroActions': ('open',),    
        'heroBetSize': '2.8x',
        },

    'BBdefends-vs2x': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('15BB', '20BB', '25BB'),
        'heroActions': ('jam', 'call',),    
        'counteredSize': 'vs 2x'
        },

    'BBdefends-3.5-4x(vs2x)': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('15BB', '20BB', '25BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '3.5x-4x',
        'counteredSize': 'vs 2x'
        },

    'BBdefends-vs2.2x': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('30BB'),
        'heroActions': ('jam', 'call',),    
        'counteredSize': 'vs 2.2x'
        },

    'BBdefends-3.5-4x(vs2.2x)': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('30BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '3.5x-4x',
        'counteredSize': 'vs 2.2x'
        },

    'BBdefends-vs2.5x': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('jam', 'call',),    
        'counteredSize': 'vs 2.5x'
        },

    'BBdefends-3.5-4x(vs2.5x)': {
        'parentUseCase': 'BBdefends',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('BB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '3.5x-4x',
        'counteredSize': 'vs 2.5x'
        },
    
    'blindvsblind(SB)-3x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('Unopened'),
        'heroPositions': ('SB',),
        'heroStackDepths': ('20BB', '25BB'),
        'heroActions': ('open',),    
        'heroBetSize': '3x',
        },

    'blindvsblind(SB)-3.8x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('Unopened'),
        'heroPositions': ('SB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('open',),    
        'heroBetSize': '3.8x',
        },
    
    'blindvsblind(SB)-4x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('Unopened'),
        'heroPositions': ('SB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('open',),    
        'heroBetSize': '4x',
        },

    'blindvsblind(SB)-vs3xISO': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('LimpvsISO',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('20BB', '25BB'),
        'heroActions': ('jam', 'limpcheckcall'),    
        'counteredSize': 'vs 3xISO'
        },

    'blindvsblind(SB)-vs3.8xISO': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('LimpvsISO',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('jam', 'limpcheckcall'),    
        'counteredSize': 'vs 3.8xISO'
        },

    'blindvsblind(SB)-vs4xISO': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('LimpvsISO',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('limpcheckcall',),    
        'counteredSize': 'vs 4xISO'
        },

    'blindvsblind(SB)-3.75x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('LimpvsISO',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('reraise',),    
        'heroBetSize': '3.75x',
        'counteredSize': 'vs 4xISO'
        },

    'blindvsblind(SB)-vs2.5x3bet': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vs3bet',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('jam', 'limpcheckcall'),    
        'counteredSize': 'vs 2.5x3bet'
        },

    'blindvsblind(SB)-vs3x3bet': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vs3bet',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('jam', 'limpcheckcall'),    
        'counteredSize': 'vs 3x3bet'
        },


    'blindvsblind(SB)-2.8x(vs3x3bet)': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vs3bet',),
        'heroPositions': ('SB',),
        'heroStackDepths': ('100BB',),
        'heroActions': ('4bet',),    
        'heroBetSize': '2.8x',
        'counteredSize': 'vs 3x3bet'
        },

    'blindvsblind(BB)-3x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsLimp',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('20BB', '25BB'),
        'heroActions': ('open',),    
        'heroBetSize': '3x',
        },
    
    'blindvsblind(BB)-3.8x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsLimp',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('open',),    
        'heroBetSize': '3.8x',
        },

    'blindvsblind(BB)-4x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsLimp',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('open',),    
        'heroBetSize': '4x',
        },

    'blindvsblind(BB)-vs3.8x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsRaise',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('jam',),    
        'counteredSize': 'vs 3.8x'
        },

    'blindvsblind(BB)-vs3x': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsRaise',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('20BB', '25BB'),
        'heroActions': ('jam', 'limpcheckcall'),    
        'counteredSize': 'vs 3x'
        },

    'blindvsblind(BB)-2.5x(vs3.8x)': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsRaise',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('30BB',),
        'heroActions': ('3bet',),    
        'heroBetSize': '2.5x',
        'counteredSize': 'vs 3.8x',
        },

    'blindvsblind(BB)-3x(vs4x)': {
        'parentUseCase': 'blindvsblind',
        'parentUseCaseVariants': ('vsRaise',),
        'heroPositions': ('BB',),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '3x',
        'counteredSize': 'vs 4x',
        },

    'vsOpen(IP)-2.6x': {
        'parentUseCase': 'vsOpen',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO'),
        'heroPositions': ('EP', 'MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('25BB', '30BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '2.6x',
        },
    
    'vsOpen(OOP)-3x': {
        'parentUseCase': 'vsOpen',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('SB',),
        'heroStackDepths': ('25BB',),
        'heroActions': ('3bet',),    
        'heroBetSize': '3x',
        },

    'vsOpen(OOP)-3.5-4x': {
        'parentUseCase': 'vsOpen',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('SB',),
        'heroStackDepths': ('30BB', '50BB', '100BB'),
        'heroActions': ('3bet',),    
        'heroBetSize': '3.5-4x',
        },

    'vsOpen(IP)-3x': {
        'parentUseCase': 'vsOpen',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO'),
        'heroPositions': ('EP', 'MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('50BB',),
        'heroActions': ('3bet',),    
        'heroBetSize': '3x',
        },
    
    'vsOpen(IP)-3.5x': {
        'parentUseCase': 'vsOpen',
        'parentUseCaseVariants': ('vsEP', 'vsMP', 'vsHJ', 'vsCO'),
        'heroPositions': ('EP', 'MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('100BB',),
        'heroActions': ('3bet',),    
        'heroBetSize': '3.5x',
        },

    'vs3bet(IP)-vs3.5x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsSB', 'vsBB'),
        'heroPositions': ('MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('30BB',),
        'heroActions': ('jam', 'call'),    
        'counteredSize': 'vs 3.5x',
        },

    'vs3bet(OOP)-vs2.6x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('MP', 'HJ', 'CO'),
        'heroStackDepths': ('30BB',),
        'heroActions': ('jam', 'call'),    
        'heroBetSize': 'vs 2.6x',
        },

    'vs3bet(IP)-vs4x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsSB', 'vsBB'),
        'heroPositions': ('MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('50BB','100BB'),
        'heroActions': ('jam', 'call'),    
        'counteredSize': 'vs 4x',
        },

    'vs3bet(OOP)-vs3x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('MP', 'HJ', 'CO'),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('jam', 'call'),    
        'heroBetSize': 'vs 3x',
        },

    'vs3bet(IP)-2.2x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsSB', 'vsBB'),
        'heroPositions': ('MP', 'HJ', 'CO', 'BTN'),
        'heroStackDepths': ('50BB', '100BB',),
        'heroActions': ('4bet',),    
        'heroBetSize': '2.2x',
        'counteredSize': 'vs 4x'
        },

    'vs3bet(OOP)-2.6-2.8x': {
        'parentUseCase': 'vs3bet',
        'parentUseCaseVariants': ('vsHJ', 'vsCO', 'vsBTN'),
        'heroPositions': ('MP', 'HJ', 'CO'),
        'heroStackDepths': ('50BB', '100BB'),
        'heroActions': ('4bet',),    
        'heroBetSize': '2.6-2.8x',
        'counteredSize': 'vs 3x'
        },

    'sqz(IP)-3.5x': {
        'parentUseCase': 'sqz',
        'parentUseCaseVariants': ('vsMPandHJ', 'vsMPandCO', 'vsHJandCO'),
        'heroPositions': ('CO', 'BTN'),
        'heroStackDepths': ('30BB',),
        'heroActions': ('sqz',),    
        'heroBetSize': '3.5x',
        },

    'sqz(IP)-3.75x': {
        'parentUseCase': 'sqz',
        'parentUseCaseVariants': ('vsMPandHJ', 'vsMPandCO', 'vsHJandCO'),
        'heroPositions': ('CO', 'BTN'),
        'heroStackDepths': ('50BB',),
        'heroActions': ('sqz',),    
        'heroBetSize': '3.75x',
        },

    'sqz(OOP)-4.5x': {
        'parentUseCase': 'sqz',
        'parentUseCaseVariants': ('vsMPandHJ', 
                            'vsMPandCO', 
                            'vsMPandBTN', 
                            'vsMPandSB', 
                            'vsHJandCO', 
                            'vsHJandBTN', 
                            'vsHJandSB', 
                            'vsCOandBTN', 
                            'vsCOandSB',
                            'vsBTNandSB'
                            ),
        'heroPositions': ('SB', 'BB'),
        'heroStackDepths': ('50BB',),
        'heroActions': ('sqz',),    
        'heroBetSize': '4.5x',
        },

    'sqz(IP)-4.5x': {
        'parentUseCase': 'sqz',
        'parentUseCaseVariants': ('vsMPandHJ', 'vsMPandCO', 'vsHJandCO'),
        'heroPositions': ('CO', 'BTN'),
        'heroStackDepths': ('100BB',),
        'heroActions': ('sqz',),    
        'heroBetSize': '4.5x',
        },

    'sqz(OOP)-5.5x': {
        'parentUseCase': 'sqz',
        'parentUseCaseVariants': ('vsMPandHJ', 
                            'vsMPandCO', 
                            'vsMPandBTN', 
                            'vsMPandSB', 
                            'vsHJandCO', 
                            'vsHJandBTN', 
                            'vsHJandSB', 
                            'vsCOandBTN', 
                            'vsCOandSB',
                            'vsBTNandSB'
                            ),
        'heroPositions': ('SB', 'BB'),
        'heroStackDepths': ('100BB',),
        'heroActions': ('sqz',),    
        'heroBetSize': '5.5x',
        },
       
    }

handClasses = {
    'Pair': { 
        'property': 'Two hole cards of equal rank',
        'variants': ('hp', 'mp', 'lp'), 
        'bfcolor': '#5c4033', 
        'wfcolor': '#FFFFFF', 
        'bfmuted': '#D3D3D3', 
        'wfmuted': '#FFFFFF'
        },

    'Ace': {
        'property': 'Two hole cards that contain one ace; no other class (except Pair - e.g. AA) is allowed to contain an ace',
        'variants': ('ahs', 'ams', 'als', 'aho', 'amo', 'alo'), 
        'bfcolor': '#FFFFFF', 
        'wfcolor': '#5c4033', 
        'bfmuted': '#FFFFFF', 
        'wfmuted': '#D3D3D3'
        },

    'Connector': { 
        'property': 'Two consecutive hole cards',
        'variants': ('chs', 'cms', 'cls', 'cho', 'cmo', 'clo'), 
        'bfcolor': '#5c4033', 
        'wfcolor': '#FFFFFF', 
        'bfmuted': '#D3D3D3', 
        'wfmuted': '#FFFFFF'
        },

    'Gapper Sr.': { 
        'property': 'Two gapped (unconsecutive) hole cards; only one card is ranked T-K',
        'variants': ('hhs', 'hms', 'hls', 'hho', 'hmo', 'hlo'), 
        'bfcolor': '#FFFFFF', 
        'wfcolor': '#5c4033', 
        'bfmuted': '#FFFFFF', 
        'wfmuted': '#D3D3D3'
        },

    'Gapper Jr.': { 
        'property': 'Two gapped (unconsecutive) hole cards; neither card is ranked T-K',
        'variants': ('mms', 'mls', 'lls', 'mmo', 'mlo', 'llo'), 
        'bfcolor' : '#5c4033', 
        'wfcolor' : '#FFFFFF', 
        'bfmuted': '#D3D3D3', 
        'wfmuted': '#FFFFFF'
        },

    }

handVariants = {
     'hp': 'high-pair',
     'mp': 'mid-pair',
     'lp': 'low-pair',
    'ahs': 'ace-high-suited',
    'ams': 'ace-mid-suited',
    'als': 'ace-low-suited',
    'aho': 'ace-high-offsuit',
    'amo': 'ace-mid-offsuit',
    'alo': 'ace-low-offsuit',
    'chs': 'connected-high-suited',
    'cms': 'connected-mid-suited',
    'cls': 'connected-low-suited',
    'cho': 'connected-high-offsuit',
    'cmo': 'connected-mid-offsuit',
    'clo': 'connected-low-offsuit',
    'hhs': 'high-high-suited',
    'hms': 'high-mid-suited',
    'hls': 'high-low-suited',
    'hho': 'high-high-offsuit',
    'hmo': 'high-mid-offsuit',
    'hlo': 'high-low-offsuit',
    'mms': 'mid-mid-suited',    
    'mls': 'mid-low-suited',
    'lls': 'low-low-suited',
    'mmo': 'mid-mid-offsuit',
    'mlo': 'mid-low-offsuit',
    'llo': 'low-low-offsuit',
    }

handMatrix = {
    'AA': {'code': 'hp', 'combos': 6},
    'KK': {'code': 'hp', 'combos': 6},
    'QQ': {'code': 'hp', 'combos': 6},
    'JJ': {'code': 'hp', 'combos': 6},
    'TT': {'code': 'hp', 'combos': 6},
    '99': {'code': 'mp', 'combos': 6},
    '88': {'code': 'mp', 'combos': 6},
    '77': {'code': 'mp', 'combos': 6},
    '66': {'code': 'mp', 'combos': 6},
    '55': {'code': 'lp', 'combos': 6},
    '44': {'code': 'lp', 'combos': 6},
    '33': {'code': 'lp', 'combos': 6},
    '22': {'code': 'lp', 'combos': 6},
    'AKs': {'code': 'ahs', 'combos': 4},
    'AQs': {'code': 'ahs', 'combos': 4},
    'AJs': {'code': 'ahs', 'combos': 4},
    'ATs': {'code': 'ahs', 'combos': 4},
    'A9s': {'code': 'ams', 'combos': 4},
    'A8s': {'code': 'ams', 'combos': 4},
    'A7s': {'code': 'ams', 'combos': 4},
    'A6s': {'code': 'ams', 'combos': 4},
    'A5s': {'code': 'als', 'combos': 4},
    'A4s': {'code': 'als', 'combos': 4},
    'A3s': {'code': 'als', 'combos': 4},
    'A2s': {'code': 'als', 'combos': 4},
    'KQs': {'code': 'chs', 'combos': 4},
    'KJs': {'code': 'hhs', 'combos': 4},
    'KTs': {'code': 'hhs', 'combos': 4},
    'K9s': {'code': 'hms', 'combos': 4},
    'K8s': {'code': 'hms', 'combos': 4},
    'K7s': {'code': 'hms', 'combos': 4},
    'K6s': {'code': 'hms', 'combos': 4},
    'K5s': {'code': 'hls', 'combos': 4},
    'K4s': {'code': 'hls', 'combos': 4},
    'K3s': {'code': 'hls', 'combos': 4},
    'K2s': {'code': 'hls', 'combos': 4},
    'QJs': {'code': 'chs', 'combos': 4},
    'QTs': {'code': 'hhs', 'combos': 4},
    'Q9s': {'code': 'hms', 'combos': 4},
    'Q8s': {'code': 'hms', 'combos': 4},
    'Q7s': {'code': 'hms', 'combos': 4},
    'Q6s': {'code': 'hms', 'combos': 4},
    'Q5s': {'code': 'hls', 'combos': 4},
    'Q4s': {'code': 'hls', 'combos': 4},
    'Q3s': {'code': 'hls', 'combos': 4},
    'Q2s': {'code': 'hls', 'combos': 4},
    'JTs': {'code': 'chs', 'combos': 4},
    'J9s': {'code': 'hms', 'combos': 4},
    'J8s': {'code': 'hms', 'combos': 4},
    'J7s': {'code': 'hms', 'combos': 4},
    'J6s': {'code': 'hms', 'combos': 4},
    'J5s': {'code': 'hls', 'combos': 4},
    'J4s': {'code': 'hls', 'combos': 4},
    'J3s': {'code': 'hls', 'combos': 4},
    'J2s': {'code': 'hls', 'combos': 4},
    'T9s': {'code': 'chs', 'combos': 4},
    'T8s': {'code': 'hms', 'combos': 4},
    'T7s': {'code': 'hms', 'combos': 4},
    'T6s': {'code': 'hms', 'combos': 4},
    'T5s': {'code': 'hls', 'combos': 4},
    'T4s': {'code': 'hls', 'combos': 4},
    'T3s': {'code': 'hls', 'combos': 4},
    'T2s': {'code': 'hls', 'combos': 4},
    '98s': {'code': 'cms', 'combos': 4},
    '97s': {'code': 'mms', 'combos': 4},
    '96s': {'code': 'mms', 'combos': 4},
    '95s': {'code': 'mls', 'combos': 4},
    '94s': {'code': 'mls', 'combos': 4},
    '93s': {'code': 'mls', 'combos': 4},
    '92s': {'code': 'mls', 'combos': 4},
    '87s': {'code': 'cms', 'combos': 4},
    '86s': {'code': 'mms', 'combos': 4},
    '85s': {'code': 'mls', 'combos': 4},
    '84s': {'code': 'mls', 'combos': 4},
    '83s': {'code': 'mls', 'combos': 4},
    '82s': {'code': 'mls', 'combos': 4},
    '76s': {'code': 'cms', 'combos': 4},
    '75s': {'code': 'mls', 'combos': 4},
    '74s': {'code': 'mls', 'combos': 4},
    '73s': {'code': 'mls', 'combos': 4},
    '72s': {'code': 'mls', 'combos': 4},
    '65s': {'code': 'cms', 'combos': 4},
    '64s': {'code': 'mls', 'combos': 4},
    '63s': {'code': 'mls', 'combos': 4},
    '62s': {'code': 'mls', 'combos': 4},
    '54s': {'code': 'cls', 'combos': 4},
    '53s': {'code': 'lls', 'combos': 4},
    '52s': {'code': 'lls', 'combos': 4},
    '43s': {'code': 'cls', 'combos': 4},
    '42s': {'code': 'lls', 'combos': 4},
    '32s': {'code': 'cls', 'combos': 4},
    'AKo': {'code': 'aho', 'combos': 12},
    'AQo': {'code': 'aho', 'combos': 12},
    'AJo': {'code': 'aho', 'combos': 12},
    'ATo': {'code': 'aho', 'combos': 12},
    'A9o': {'code': 'amo', 'combos': 12},
    'A8o': {'code': 'amo', 'combos': 12},
    'A7o': {'code': 'amo', 'combos': 12},
    'A6o': {'code': 'amo', 'combos': 12},
    'A5o': {'code': 'alo', 'combos': 12},
    'A4o': {'code': 'alo', 'combos': 12},
    'A3o': {'code': 'alo', 'combos': 12},
    'A2o': {'code': 'alo', 'combos': 12},
    'KQo': {'code': 'cho', 'combos': 12},
    'KJo': {'code': 'hho', 'combos': 12},
    'KTo': {'code': 'hho', 'combos': 12},
    'K9o': {'code': 'hmo', 'combos': 12},
    'K8o': {'code': 'hmo', 'combos': 12},
    'K7o': {'code': 'hmo', 'combos': 12},
    'K6o': {'code': 'hmo', 'combos': 12},
    'K5o': {'code': 'hlo', 'combos': 12},
    'K4o': {'code': 'hlo', 'combos': 12},
    'K3o': {'code': 'hlo', 'combos': 12},
    'K2o': {'code': 'hlo', 'combos': 12},
    'QJo': {'code': 'cho', 'combos': 12},
    'QTo': {'code': 'hho', 'combos': 12},
    'Q9o': {'code': 'hmo', 'combos': 12},
    'Q8o': {'code': 'hmo', 'combos': 12},
    'Q7o': {'code': 'hmo', 'combos': 12},
    'Q6o': {'code': 'hmo', 'combos': 12},
    'Q5o': {'code': 'hlo', 'combos': 12},
    'Q4o': {'code': 'hlo', 'combos': 12},
    'Q3o': {'code': 'hlo', 'combos': 12},
    'Q2o': {'code': 'hlo', 'combos': 12},
    'JTo': {'code': 'cho', 'combos': 12},
    'J9o': {'code': 'hmo', 'combos': 12},
    'J8o': {'code': 'hmo', 'combos': 12},
    'J7o': {'code': 'hmo', 'combos': 12},
    'J6o': {'code': 'hmo', 'combos': 12},
    'J5o': {'code': 'hlo', 'combos': 12},
    'J4o': {'code': 'hlo', 'combos': 12},
    'J3o': {'code': 'hlo', 'combos': 12},
    'J2o': {'code': 'hlo', 'combos': 12},
    'T9o': {'code': 'cho', 'combos': 12},
    'T8o': {'code': 'hmo', 'combos': 12},
    'T7o': {'code': 'hmo', 'combos': 12},
    'T6o': {'code': 'hmo', 'combos': 12},
    'T5o': {'code': 'hlo', 'combos': 12},
    'T4o': {'code': 'hlo', 'combos': 12},
    'T3o': {'code': 'hlo', 'combos': 12},
    'T2o': {'code': 'hlo', 'combos': 12},
    '98o': {'code': 'cmo', 'combos': 12},
    '97o': {'code': 'mmo', 'combos': 12},
    '96o': {'code': 'mmo', 'combos': 12},
    '95o': {'code': 'mlo', 'combos': 12},
    '94o': {'code': 'mlo', 'combos': 12},
    '93o': {'code': 'mlo', 'combos': 12},
    '92o': {'code': 'mlo', 'combos': 12},
    '87o': {'code': 'cmo', 'combos': 12},
    '86o': {'code': 'mmo', 'combos': 12},
    '85o': {'code': 'mlo', 'combos': 12},
    '84o': {'code': 'mlo', 'combos': 12},
    '83o': {'code': 'mlo', 'combos': 12},
    '82o': {'code': 'mlo', 'combos': 12},
    '76o': {'code': 'cmo', 'combos': 12},
    '75o': {'code': 'mlo', 'combos': 12},
    '74o': {'code': 'mlo', 'combos': 12},
    '73o': {'code': 'mlo', 'combos': 12},
    '72o': {'code': 'mlo', 'combos': 12},
    '65o': {'code': 'cmo', 'combos': 12},
    '64o': {'code': 'mlo', 'combos': 12},
    '63o': {'code': 'mlo', 'combos': 12},
    '62o': {'code': 'mlo', 'combos': 12},
    '54o': {'code': 'clo', 'combos': 12},
    '53o': {'code': 'llo', 'combos': 12},
    '52o': {'code': 'llo', 'combos': 12},
    '43o': {'code': 'clo', 'combos': 12},
    '42o': {'code': 'llo', 'combos': 12},
    '32o': {'code': 'clo', 'combos': 12},
    }

cardclasses= { 
    'ace': {'code': 'a', 'variants': ('A',)},
    'high': {'code': 'h', 'variants': ('T', 'J', 'Q', 'K')},
    'mid': { 'code': 'm', 'variants': ('6', '7', '8', '9')},
    'low': { 'code': 'l', 'variants': ('2', '3', '4', '5')},
    }

flopsuitedness = ('rainbow', 'flushdraw', 'monotone') 

flopconnectedness = ('0-straight', '1-straight', '2-straight', 'straight')   

floptypes = ('classic-dry', 'dry-polar', 'dynamic-dry', 'dynamic-wet', 'air-strong')

betsizingmatrix = {
    'SRP-100BB-flop': { 
        'ovr': ('160',),
        'big': ('90',),
        'med': ('60',),
        'sml': ('30',),
        'OOPrse': ('40', '60'),
        'addallin': False
        },
    
    'SRP-100BB-turn': { 
        'ovr': ('200',),
        'big': ('120',),
        'med': ('80',),
        'sml': ('40',),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-100BB-river': { 
        'ovr': ('200',),
        'big': ('200',),
        'med': ('100',),
        'sml': ('50'),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-75BB-flop': { 
        'big': ('90',),
        'sml': ('30',),
        'OOPrse': ('40', '60'),
        'addallin': False
        },
    
    'SRP-75BB-turn': { 
        'big': ('100',),
        'med': ('66',),
        'sml': ('33',),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-75BB-river': { 
        'big': ('200',),
        'med': ('100',),
        'sml': ('50'),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-50BB-flop': { 
        'ovr': (),
        'big': ('75',),
        'med': ('50',),
        'sml': ('30',),
        'OOPrse': ('40', '60'),
        'addallin': False
        },
    
    'SRP-50BB-turn': { 
        'ovr': (),
        'big': ('110',),
        'med': ('70',),
        'sml': ('35',),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-50BB-river': { 
        'ovr': (),
        'big': ('120',),
        'med': ('80',),
        'sml': ('40',),
        'dnk': ('30', '90'),
        'addallin': True
        },

    'SRP-30BB-flop': {
        'ovr': (),
        'big': ('70',),
        'med': ('35',),
        'sml': ('20',),
        'OOPrse': ('35', '55'),
        'addallin': True
        },

    'SRP-30BB-turn': {
        'ovr': (),
        'big': ('105',),
        'med': ('70',),
        'sml': ('35',),
        'dnk': ('30', '70'),
        'addallin': True
        },

    'SRP-30BB-river': {
        'ovr': (),
        'big': ('120',),
        'med': ('80',),
        'sml': ('40',),
        'dnk': ('30', '70'),
        'addallin': True
        },

    }

postflopcategories = { 
    'classic-dry': 'no drastic equity shifts; not a ton of hands OOP can float',
    'dry-polar': 'polarized strategy with no protection concerns',
    'polar-linear': 'mostly polarized with some protection concerns',
    'dynamic': 'drastic shifts in equity; high frequency bet or check',
    'wet': 'significant shifts in equity yet equities run fairly close; neither position puts much money in',
    'air-strong': 'OOP player has a polarized distribution of air and strength',

    }

postflopusecases = { 
    'SRP': {
        'fileDirPattern': '**/*SRP/*.txt',
        'flop': '',
        'heroPositions': ('LJ', 'BTN'),
        'heroStackDepths': ('30BB', '50BB', '75BB' '100BB'),
        'heroActions': ('bet', 'check', 'raise', 'call'),
        'heroUseCaseVariants': ('vsBB',),
        }, 

    '3bet': { 
        'fileDirPattern': '**/*3bet/*.txt',
        'flop': '',
        'heroPositions': ('LJ', 'BTN'),
        'heroStackDepths': ('30BB', '50BB', '75BB' '100BB'),
        'heroActions': ('bet', 'check', 'raise', 'call'),
        'heroUseCaseVariants': ('vsBB',),
        }

    }

postflopusecasesDEPRECATED = { 

    '3BET-TBD-TBD': { 

        },

    'SRP-BTNvsBB-30BB': {

        'AdKh2s': { 
            'IPflopstrategy': {
                'big': {'freq': 0.22, 'handtypes': ()},
                'med': {'freq': 0.12, 'handtypes': ()},
                'sml': {'freq': 0.61, 'handtypes': ()},
                'chk': {'freq': 0.02, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()},
                'vssml': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'AhJs4s': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.40, 'handtypes': ()},
                'med': {'freq': 0.25, 'handtypes': ()},
                'sml': {'freq': 0.34, 'handtypes': ()},
                'chk': {'freq': 0.01, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                }

            },

        'Ad5h4s': { 
            'IPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP 
                'big': {'freq': 0.70, 'handtypes': ()},
                'med': {'freq': 0.25, 'handtypes': ()},
                'sml': {'freq': 0.04, 'handtypes': ()},
                'chk': {'freq': 0.01, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        },

    'SRP-BTNvsBB-50BB': { 
    
        'AdKh2s': { 
            'IPflopstrategy': {
                'big': {'freq': 0.03, 'handtypes': ()},
                'med': {'freq': 0.02, 'handtypes': ()},
                'sml': {'freq': 0.82, 'handtypes': ()},
                'chk': {'freq': 0.14, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'Ad5h4s': { 
            'IPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP 
                'big': {'freq': 0.10, 'handtypes': ()},
                'med': {'freq': 0.11, 'handtypes': ()},
                'sml': {'freq': 0.52, 'handtypes': ()},
                'chk': {'freq': 0.25, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'AhJs4s': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.04, 'handtypes': ()},
                'med': {'freq': 0.04, 'handtypes': ()},
                'sml': {'freq': 0.90, 'handtypes': ()},
                'chk': {'freq': 0.02, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                }

            },    

        'QsTs9d': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.14, 'handtypes': ()},
                'med': {'freq': 0.50, 'handtypes': ()},
                'sml': {'freq': 0.20, 'handtypes': ()},
                'chk': {'freq': 0.18, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
            
            },

        },


    'SRP-LJvsBB-50BB': {

        'Ad5h4s': {
            'IPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP 
                'big': {'freq': 0.55, 'handtypes': ()},
                'med': {'freq': 0.15, 'handtypes': ()},
                'sml': {'freq': 0.15, 'handtypes': ()},
                'chk': {'freq': 0.15, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },
            
        'QsTs9d': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.02, 'handtypes': ()},
                'med': {'freq': 0.82, 'handtypes': ()},
                'sml': {'freq': 0.14, 'handtypes': ()},
                'chk': {'freq': 0.01, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
            
            },

        },

 
    'SRP-LJvsBB-75BB': { 
    
        '9h3h2h': {
            'IPflopstrategy': {
                'big': {'freq': 0.03, 'handtypes': ()},
                'med': {'freq': 0.00, 'handtypes': ()},
                'sml': {'freq': 0.88, 'handtypes': ()},
                'chk': {'freq': 0.09, 'handtypes': ()}
                },

            'OOPflopstrategy': {

                'vssml': {'raisefreq': 0.0, 'raisehandtypes': ('bare gut shots',), 'callfreq': 0.0, 'callhandtypes': ()},

                }
            
            }

        },

    'SRP-BTNvsBB-100BB': { 
    
        'Kh8s2d': {
            'IPflopstrategy': {
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.02, 'handtypes': ()},
                'sml': {'freq': 0.85, 'handtypes': ()},
                'chk': {'freq': 0.12, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'Ah7s2d': {

            },

        'Ad5h4s': { 
            'IPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP 
                'ovr': {'freq': 0.01, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.02, 'handtypes': ()},
                'sml': {'freq': 0.51, 'handtypes': ()},
                'chk': {'freq': 0.45, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                #figure out how to differentiate handtypes with equity vs blockers for IP and OOP
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
        
            },
        
        'AhJs4s': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.05, 'handtypes': ()},
                'big': {'freq': 0.02, 'handtypes': ()},
                'med': {'freq': 0.03, 'handtypes': ()},
                'sml': {'freq': 0.78, 'handtypes': ()},
                'chk': {'freq': 0.12, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'JsTd2h': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.02, 'handtypes': ()},
                'big': {'freq': 0.02, 'handtypes': ()},
                'med': {'freq': 0.03, 'handtypes': ()},
                'sml': {'freq': 0.88, 'handtypes': ()},
                'chk': {'freq': 0.05, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                }

            },

        'Th8h3h': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.02, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.08, 'handtypes': ()},
                'sml': {'freq': 0.57, 'handtypes': ()},
                'chk': {'freq': 0.32, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                }

            },

        'AdKh2s': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.20, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.01, 'handtypes': ()},
                'sml': {'freq': 0.33, 'handtypes': ()},
                'chk': {'freq': 0.45, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsovr': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
            
            },

        'KdQd6s': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.12, 'handtypes': ()},
                'big': {'freq': 0.03, 'handtypes': ()},
                'med': {'freq': 0.04, 'handtypes': ()},
                'sml': {'freq': 0.36, 'handtypes': ()},
                'chk': {'freq': 0.45, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsovr': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
            
            },

        '8d4s2h': {  
            'IPflopstrategy': { 
                'ovr': {'freq': 0.37, 'handtypes': ()},
                'big': {'freq': 0.03, 'handtypes': ()},
                'med': {'freq': 0.05, 'handtypes': ()},
                'sml': {'freq': 0.07, 'handtypes': ()},
                'chk': {'freq': 0.48, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            }, 

        '9s7s3d': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.09, 'handtypes': ()},
                'big': {'freq': 0.30, 'handtypes': ()},
                'med': {'freq': 0.13, 'handtypes': ()},
                'sml': {'freq': 0.05, 'handtypes': ()},
                'chk': {'freq': 0.43, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'QsTs9d': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.01, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.35, 'handtypes': ()},
                'sml': {'freq': 0.35, 'handtypes': ()},
                'chk': {'freq': 0.28, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
            
            },

        '7h6s5s': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.01, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.43, 'handtypes': ()},
                'sml': {'freq': 0.01, 'handtypes': ()},
                'chk': {'freq': 0.54, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },
    
        },

    'SRP-LJvsBB-100BB': {
   
        'QsTs9d': { 
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.01, 'handtypes': ()},
                'med': {'freq': 0.15, 'handtypes': ()},
                'sml': {'freq': 0.78, 'handtypes': ()},
                'chk': {'freq': 0.05, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
        
            },

        'JsJh4h': {
            'IPflopstrategy': { 
                'ovr': {'freq': 0.00, 'handtypes': ()},
                'big': {'freq': 0.00, 'handtypes': ()},
                'med': {'freq': 0.00, 'handtypes': ()},
                'sml': {'freq': 0.98, 'handtypes': ()},
                'chk': {'freq': 0.02, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                }

            },

        'AdKh2s': {
            'IPflopstrategy': { 
                'big': {'freq': 0.50, 'handtypes': ()},
                'med': {'freq': 0.03, 'handtypes': ()},
                'sml': {'freq': 0.03, 'handtypes': ()},
                'chk': {'freq': 0.44, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },
  
        'AhJs4s': {
            'IPflopstrategy': { 
                'big': {'freq': 0.40, 'handtypes': ()},
                'med': {'freq': 0.20, 'handtypes': ()},
                'sml': {'freq': 0.20, 'handtypes': ()},
                'chk': {'freq': 0.20, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        'Ad5h4s': { 
            'IPflopstrategy': { 
                'big': {'freq': 0.12, 'handtypes': ()},
                'med': {'freq': 0.12, 'handtypes': ()},
                'sml': {'freq': 0.13, 'handtypes': ()},
                'chk': {'freq': 0.63, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }
        
            },

        'Kd3s3h': {
                'IPflopstrategy': { 
                'big': {'freq': 0.05, 'handtypes': ()},
                'med': {'freq': 0.05, 'handtypes': ()},
                'sml': {'freq': 0.30, 'handtypes': ()},
                'chk': {'freq': 0.69, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        '4s4d2d': {
            'IPflopstrategy': { 
                'big': {'freq': 0.05, 'handtypes': ()},
                'med': {'freq': 0.05, 'handtypes': ()},
                'sml': {'freq': 0.36, 'handtypes': ()},
                'chk': {'freq': 0.63, 'handtypes': ()}
                },

            'OOPflopstrategy': {
                'vsbig': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vsmed': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vssml': {'raisefreq': 0.0, 'raisehandtypes': (), 'callfreq': 0.0, 'callhandtypes': ()},
                'vschk': {'callfreq': 0.0, 'callhandtypes': (), 'betfreq': 0.0, 'bethandtypes': ()}
                }

            },

        },

    }

flopclasses = {
    'Pair': { 
        'codes': ('hph', 'hpm', 'hpw', 'mph', 'mpm', 'mpl', 'lph', 'lpm', 'lpl'),
        'suitedness': ('rainbow', 'flushdraw'),
        'connectedness': ('0-straight', '1-straight',)
        },

    'Ace': {
        'codes': ('ahh', 'ahm', 'ahl', 'amm', 'aml', 'all'),
        'suitedness': ('rainbow', 'flushdraw', 'monotone'), 
        'connectedness': ('1-straight', '2-straight', '3-straight')
        },

    'Gapper Sr.': { 
        'codes': ('hhh', 'hhm', 'hhl', 'hmm', 'hml', 'hll'),
        'suitedness': ('rainbow', 'flushdraw', 'monotone'),
        'connectedness': ('0-straight', '1-straight', '2-straight', '3-straight')
        },
    
    'Gapper Jr.': { 
        'codes': ('mmm', 'mml', 'mll', 'lll'),
        'suitedness': ('rainbow', 'flushdraw', 'monotone'),
        'connectedness': ('1-straight', '2-straight', '3-straight')
        },

    }

flopvariants = { 
    'hph': 'high-pair-high', 
    'hpm': 'high-pair-mid', 
    'hpw': 'high-pair-low', 
    'mph': 'mid-pair-high', 
    'mpm': 'mid-pair-mid',
    'mpl': 'mid-pair-low',
    'lph': 'low-pair-high', 
    'lpm': 'low-pair-mid',
    'lpl': 'low-pair-low', 
    'ahh': 'ace-high-high', 
    'ahm': 'ace-high-mid',
    'ahl': 'ace-high-low',
    'amm': 'ace-mid-mid',
    'aml': 'ace-mid-low',
    'all': 'ace-low-low',
    'hhh': 'high-high-high', 
    'hhm': 'high-high-mid',
    'hhl': 'high-high-low',
    'hmm': 'high-mid-mid',
    'hml': 'high-mid-low',
    'hll': 'high-low-low',
    'mmm': 'mid-mid-mid', 
    'mml': 'mid-mid-low',
    'mll': 'mid-low-low',
    'lll': 'low-low-low',
    }


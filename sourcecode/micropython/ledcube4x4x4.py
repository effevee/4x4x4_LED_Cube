import machine
import utime

class ledcube :

    """a 4x4x4 LED cube consisting of 4 levels of 4 by 4 LEDs with all the anodes on each level commoned. Each cathode of the LEDs
       is connected across the 4 levels into 16 columns. To light a particular LED the level has to be put high and the column low.
       This is controlled with 2 SN74HC595 shift registers so that only 3 GPIO pins are required to control the column LEDs on the µC,
       4 additional GPIO pins select the level of the output :
       - 1 data pin (SN74HC595 SER pin 14) to input 16 bits of column data into the data register
       - 1 clock pin (SN74HC595 SRCLK pin 11) to shift the data bits into the data register
       - 1 latch pin (SN74HV595 RCLK pin 12) to copy the 16 data bits from the data into the latch register and set the output pins
       To protect the shift registers, 4 BC547 NPN transistors are used to limit the source current of the level ports (commoned anodes).
       
       the SN74HC595 shift registers are daisy chained :
       shift #1  shift #2  µController
       ========  ========  =========== 
        QH'    --> SER    --> gpio pin
        SRCLK  --> SRCLK  --> gpio pin
        RCLK   --> RCLK   --> gpio pin
        OE#    --> OE#    --> GND
        GND    --> GND    --> GND
        SRCLR# --> SRCLR# --> VCC
        VCC    --> VCC    --> VCC
       
       the columns of the LEDs are connected to the SN74HC595 shift registers as follows :
       LED  shift #1  shift #2
       ==== ========  ========
        C0 --> QA
        C1 --> QB
        C2 --> QC
        C3 --> QD
        C4 --> QE
        C5 --> QF
        C6 --> QG
        C7 --> QH
        C8 -----------> QA
        C9 -----------> QB
        C10 ----------> QC
        C11 ----------> QD 
        C12 ----------> QE 
        C13 ----------> QF 
        C14 ----------> QG 
        C15 ----------> QH
        
        The levels of the LED cube are connected to the µController as follows :
        LED level  µController     
        =========  ===========
        L0 --------> gpio pin
        L1 --------> gpio pin
        L2 --------> gpio pin
        L3 --------> gpio pin
    """
       
 
    def __init__(self, data_pin, clock_pin, latch_pin, L0_pin, L1_pin, L2_pin, L3_pin, debug=True):
        
        """constructor 4x4x4 LED cube """
        
        try:
            self.data = data_pin
            self.clock = clock_pin
            self.latch = latch_pin
            self.Lv = [L0_pin, L1_pin, L2_pin, L3_pin]
            self.da = None
            self.cl = None
            self.la = None
            self.lv = [None, None, None, None]
            self.debug = debug
        
        except Exception as E:
            if self.debug:
                print("4x4x4 LED Cube __init__ error: ",E)

    
    def start(self):
        
        """Initialise 4x4x4 LED Cube"""
        
        try:
            # make pin objects
            self.da = machine.Pin(self.data, machine.Pin.OUT)
            self.cl = machine.Pin(self.clock, machine.Pin.OUT)
            self.la = machine.Pin(self.latch, machine.Pin.OUT)
            for l in range(len(self.Lv)):
                self.lv[l] = machine.Pin(self.Lv[l], machine.Pin.OUT)
            # initialise pin objects
            self.da.value(0)
            self.cl.value(0)
            self.la.value(0)
            for l in range(len(self.lv)):
                self.lv[l].value(0)
        
        except Exception as E:
            if self.debug:
                print("4x4x4 LED Cube start error: ",E)

    
    def shift_data(self, data, levl):
        
        """ helper function to put data (list of 16 bit values) in the data and latch registers and to the output pins.
            levl sets the level gpio values high to activate the level of the LED cube.
            the SN74HC595 data registers will be filled as follows:
              shift register #1       shift register #2
            ======================= ============================
            QA QB QC QD QE QF QG QH QA QB QC  QD  QE  QF  QG  QH   <-- SN74HC595
             |  |  |  |  |  |  |  |  |  |  |   |   |   |   |   |
             v  v  v  v  v  v  v  v  v  v  v   v   v   v   v   v
            C0 C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12 C13 C14 C15  <-- LED data coloms
            ======================= ============================
            15 14 13 12 11 10  9  8  7  6  5   4   3   2   1   0   <-- bit positions (shift in reverse order !!!)
        """
        
        # set latch low to begin shifting
        self.la.value(0)
        # shift bits from bit list into the data registers
        for bit in data:
            self.cl.value(0)
            self.da.value(bit)
            self.cl.value(1)
        # set latch high to shift into the latch register and to the output pins
        self.la.value(1)
        self.cl.value(0)
        self.da.value(0)
        # set level
        for l in range(len(self.lv)):
            self.lv[l].value(levl[l])


    def display(self, pat_L0, pat_L1, pat_L2, pat_L3, delay_ms):
        
        """ display the LED patterns for the levels L0, L1, L2 and L3 of the 4x4x4 LED Cube during delay_ms microseconds

           LED levels : set high to activate (source current from external VCC)
           ==========
           L3 : level 3 -> top
           L2 : level 2 
           L1 : level 1 
           L0 : level 0 -> bottom

           LED columns : set low to activate (sink current to ground)
           ===========
           C12 - C13 - C14 - C15
            |     |     |     |
           C8 -- C9 -- C10 - C11
            |     |     |     |
           C4 -- C5 -- C6 -- C7
            |     |     |     |
           C0 -- C1 -- C2 -- C3
 
           LED pattern frame --> 0b0123456789012345, 0b0123456789012345, 0b0123456789012345, 0b0123456789012345, 150
                                          |                   |                   |                   |           |
                                          L0                  L1                  L2                  L3        delay (ms) 

           A LED frame consists of 4 LED patterns (16 bits or 2 bytes) for each level of LEDs, followed by a delay time in milliseconds.
           The different patterns on each level are multiplexed until the delay time has elapsed.
        """
 
        try:
            # column pattern from different levels to list
            patterns = [pat_L0, pat_L1, pat_L2, pat_L3]
            # start timer
            start_ms = utime.ticks_ms()
            current_ms = start_ms
            # multiplex levels of LEDs until delay_ms has passed
            while current_ms < start_ms + delay_ms:
                # loop through patterns
                for idx, pat in enumerate(patterns):
                    # convert column pattern to binary list
                    bits = []
                    # complement of bit pattern (low to activate LED) 
                    # bits = [(~int(x) + 2) for x in list('{0:0b}'.format(pat))]
                    # bit pattern (high to activate LED) 
                    bits = [int(x) for x in list('{0:0b}'.format(pat))]
                    # insert missing 1 bits if necessary 
                    while len(bits) < 16: 
                        bits.insert(0, 0)
                    # set level bits (low to activate)
                    levl = [1]*4
                    levl[idx] = 0
                    # debug info
                    if self.debug:
                        print('column pattern: ', bits[0:16], ' - levels: ', levl)
                    # reverse shift the bits into the shift registers
                    bits.reverse()
                    self.shift_data(bits, levl)
                    # minimum display time
                    utime.sleep_ms(2)
                    # turnoff levels & columns
                    bits = []
                    bits = [0]*16
                    levl = [1]*4
                    self.shift_data(bits, levl)                    
                # update current time
                current_ms = utime.ticks_ms()
           
        except Exception as E:
            if self.debug:
                print("4x4x4 LED Cube display error: ",E)
            
    
    def clear(self):
        
        """ clear 4x4x4 LED Cube """

        self.display(0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 100)

    
    def stop(self):
        
        """ stop 4x4x4 LED Cube """
        
        try:
            self.clear()
            del self.da
            del self.cl
            del self.la
            del self.lv
        
        except Exception as E:
            if self.debug:
                print("4x4x4 LED Cube stop error: ",E)

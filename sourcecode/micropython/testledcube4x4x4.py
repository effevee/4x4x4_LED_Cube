import ledcube4x4x4

# pins
DATA = 19
CLOCK = 18
LATCH = 5
L0 = 17
L1 = 16
L2 = 4
L3 = 15

# frames
FRAME = [
    # ---------------------------------------
    # round and round
    # ---------------------------------------
    0b1000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0100000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0010000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150, 
    0b0001000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000100000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000010000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000001, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000010, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000100, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000001000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000010000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000100000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000010000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000001000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000100000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000001000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    #
    0b0000000000000000, 0b0000000001000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000100000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000001000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000010000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000100000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000010000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000001000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000100, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000010, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000001, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000010000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000100000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0001000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0010000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0100000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b1000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    #
    0b0000000000000000, 0b0000000000000000, 0b1000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0100000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0010000000000000, 0b0000000000000000, 150, 
    0b0000000000000000, 0b0000000000000000, 0b0001000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000100000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000010000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000001, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000010, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000100, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000001000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000010000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000100000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000010000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000001000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000100000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000001000000, 0b0000000000000000, 150,
    #
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000001000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000100000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000001000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000010000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000100000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000010000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000001000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000100, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000010, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000001, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000010000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0001000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0010000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0100000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1000000000000000, 150,
    # ---------------------------------------
    # crazy elevator
    # ---------------------------------------
    0b1111100110011111, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b1111100110011111, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b1111100110011111, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111100110011111, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000011001100000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000011001100000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000011001100000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000011001100000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000011001100000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000011001100000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000011001100000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111100110011111, 150,
    0b0000000000000000, 0b0000000000000000, 0b1111100110011111, 0b0000000000000000, 150,
    0b0000000000000000, 0b1111100110011111, 0b0000000000000000, 0b0000000000000000, 150,
    0b1111100110011111, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    # ---------------------------------------
    # mopping levels
    # ---------------------------------------
    0b1111000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000111100000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000011110000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000001111, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000001111, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000011110000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000111100000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b1111000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b1111000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000111100000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000011110000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000001111, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000001111, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000011110000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000111100000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111000000000000, 150,
    #
    0b1000100010001000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0100010001000100, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0010001000100010, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0001000100010001, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0001000100010001, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0010001000100010, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0100010001000100, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b1000100010001000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b1000100010001000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0100010001000100, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0010001000100010, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0001000100010001, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0001000100010001, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0010001000100010, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0100010001000100, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1000100010001000, 150,
    # ---------------------------------------
    # climbing stairs
    # ---------------------------------------
    0b1111000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000111100000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000011110000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000001111, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1000100010001000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0100010001000100, 0b0000000000000000, 150,
    0b0000000000000000, 0b0010001000100010, 0b0000000000000000, 0b0000000000000000, 150,
    0b0001000100010001, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000001111, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000011110000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000111100000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0001000100010001, 150,
    0b0000000000000000, 0b0000000000000000, 0b0010001000100010, 0b0000000000000000, 150,
    0b0000000000000000, 0b0100010001000100, 0b0000000000000000, 0b0000000000000000, 150,
    0b1000100010001000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    # ---------------------------------------
    # More X's
    # ---------------------------------------
    0b1001011001101001, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b1001011001101001, 0b0000000000000000, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b1001011001101001, 0b0000000000000000, 150,
    0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1001011001101001, 150,
    0b1001000000000000, 0b0110000000000000, 0b0110000000000000, 0b1001000000000000, 150,
    0b0001000000000001, 0b0000000100010000, 0b0000000100010000, 0b0001000000000001, 150,
    0b0000000000001001, 0b0000000000000110, 0b0000000000000110, 0b0000000000001001, 150,
    0b1000000000001000, 0b0000100010000000, 0b0000100010000000, 0b1000000000001000, 150,

]

# instantiate ledcube4x4x4
lc = ledcube4x4x4.ledcube(DATA, CLOCK, LATCH, L0, L1, L2, L3, debug=False)

lc.start()

try:
    # loop to display the frames on the LED cube
    currentFrame = 0
    while True:
        # parameters for LED cube frame display
        L0pattern = FRAME[currentFrame]
        L1pattern = FRAME[currentFrame + 1]
        L2pattern = FRAME[currentFrame + 2]
        L3pattern = FRAME[currentFrame + 3]
        delay_ms = FRAME[currentFrame + 4]
        # display frame on LED cube   
        lc.display(L0pattern, L1pattern, L2pattern, L3pattern, delay_ms)
        # move to next frame        
        currentFrame += 5
        if currentFrame >= len(FRAME):
            currentFrame = 0

except KeyboardInterrupt as e:
    print("programma onderbroken met Ctrl-C")
    
finally:
    # stop display
    lc.stop()

import smbus
import mcp23017
import time

BUS = 1

mcp = mcp23017.MCP23017( smbus.SMBus(BUS) )

mcp.write_byte_data( mcp23017.IODIRA, 0x7F )

while 1:
    
    for j in range( 5 ):
        mcp.write_byte_data( mcp23017.GPIOA, 0x00 )
        time.sleep( 0.1 )
        
        mcp.write_byte_data( mcp23017.GPIOA, 0x80 )
        time.sleep( 0.9 )

    mcp.write_byte_data( mcp23017.GPIOA, 0x00 )
    time.sleep( 0.5 )
    
    mcp.write_byte_data( mcp23017.GPIOA, 0x80 )
    time.sleep( 0.5 )

    time.sleep(4)
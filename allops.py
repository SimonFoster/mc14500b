import smbus
import mcp23017
import time

BUS = 1

mcp = mcp23017.MCP23017( smbus.SMBus(BUS) )

mcp.write_byte_data( mcp23017.IODIRB, 0x78 )

while 1:
    for op in range( 16 ):
        
        print( op )
        mcp.write_byte_data( mcp23017.GPIOB, op )
        time.sleep( 0.5 )
        mcp.dump()
        
        mcp.write_byte_data( mcp23017.GPIOB, op + 0x80 )
        time.sleep( 0.5 )
        mcp.dump()

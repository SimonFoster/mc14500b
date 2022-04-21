# Assume BANK = 0 (8-bit mode)

IODIRA      = 0x00
IODIRB      = 0x01
IPOLA       = 0x02
IPOLB       = 0x03
GPINTENA    = 0x04
GPINTENB    = 0x05
DEFVALA     = 0X06
DEFVALB     = 0X07
INTCONA     = 0X08
INTCONB     = 0x09
IOCON       = 0x0A
# IOCON     = 0x0B
GPPUA       = 0x0C
GPPUB       = 0x0D
INTFA       = 0x0E
INTFB       = 0x0F
INTCAPA     = 0x10
INTCAPB     = 0x11
GPIOA       = 0x12
GPIOB       = 0x13
OLATA       = 0x14
OLATB       = 0x15

class MCP23017:

    def __init__( self, bus, address=0x20 ):
        self.bus = bus
        self.address = address

    def write_byte_data( self, address, data ):
        self.bus.write_byte_data( self.address, address, data )

    def read_i2c_block_data( self, address, length ):
        return self.bus.read_i2c_block_data( self.address, address, length )

    def dump( self ):
        print( [ f"{i:02X}" for i in self.bus.read_i2c_block_data( self.address, 0, 32 ) ] )
        pass





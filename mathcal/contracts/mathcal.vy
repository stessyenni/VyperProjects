# @version ^0.3.10

# Contract to perform basic arithmetic operations

# Currency Conversion Functions
owner: public(address)
stored_amount: public(uint256)
exchange_rate: public(uint256)  # Exchange rate (e.g., USD to ETH)
#trigger_event: public(uint256)

# Default precision scaling factor (10**18 for high precision)
SCALING_FACTOR: constant(uint256) = 10**18


@external
@view
def get_amount() -> uint256:
    return self.stored_amount

@external
@pure
def add(a: uint256, b: uint256) -> uint256:
    return a + b

@external
@pure
def subtract(a: uint256, b: uint256) -> uint256:
    return a - b

@external
@pure
def multiply(a: uint256, b: uint256) -> uint256:
    return a * b
    #result: uint256 = (a * b) SCALING_FACTOR 

@external
@pure
def divide(a: uint256, b: uint256) -> uint256:
    assert b != 0, "Division by zero, change to >0"
    
    # Division with scaling factor to maintain decimal precision
    result: uint256 = (a * SCALING_FACTOR) / b
    return a / b


event ConversionResult:
    sender: address
    input_amount: uint256
    output_amount: uint256
    is_reverse: bool

event ExchangeRateUpdated:
    sender: address
    old_rate: uint256
    new_rate: uint256

event Conversion:
    sender: address
    amount_in: uint256
    amount_out: uint256
    is_reverse: bool

# Currency Conversion Functions

@external
def __init__():
    """
    Initialize the contract and set the owner.
    """
    self.owner = msg.sender
    self.exchange_rate = 0  # Default exchange rate is 0
    self.stored_amount = 0

    

@external
def update_exchange_rate(new_rate: uint256):
    """
    Update the exchange rate. Only the owner can call this.
    The rate should be scaled by 10**18 (e.g., 2500.0 becomes 2500 * 10**18).
    """
    assert msg.sender == self.owner, "Only the owner can set the exchange rate"
    assert new_rate > 0, "Exchange rate must be positive"
    # Log the old and new rates for debugging
    log ExchangeRateUpdated(msg.sender, self.exchange_rate, new_rate)
    self.exchange_rate = new_rate

@external
@payable
def convert_currency(amount: uint256, is_reverse: bool) -> uint256:
    """
    Convert a value using the exchange rate.
    - If is_reverse = False, convert from base currency to target currency.
    - If is_reverse = True, convert from target currency to base currency.
    Example: Convert 100 USD to ETH or vice versa.
    """
    assert self.exchange_rate > 0, "Exchange rate is not set"

    # Calculate the conversion
    result: uint256 = 0
    
    if not is_reverse:
        # Convert base to target: (amount * 10**18) / exchange_rate
        result = (amount * 10**18) / self.exchange_rate
    else:
        # Convert target to base: (amount * exchange_rate) / 10**18
        result = (amount * self.exchange_rate) / 10**18

    # Store the result
    self.stored_amount = result

    # Emit the result for visibility in logs
    log Conversion(msg.sender, amount, result, is_reverse)

    return result
   
    
    #Log ConversionResult(
        #input_amount = output_amount,
        #convert_currency = self.stored_amount.is_reverse,
        #output_amount = self.convert_currency.get_amount
   # )
    #self.convert_currency.get_amount = get_amount
    
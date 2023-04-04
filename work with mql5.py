import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
import numpy as np


mt5.initialize()

# print(mt5.last_error())

info = mt5.account_info()

# print(type(info))

print('\t\n\t' , info.name , info.balance, '\t\n\t\n')

# symbol = mt5.symbol_info('US30.s')

# print(symbol.bid, '\t',symbol.description,'\n', symbol.ask, '\n',symbol.bidhigh,'\n', symbol.bidlow)

# book_order = mt5.market_book_get("US30.s")

# print(book_order)

mt5.symbol_select("GBPCHF.s")

# mt5.initialize()

# first_date = datetime(2023, 1, 1)

# seconde_date = datetime(2023, 1, 10)

# ticks = mt5.copy_rates_range('US30.s', mt5.TIMEFRAME_M1, first_date, seconde_date)

# # print(ticks)

# df_ticks = pd.DataFrame(ticks)

# df_ticks['time'] = pd.to_datetime(df_ticks['time'], unit='s')

# print(df_ticks)

def get_ticks(symbol, data):

    date = datetime.now()

    ticks = mt5.copy_ticks_from('US30.s', date, data, mt5.COPY_TICKS_ALL)

    print(ticks)

    df_ticks = pd.DataFrame(ticks)

    df_ticks['time'] = pd.to_datetime(df_ticks['time'], unit='s')

    df_ticks = df_ticks.set_index("time")

    return print(df_ticks)

# get_ticks('US30.s', 50)

def get_rates(symbol, data, timeframe):

    date = datetime.now()

    rates = mt5.copy_rates_from(symbol, timeframe , date, data)

    df_rates = pd.DataFrame(rates)

    df_rates['time'] = pd.to_datetime(df_rates['time'], unit='s')   

    df_rates = df_rates.set_index('time')

    return print(df_rates)

# get_rates('US30.s', 50, mt5.TIMEFRAME_D1)

mt5.shutdown()

mt5.initialize()

lot = 0.01

mt5.symbol_select("EURUSD.s")

symbol = 'US30.s'

deviation = 10

filling_type = mt5.symbol_info(symbol).filling_mode

buy_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": deviation,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC
}

sell_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": mt5.symbol_info_tick(symbol).bid,
    "deviation": deviation,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC
}
############ for check order #############


# buy_order = mt5.order_check(buy_request)

# sell_order = mt5.order_check(sell_request)

# print('Buy_order', '\n', buy_order,'\n','sell_order', '\n',sell_order)

######## for  send order ###########

# buy_order = mt5.order_send(buy_request)

# sell_order = mt5.order_send(sell_request)

# print('Buy_order', '\n', buy_order,'\n','sell_order', '\n',sell_order)

close_sell_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    ########## position code #########
    "position":50067384583,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": deviation,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC
}

close_buy_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    ########## position code #########
    "position":50067383081,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": mt5.symbol_info_tick(symbol).bid,
    "deviation": deviation,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC
}

############# close orders with enter position code of order ###############

# close_sell_order = mt5.order_send(close_sell_request)

# close_buy_order = mt5.order_send(close_buy_request)

# print('close_Buy_order', '\n\t', close_buy_order,'\n\t','close_sell_order', '\n', close_sell_order)


#### define a function for trade or close trade so if we want to close a trade we should have position code so :::: ##################

def send_order(symbol, lot, buy, sell, id_position=None, comment=" No specific comment", magic=0):
    
    # Initialize the bound between MT5 and Python
    mt5.initialize()
    
    # Extract filling_mode
    filling_type = mt5.symbol_info(symbol).filling_mode
    
    
    """ OPEN A TRADE """
    if buy and id_position==None:
        request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": filling_type,
        "type_time": mt5.ORDER_TIME_GTC}
        
        result = mt5.order_send(request)
        return result
        
    if sell and id_position==None:
        request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": filling_type,
        "type_time": mt5.ORDER_TIME_GTC}
        
        result = mt5.order_send(request)
        return result
    
    
    """ CLOSE A TRADE """
    if buy and id_position!=None:
        request = {
        "position": id_position,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": filling_type,
        "type_time": mt5.ORDER_TIME_GTC}
        
        result = mt5.order_send(request)
        return result
        
    if sell and id_position!=None:
        request = {
        "position": id_position,
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_filling": filling_type,
        "type_time": mt5.ORDER_TIME_GTC}
        
        result = mt5.order_send(request)
        return result

#### we open order #############

# information = send_order("EURUSD.s", 0.01, True, False)

# print(information)

### close last order (order that open on line 244) ##########

# close_order = send_order("EURUSD.s", 0.01, True, False, id_position=information.order)

# print('\t\n\n', close_order)


# Place a BUY order with take profit
# Initialization value
lot = 0.01
symbol = "US30.s"

# Extract symbol point
point = mt5.symbol_info(symbol).point

# Choose the deviation
deviation = 10

# Find the filling mode of symbol
filling_type = mt5.symbol_info(symbol).filling_mode

# Create dictionnary request
buy_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": deviation,
    "tp": mt5.symbol_info_tick(symbol).ask + 100 * point,
    "sl": mt5.symbol_info_tick(symbol).ask - 100 * point, 
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC,
}
Sell_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": deviation,
    "tp": mt5.symbol_info_tick(symbol).ask + 100 * point,
    "sl": mt5.symbol_info_tick(symbol).ask - 100 * point, 
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC,
}

#### for buy #######

# check = mt5.order_check(buy_request)
# check_comment = check.comment
# print(check)
# print(check_comment)

#### for sell #######

# check = mt5.order_check(Sell_request)
# check_comment = check.comment
# print(check)
# print(check_comment)


###############  Find stop loss and take profit level for a specific risk percentage #############

def risk_reward_threshold(symbol, buy=True, risk=0.01, reward=0.02):
    
    # Extract the leverage
    leverage = mt5.account_info().leverage

    balance = mt5.account_info().balance

    # Compute the price
    price = mt5.symbol_info(symbol).ask

    # Extract the number of decimals
    nb_decimal = str(price)[::-1].find(".")


    # Compute the variations in percentage
    var_down = risk/leverage
    var_up = reward/leverage


    # Find the TP and SL threshold in absolute price
    if buy:
        price = mt5.symbol_info(symbol).ask

        # Compute the variations in absolute price
        price_var_down = var_down*price
        price_var_up = var_up * price

        tp = np.round(price + price_var_up, nb_decimal)
        sl = np.round(price - price_var_down, nb_decimal)

    else:

        price = mt5.symbol_info(symbol).bid

        # Compute the variations in absolute price
        price_var_down = var_down*price
        price_var_up = var_up * price

        tp = np.round(price - price_var_up, nb_decimal)
        sl = np.round(price + price_var_down, nb_decimal)


    print(f'your account leverage {leverage}\t and your balance {balance}\t so we have this result for {symbol} :\n\t')    
    print(f"\tPRICE: {price} \t Take Profit: {tp} \t Stop Loss: {sl}\n\n")
    pass

# risk_reward_threshold('US30.s', True, 0.01, 0.02)





#### Find the volume depending of your capital####

def position_size(capital, symbol):
    mt5.initialize()
    print(f"INVESTED CAPITAL: {capital}")
    
    leverage = mt5.account_info().leverage
    print(f"LEVERAGE: {leverage}")
    
    invested_capital = capital  * leverage
    print(f"INVESTED CAPITAL LEVERAGED: {invested_capital}")
    
    trade_size = mt5.symbol_info(symbol).trade_contract_size
    print(f"TRADE SIZE: {trade_size}")
    
    price = (mt5.symbol_info(symbol).ask + mt5.symbol_info(symbol).bid)/2
    print(f"PRICE: {price}")

    lot_size = invested_capital / trade_size / price
    print(f"LOT SIZE: {lot_size}")
    
    min_lot = mt5.symbol_info(symbol).volume_min
    print(f"MIN LOT: {min_lot}")
    
    max_lot = mt5.symbol_info(symbol).volume_max
    print(f"MAX LOT: {max_lot}")


    if min_lot<lot_size:
        number_decimal = str(min_lot)[::-1].find(".")
        print(f"NUMBER DECIMAL: {number_decimal}")

        if number_decimal>0:
            lot_size_rounded = np.round(lot_size, number_decimal)
            print(f"LOT SIZE ROUNDED: {lot_size_rounded}")

            if lot_size < lot_size_rounded:
                lot_size_rounded = np.round(lot_size_rounded - min_lot, number_decimal)
                print(f"LOT DOWN ROUNDED: {lot_size_rounded}")

        else:
            number_size_lot =  len(str(min_lot))

            lot_size_rounded = int(np.round(lot_size, -number_size_lot))

            if lot_size < lot_size_rounded:
                lot_size_rounded = int(np.round(lot_size_rounded - number_size_lot, - number_size_lot))
                
        if lot_size_rounded>max_lot:
            lot_size_rounded = max_lot
            
        print(f"GOOD SIZE LOT: {lot_size_rounded}")
        return lot_size_rounded
    else: 
        print("Invested capital is too small to be able to place an order")
        
    pass
    
# position_size(25,'US30.s')    


########## we want to use sell limite or buy limit #######

### we just chaneg our requset ######

mt5.initialize()

symbol = 'US30.s'

filling_type  = mt5.symbol_info(symbol).filling_mode

point = mt5.symbol_info(symbol).point

####    Sell limit #####
request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": 1.0,
    "type": mt5.ORDER_TYPE_BUY_LIMIT,
    "price": mt5.symbol_info_tick(symbol).bid-100*point,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC,
}

# order = mt5.order_check(request)

# print(order,'\n\t')

# order = mt5.order_send(request)

# print(order,'\n\t')

# REMOVE PENDING ORDER ####

# request = {
    #  "action" : mt5.TRADE_ACTION_REMOVE ,
    #  "order" : order.order ,
# }

# mt5.order_send(request)


#### Buy limit #####

###
# we just change sell request to buy request
###

#### change SL\TP 1. we open a deal  -- 2. change sl or tp ######
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 0.01,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": deviation,
    "sl": mt5.symbol_info_tick(symbol).ask-100*point,
    "tp": mt5.symbol_info_tick(symbol).ask+100*point,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC,
}

info_order = mt5.order_send(request)

# print(info_order,'\n')

### change our sl or tp ####
request = {
    "action": mt5.TRADE_ACTION_SLTP,
    "symbol": symbol,
    "position": 5138403,
    "volume": 0.1,
    "type": mt5.ORDER_TYPE_SELL,
    "price": 1.10508,
    "deviation": 10,
    "sl": mt5.symbol_info_tick(symbol).ask+1000*point,
    "tp": mt5.symbol_info_tick(symbol).ask-1000*point,
    "type_filling": filling_type,
    "type_time": mt5.ORDER_TIME_GTC,
}

order = mt5.order_send(request)

# print(order,'\n')

### advance mony managment and make table with or trade ######
def resume():
    """ Return the current positions. Position=0 --> Buy """    
    # Define the name of the columns that we will create
    columns = ["ticket", "position", "symbol", "volume", "magic", "profit", "price", "tp", "sl","trade_size"]

    # Go take the current open trades
    list_current = mt5.positions_get()

    # Create a empty dataframe
    summary = pd.DataFrame()

    # Loop to add each row in dataframe
    for element in list_current:
        element_pandas = pd.DataFrame([element.ticket, element.type, element.symbol, element.volume, element.magic,
                                       element.profit, element.price_open, element.tp,
                                       element.sl, mt5.symbol_info(element.symbol).trade_contract_size],
                                      index=columns).transpose()
        summary = pd.concat((summary, element_pandas), axis=0)
    
    try:
        summary["profit %"] = summary.profit / (summary.price * summary.trade_size * summary.volume)
        summary = summary.reset_index(drop=True)
    except:
        pass
    return print(summary)

# resume()

# position_size(20,'US30.s')


send_order(buy=True,sell=False, symbol='US30.s', lot=0.01, )
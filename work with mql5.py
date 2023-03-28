import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

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

#### we open order

information = send_order("EURUSD.s", 0.01, True, False)

print(information)

### close last order (order that open on line 244) ##########

close_order = send_order("EURUSD.s", 0.01, True, False, id_position=information.order)

print('\t\n\n', close_order)

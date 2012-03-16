#!/usr/bin/env python

import json
import pprint
import urllib2
import prettytable 
import time 
def get_stock_quote(ticker_symbol):   
    url = 'http://finance.google.com/finance/info?q=%s' % ticker_symbol
    #lines = urllib2.urlopen(url).read().splitlines()
    u = urllib2.urlopen(url)
    content = u.read()
    obj = json.loads(content[3:])
    return obj
#   return json.loads(''.join([x for x in lines if x not in ('// [', ']')]))


# u'c': u'+1.28',
# u'ccol': u'chg',
# u'cp': u'0.65',
# u'e': u'NYSE',
# u'id': u'18241',
# u'l': u'198.81',
# u'l_cur': u'198.81',
# u'lt': u'Mar 2, 4:03PM EST',
# u'ltt': u'4:03PM EST',
# u's': u'0',
# u't': u'IBM'}

import sys, signal, curses, traceback
def signal_handler(signal, frame):
    print "you pressed ctr+c!"
    curses.endwin()
    sys.exit(0)
    
stdscr = curses.initscr()
height, width = stdscr.getmaxyx()
signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    try:
        filename = "stocksymbol"
        FILE = open (filename, 'r')
        tickarrp = [] 
        tickarr = []
        i = 0 
        for line in FILE:
    	    tickarr.append(line.upper().rstrip("\n"))
            i = i + 1 # why can't use ++i  
            if i % 5 == 0:
               i = 0
               tickerstr = ','.join(tickarr)
               stdscr.addstr(height-1, 0, tickerstr); stdscr.refresh(); stdscr.deleteln()
               tickarrp.append(tickerstr) 
               tickarr = [] 
        if i != 0: 
            tickerstr = ','.join(tickarr)
            tickarrp.append(tickerstr)
            stdscr.addstr(height-1, 0, tickerstr); stdscr.refresh(); stdscr.deleteln()
            tickarr = [] 
        while(1):
          stdscr.addstr(height-1, 0, "####################################################"); stdscr.refresh(); stdscr.deleteln()
          table = [["symbol" , "abs chg", "%", "price", "time"]]
          for tickerstr in tickarrp:
              stdscr.addstr(height-1, 0, tickerstr); stdscr.refresh(); stdscr.deleteln()
              quotes = get_stock_quote(tickerstr)
    	      for obj in quotes: 
                data = [] 
                data.append(obj['t']) 
                data.append(obj['c'])
                data.append(obj['cp'])
                data.append(obj['l_cur'])
                data.append(obj['lt'])
                table.append(data)
          
          stdscr.erase()
          #stdscr.addstr(0, 0, pprint.pformat(table, indent=4))
          stdscr.addstr(0, 0, prettytable.pprint_table_str(table))
          stdscr.refresh()
          time.sleep(10)
    except:
        # In event of error, restore terminal to sane state.
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()
        print "shit got ended :)"
             

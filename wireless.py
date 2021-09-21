'''
 * This module is useful to connect to a Wi-Fi Network in a fast and secure way.
 *
 * Name    = wireless
 * Version = 1.0.0
 * Author  = Jhonatan Lamiña
 * e-mail  = contacto@jhonatanlamina.com
 * Url     = www.jhonatanlamina.com
 *
 *
 * To use this module you must include the following in your file
 *
 * import wireless
 * wireless.wifi('SSID', 'PASSWORD', PinOut)
 *
 * SSID     = Wi-Fi Network Name (string)
 * PASSWORD = Wi-Fi Network Password (string)
 * PinOut   = Output pin that indicates the status of the connection,
 *            it can be omitted if not required. (int)
 *
 *
 * Copyright (c) Jhonatan Lamiña - All rights reserved
'''

import network
from machine import Pin
import time

class wifi():
    def __init__(self, ssid='None', password='None', output = 'None'):
        self.ssid = ssid
        self.password = password
        self.output = output
        
        if output != 'None':
            indicator = Pin(output, Pin.OUT)
            
        wlan = network.WLAN(network.STA_IF)
        if not wlan.isconnected():
            wlan.active(True)
            wlan.connect(ssid, password)
            print('Connecting to:', ssid)
            timeout = time.ticks_ms()
            while not wlan.isconnected():
                if output != 'None':
                    indicator.on()
                    time.sleep(0.15)
                    indicator.off()
                    time.sleep(0.15)
                if (time.ticks_diff (time.ticks_ms(), timeout) > 10000):
                 break
            if wlan.isconnected():
                if output != 'None':
                    indicator.on()
                print('Successful connection to: %s' % ssid)
                print(str(wlan.ifconfig()))
            else:
                if output != 'None':
                    indicator.off()
                wlan.active(False)
                print('Failed to connect to: %s' % ssid)
        else:
            if output != 'None':
                indicator.on()
            print('Connected')
            print(str(wlan.ifconfig()))
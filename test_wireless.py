#Import wireless module
import wireless

#To make the connection, you must replace the following data with your WiFi network:
#SSID     = Wi-Fi Network Name (string)
#PASSWORD = Wi-Fi Network Password (string)
#PinOut   = Output pin that indicates the status of the connection, it can be omitted if not required. (int)
wireless.wifi('SSID', 'PASSWORD', PinOut)
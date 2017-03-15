import logging
import logging.handlers
import os.path
import configparser


"""
This module writing config in 5 files. Logging, loglevel and size of file change in config file
"""
if os.path.exists('/home/pi/new_interface/log_settings.default.cfg') == False:
    config = configparser.ConfigParser()
    config['Logging'] = {}
    config['Logging']['logging'] = 'yes'
    config['Loglevel'] = {}
    config['Loglevel']['loglevel'] = 'WARNING'
    config['Filesize'] = {}
    config['Filesize']['filesize'] = '200'
    config['Logfilename'] = {}
    config['Logfilename']['filename'] = 'dev_log.log'
    config['Backupcount'] = {}
    config['Backupcount']['count'] = '5'
    with open('log_settings.default.cfg', 'w') as defaultconfigfile:
        config.write(defaultconfigfile)

config = configparser.ConfigParser()
try:
    if os.path.exists('/mnt/switchinterface/alo'):
        config.read('log_settings.cfg')
        log_check = config['Logging']['logging']
        log_level = config['Loglevel']['loglevel']
        log_filesize = int(config['Filesize']['filesize'])
        log_filename = config['Logfilename']['filename']
        log_count = int(config['Backupcount']['count'])
    else:
        config.read('log_settings.default.cfg')
        log_check = config['Logging']['logging']
        log_level = config['Loglevel']['loglevel']
        log_filesize = int(config['Filesize']['filesize'])
        log_filename = config['Logfilename']['filename']
        log_count = int(config['Backupcount']['count'])
except Exception as ex:
    print(ex)

    # Set up a specific logger with our desired output level

my_logger = logging.getLogger(__name__)
LEVELS = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}
LEVEL = LEVELS[log_level]
my_logger.setLevel(LEVEL)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=log_filesize, backupCount=log_count)
handler.setFormatter(formatter)
my_logger.addHandler(handler)

def interfaceLog(levelofLog, message):
    lvlmes = LEVELS[levelofLog]
    my_logger.log(lvlmes, message)
        
if __name__ == "__main__":
    # if module starting as a separate programme
    print('Test function interfaceLog')
    print('Settings in log_settings.cfg')
    print("If log_settings isn't exist, all settings change to default and writing in log_interface.default.cfg")
    interfaceLog('WARNING', 'test message ')
    for i in range(20):
        print(i)
        interfaceLog('WARNING', 'test message ' + str(i))
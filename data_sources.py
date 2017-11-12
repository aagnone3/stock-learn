import os
import urllib
import logging
import pandas as pd

logger = logging.getLogger("stock_learn")
RES_DIR = os.path.join(os.getcwd(), "res")
SYMBOLS_DIR = os.path.join(RES_DIR, "symbols")


def get_api_keys():
    api_keys = {}
    with open('.keys') as fp:
        for line in fp:
            key, val = line.strip('\n').split('=')
            api_keys[key] = val
    return api_keys


def updated_nasdaq_symbols():
    """
    Retrieve updated NASDAQ symbols from the FTP
    :return: pandas Series of updated NASDAQ symbols
    """
    # TODO logic to determine if new query is needed or not
    fn = os.path.join(SYMBOLS_DIR, "nasdaq.csv")
    if os.path.exists(fn):
        logger.info("NASDAQ symbols found in a local file, not querying to update.")
    else:
        urllib.urlretrieve("ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt", fn)
    df = pd.read_csv(fn, sep='|')
    return df[["Symbol", "Security Name"]]

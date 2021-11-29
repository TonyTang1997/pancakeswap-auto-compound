# pancakeswap-auto-compound

## Description:

This code is used to auto compound CAKE tokens earned from the CAKE/BNB farm on pancakeswap. The bot will be doing below actions continuously 

- harvesting CAKE
- selling half of the CAKE into BNB
- getting new CAKE-BNB tokens by CAKE and BNB tokens above
- re-investing all CAKE-BNB LPs into the yield farm

## Steps to run the bot:

Make sure you have python version > 3.5

- Clone this repo
```
git clone https://github.com/TonyTang1997/pancakeswap-auto-compound
```

- Install required libraries 
```
cd pancakeswap-auto-compound
pip3 install requirements.txt
```

- Running the script 
```
python3 main.py --privateAddress {your address} --privateKey {your private key} --inital 1000 --length 365
```

- Parameters instructions 

| Parameter     | Type           | Usage  |
| ------------- |:--------------:| ------:|
| --privateAddress | str | your wallet address |
| --privateKey| str | your private key |
| --inital | float | amount of current investment (in unit of bnb) |
| --length | int | lenght of time period holding this investment (in days) since now, i.e. 365 = holding for 1 year|
| --approve | boolean | approve the pool to make transcation, set to True if you have not approved the CAKE/BNB farm on pancakeswap |


## Algorithm 

There are few assumptions made for the algorithm to determine whether to harvest and reinvest or not 

- the transaction cost of every transcation is estimated by the average gas used of the last block's transcations
- the transcation cost of four different actions are the same
- the apy of CAKE/BNB farm is calculated based on the latest block's reward, assuming there are 20 blocks per minute
- the actions are taken only after a new block is just finished

To generate most return from the auto compounding yield farming, we need to maximize the following objective function  

```
def objective(x, length):
    nInterval = ((20 * 60 * 24 * length) / x)
    return initalCap * (1 + farmAPY / nInterval) ** nInterval - latestCost * nInterval
```

where x is the interval for reinvesting 

Because there are only one variable to optimize, the current implementation is to find the optimal interval for reinvesting by brute force.

With the optimal interval, we can calculate the minium amount of pending CAKE reward to harvest and only reinvest when our pedning CAKE reward is larger than this number.

## Note 

- The apy calculated is much less than the apy listed on pancakeswap, two possible reasons:

1. The apy estimation based on latest's reward is incorrect.
2. The pancakeswap displayed apy is based on the average of a longer time period, but not the latest one only.





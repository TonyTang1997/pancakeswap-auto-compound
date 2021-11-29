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
python main.py --privateAddress {your address} --privateKey {your private key} --inital 1000 --length 365
```

- Parameters instructions 


| Parameter     | Type           | Usage  |
| ------------- |:--------------:| ------:|
| --privateAddress | str | your wallet address |
| --privateKey| str | your private key |
| --inital | float | amount of current investment |
| --length | int | lenght of time period holding this investment (in days) since now, i.e. 365 = holding for 1 year|
| --approve | boolean | approve the pool to make transcation, set to True if you have not approved the CAKE/BNB farm on pancakeswap |










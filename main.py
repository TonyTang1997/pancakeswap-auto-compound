from web3 import Web3
from web3.middleware import geth_poa_middleware
import time
import argparse

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# masterchef router
masterChefAddress = '0x73feaa1eE314F8c655E354234017bE2193C9E24E'
masterChefABI = '[{"inputs":[{"internalType":"contract CakeToken","name":"_cake","type":"address"},{"internalType":"contract SyrupBar","name":"_syrup","type":"address"},{"internalType":"address","name":"_devaddr","type":"address"},{"internalType":"uint256","name":"_cakePerBlock","type":"uint256"},{"internalType":"uint256","name":"_startBlock","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IBEP20","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cake","outputs":[{"internalType":"contract CakeToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cakePerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_devaddr","type":"address"}],"name":"dev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"enterStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"leaveStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"contract IMigratorChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingCake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IBEP20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accCakePerShare","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigratorChef","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"syrup","outputs":[{"internalType":"contract SyrupBar","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"multiplierNumber","type":"uint256"}],"name":"updateMultiplier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

# pancakeswap router
panAddress = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
panABI = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

# cake router
cakeAddress = web3.toChecksumAddress('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')
cakeABI = '[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"},{"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "balance","type": "uint256"}],"payable": false,"type": "function"},{"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}]'

cakeBnbAddress = web3.toChecksumAddress("0xa527a61703d82139f8a06bc30097cc9caa2df5a6")
cakeBnbABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]'

bnbAddress = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")

cakeBnbPid = 251

masterChefContract = web3.eth.contract(address=masterChefAddress, abi=masterChefABI)
panContract = web3.eth.contract(address=panAddress, abi=panABI)
cakeContract = web3.eth.contract(address=cakeAddress, abi=cakeABI)
cakeBnbLPContract = web3.eth.contract(address=cakeBnbAddress, abi=cakeBnbABI)


def approveLPToken(address, key, gas_price):
    """approve the cake-bnb LP token"""

    totalSupply = cakeBnbLPContract.functions.totalSupply().call()

    start = time.time()
    approve = cakeBnbLPContract.functions.approve(panAddress, totalSupply).buildTransaction({
        'from': address,
        'gasPrice': web3.toWei(gas_price, 'gwei'),
        'nonce': web3.eth.get_transaction_count(address),
    })

    signed_txn = web3.eth.account.sign_transaction(approve, private_key=key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Approved: " + web3.toHex(tx_token))


def harvest(address, key, gas_price):
    """harvest the pending cake reward"""

    try:
        txn = masterChefContract.functions.deposit(
            cakeBnbPid,
            0
        ).buildTransaction({
            'from': address,
            'value': web3.toWei(0, 'ether'),
            'gasPrice': web3.toWei(gas_price, 'gwei'),
            'nonce': nonce,
        })
        singed_txn = web3.eth.account.signTransaction(txn, key)
        txtoken = web3.eth.send_raw_transaction(singed_txn.rawTransaction)
        new_Tx = web3.toHex(txtoken)
        print("harvest done: " + new_Tx)
        return True, new_Tx

    except Exception as e:
        print(str(e))
        return False, ""


def swapCakeBnb(address, key, gas_price):
    """swap half of the current cake balance to bnb"""

    cakeBalance = cakeContract.functions.balanceOf(address).call()

    try:
        txn = panContract.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(
            int(cakeBalance / 2),
            0,
            [cakeAddress, bnbAddress],
            address,
            (int(time.time()) + 10000)
        ).buildTransaction({
            'from': address,
            'gas': 250000,
            'gasPrice': web3.toWei(str(gas_price), 'gwei'),
            'nonce': nonce
        })

        singed_txn = web3.eth.account.signTransaction(txn, key)
        txtoken = web3.eth.send_raw_transaction(singed_txn.rawTransaction)
        new_Tx = web3.toHex(txtoken)
        print("swap from cake to bnb done: " + new_Tx)
        return True, new_Tx

    except Exception as e:
        print(str(e))
        return False, ""


def createCakeBnbLP(address, key, gas_price):
    """create cake-bnb LP Token with current cake and bnb balance"""

    try:
        cakeBalance = cakeContract.functions.balanceOf(address).call()
        cakeBalance = web3.fromWei(cakeBalance, 'ether')

        bnbBalance = web3.eth.get_balance(address)
        bnbBalance = float(web3.fromWei(bnbBalance, 'ether')) - 0.001  # reserve some bnb for gas fee

        amountCakeDesired = web3.toWei(str(cakeBalance), 'ether')
        amountBnbDesired = web3.toWei(str(bnbBalance), 'ether')

        deadline = int(time.time()) + 10000

        addLiquidity = panContract.functions.addLiquidity(
            cakeAddress, bnbAddress, amountCakeDesired, amountBnbDesired,
            amountCakeDesired, amountBnbDesired, address, deadline
        ).buildTransaction({
            'from': address,
            'gas': 250000,
            'gasPrice': web3.toWei(str(gas_price), 'gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(addLiquidity, private_key=key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        new_Tx = web3.toHex(tx_token)

        print("cake-bnb LP created: " + new_Tx)
        return True, new_Tx

    except Exception as e:
        print(str(e))
        return False, ""


def depositCakeBnbLP(address, key, gas_price):
    """reinvesting the current cake-bnb LP token into farm"""

    cakeBnbLPBalance = cakeBnbLPContract.functions.balanceOf(address).call()

    try:
        txn = masterChefContract.functions.deposit(
            cakeBnbPid,
            cakeBnbLPBalance
        ).buildTransaction({
            'from': address,
            'gas': 250000,
            'gasPrice': web3.toWei(gas_price, 'gwei'),
            'nonce': nonce,
        })
        singed_txn = web3.eth.account.signTransaction(txn, key)
        txtoken = web3.eth.send_raw_transaction(singed_txn.rawTransaction)
        new_Tx = web3.toHex(txtoken)
        print("cake-bnb LP deposited: " + new_Tx)
        return True, new_Tx

    except Exception as e:
        print(str(e))
        return False, ""


def getLatestGas():
    """get the average transcation cost from the last block"""

    latest = web3.eth.get_block('latest', full_transactions=True)
    costList = [transaction['gas'] * float(web3.fromWei(transaction['gasPrice'], 'ether')) for transaction in
                latest['transactions']]
    return sum(costList) / len(costList)


def calcPrice(tokenAddress):
    """calculate the current exchange rate of cake -> bnb"""

    oneToken = web3.toWei(1, 'Ether')
    price = panContract.functions.getAmountsOut(oneToken, [tokenAddress, bnbAddress]).call()
    normalizedPrice = web3.fromWei(price[1], 'Ether')
    return normalizedPrice


def getFarmAPY():
    """calculate the apy of cake-bnb farm from the lastest block's reward"""

    poolInfo = masterChefContract.functions.poolInfo(cakeBnbPid).call()
    allocPoint = poolInfo[1]

    cakePerBlock = masterChefContract.functions.cakePerBlock().call()
    totalAllocPoint = masterChefContract.functions.totalAllocPoint().call()

    blockReward = cakePerBlock * allocPoint / totalAllocPoint
    numberOfBlocks = 20 * 60 * 24 * 365

    annualBlockReward = blockReward * numberOfBlocks * 1000000000000

    lpSupply = cakeContract.functions.balanceOf(masterChefAddress).call()

    apy = annualBlockReward / lpSupply / 100000000 / 100

    return apy / 100


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='auto compounding yield farming')
    parser.add_argument('--privateAddress', help="address")
    parser.add_argument('--privateKey', help="private key")
    parser.add_argument('--inital', help="inital amount of investment")
    parser.add_argument('--length', help="length of investment ( in days )")
    parser.add_argument('--approveToken', help="to approve LP token or not", default=False)

    args = parser.parse_args()

    privateAddress = args.privateAddress
    privateKey = args.privateKey
    initalCap = int(args.inital)
    length = int(args.length)

    nonce = web3.eth.get_transaction_count(privateAddress)

    if args.approveToken:
        approveLPToken(privateAddress, privateKey, 5)

    harvest_ = False
    swapCakeBnb_ = False
    createCakeBnbLP_ = False
    depositCakeBnbLP_ = False

    while True:
        pendingCake = masterChefContract.functions.pendingCake(cakeBnbPid, privateAddress).call()
        pendingCake = web3.fromWei(pendingCake, 'ether')
        cakePrice = calcPrice(cakeAddress)
        pendingReward = pendingCake * cakePrice

        latestCost = getLatestGas() * 4
        farmAPY = getFarmAPY()

        def objective(x, length):
            nInterval = ((20 * 60 * 24 * length) / x)
            return initalCap * (1 + farmAPY / nInterval) ** nInterval - latestCost * nInterval

        rewards = [objective(i, length) for i in range(1, length * 24 * 60 * 20)]
        intervals = list(range(1, length * 24 * 60 * 20))

        rewardsDict = dict(zip(intervals, rewards))
        sortedRewards = sorted(rewardsDict.items(), key=lambda x: x[1])

        optIntervals, optRewards = list(sortedRewards)[-1][0], list(sortedRewards)[-1][1] / initalCap
        optCompounds = 20 * 60 * 24 * length / optIntervals
        optTargetCake = initalCap * farmAPY / optCompounds

        print(f"expected apy of the cake-bnb farm: {1 + farmAPY}")
        print(f"expected apy of auto compounding the cake-bnb farm: {optRewards}")
        print(f"expected extra reward with auto compounding: {optRewards - 1 - farmAPY}")

        if pendingCake >= optTargetCake:
            harvest_ = True

        else:
            print(f"pending cake {pendingCake} is less than target cake {optTargetCake}, not harvesting")

        if harvest_:
            result, Tx = harvest(privateAddress, privateKey, 5)
            if result:
                harvest_ = False
                swapCakeBnb_ = True
            else:
                print("harvesting failed, retrying next loop")

        if swapCakeBnb_:
            result, Tx = swapCakeBnb(privateAddress, privateKey, 5)
            if result:
                swapCakeBnb_ = False
                createCakeBnbLP_ = True
            else:
                print("swapping cake-bnb failed, retrying next loop")

        if createCakeBnbLP_:
            result, Tx = createCakeBnbLP(privateAddress, privateKey, 5)
            if result:
                createCakeBnbLP_ = False
                depositCakeBnbLP_ = True
            else:
                print("creating cake-bnb LP token failed, retrying next loop")

        if depositCakeBnbLP_:
            result, Tx = depositCakeBnbLP(privateAddress, privateKey, 5)
            if result:
                depositCakeBnbLP_ = False
            else:
                print("depositing cake-bnb LP token failed, retrying next loop")

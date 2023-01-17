from django.shortcuts import render, HttpResponseRedirect
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wallet, CryptoWallet, InvestmentPrice
from . forms import PurchaseForm

# Create your views here.
response = requests.get(
    'https://api.coinlore.net/api/tickers/?start=0&limit=100')
coin_json = response.json()['data']
all_coins = []
coins_nameid = []


for item in coin_json:
    all_coins.append(item)


for item in all_coins:
    coins_nameid.append(item['nameid'])


def home(request):
    response = requests.get(
        'https://api.coinlore.net/api/tickers/?start=0&limit=100')
    coin_json = response.json()['data']
    all_coins = []
    list_item = []
    for item in coin_json:
        all_coins.append(item)
    coin_name = []
    all_coin_name = []
    money = 0
    for x in range(10):
        coin_name.append(coin_json[x]['name'])

    for item in all_coins:
        all_coin_name.append(item['name'])

    query = Wallet.objects.all()
    for item in query:
        list_item.append(item)

    for item in list_item:
        if str(item) == request.user.username:
            if item.money == None:
                money = 0
            else:
                money = item.money
                money = round(money, 2)
                money = "{:,}".format(money)

    context = {
        'crypto': coin_name,
        'all_coin': all_coin_name,
        'money': money
    }
    return render(request, 'index.html', context)


def coin(request, code):
    response = requests.get(
        'https://api.coinlore.net/api/tickers/?start=0&limit=100')
    coin_json = response.json()['data']
    all_coins = []
    for item in coin_json:
        all_coins.append(item)

    for item in coin_json:
        if item['name'] == code:
            symbol = item['symbol']
            price = float(item['price_usd'])
            price = "{:,}".format(price)
            price = price.replace(',', '.')
            break

    context = {
        'code': code,
        'symbol': symbol,
        'price': price,
    }
    return render(request, 'coin.html', context)


@login_required
def profile(request):
    response = requests.get(
        'https://api.coinlore.net/api/tickers/?start=0&limit=100')
    coin_json = response.json()['data']
    all_coins = []
    money = 0
    for item in coin_json:
        all_coins.append(item)
    list_item = []
    query = Wallet.objects.all()
    for item in query:
        list_item.append(item)

    for item in list_item:
        if str(item) == request.user.username:
            if item.money == None:
                money = 0
            else:
                money = item.money
                money = round(money, 2)
                money = "{:,}".format(money)

    investment_list = []
    price_list = []
    wallet_list = []
    coins_list = []
    return_list = []
    query = CryptoWallet.objects.all()
    for item in query:
        wallet_list.append(item)

    for item in wallet_list:
        if str(item) == request.user.username:
            if item.bitcoin > 0:
                investment_list.append('Bitcoin')
                coins_list.append(round(item.bitcoin, 3))
            if item.ethereum > 0:
                investment_list.append('Ethereum')
                coins_list.append(round(item.ethereum, 3))
            if item.tether > 0:
                investment_list.append('Tether')
                coins_list.append(round(item.tether, 3))
            if item.usdcoin > 0:
                investment_list.append('USD Coin')
                coins_list.append(round(item.usdcoin, 3))
            if item.binancecoin > 0:
                investment_list.append('Binance Coin')
                coins_list.append(round(item.binancecoin, 3))
            if item.binanceusd > 0:
                investment_list.append('Binance USD')
                coins_list.append(round(item.binanceusd, 3))
            if item.ripple > 0:
                investment_list.append('XRP')
                coins_list.append(round(item.ripple, 3))
            if item.cardano > 0:
                investment_list.append('Cardano')
                coins_list.append(round(item.cardano, 3))
            if item.dogecoin > 0:
                investment_list.append('Dogecoin')
                coins_list.append(round(item.dogecoin, 3))
            if item.solana > 0:
                investment_list.append('Solana')
                coins_list.append(round(item.solana, 3))

    query = InvestmentPrice.objects.all()
    for item in query:
        price_list.append(item)
    for item in price_list:
        if str(item) == request.user.username:
            if item.bitcoin > 0:
                return_percentage = (
                    item.bitcoin - float(all_coins[0]['price_usd']))/float(all_coins[0]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.ethereum > 0:
                return_percentage = (
                    item.ethereum - float(all_coins[1]['price_usd']))/float(all_coins[1]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.tether > 0:
                return_percentage = (
                    item.tether - float(all_coins[2]['price_usd']))/float(all_coins[2]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.usdcoin > 0:
                return_percentage = (
                    item.usdcoin - float(all_coins[3]['price_usd']))/float(all_coins[3]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.binancecoin > 0:
                return_percentage = (
                    item.binancecoin - float(all_coins[4]['price_usd']))/float(all_coins[4]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.binanceusd > 0:
                return_percentage = (
                    item.binanceusd - float(all_coins[5]['price_usd']))/float(all_coins[5]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.ripple > 0:
                return_percentage = (
                    item.ripple - float(all_coins[6]['price_usd']))/float(all_coins[6]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.cardano > 0:
                return_percentage = (
                    item.cardano - float(all_coins[7]['price_usd']))/float(all_coins[7]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.dogecoin > 0:
                return_percentage = (
                    item.dogecoin - float(all_coins[8]['price_usd']))/float(all_coins[8]['price_usd'])*100
                return_list.append(round(return_percentage, 2))
            if item.solana > 0:
                return_percentage = (
                    item.solana - float(all_coins[9]['price_usd']))/float(all_coins[9]['price_usd'])*100
                return_list.append(round(return_percentage, 2))


# python manage.py runserver

    context = {
        'username': request.user.username,
        'money': money,
        'investment_list': investment_list,
        'investment_amount': coins_list,
        'return_list': return_list
    }

    return render(request, 'profile.html', context)


@login_required
def purchase(request):
    response = requests.get(
        'https://api.coinlore.net/api/tickers/?start=0&limit=100')
    coin_json = response.json()['data']
    all_coins = []
    for item in coin_json:
        all_coins.append(item)

    form = PurchaseForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        query = Wallet.objects.all()
        list_user_wallet = []
        for item in query:
            list_user_wallet.append(item)
        for item in list_user_wallet:
            if str(item) == request.user.username:
                if item.money == None:
                    money = 0
                else:
                    money = item.money

                # money = money.replace('.', ',')

        if int(amount) > float(money) or int(amount) == 0:
            context = {
                'form': form,
                'message': 'Gak Cukup Uangnya Bang'}
            return render(request, 'purchase.html', context)
        else:
            for item in list_user_wallet:
                if str(item) == request.user.username:
                    if item.money == None:
                        money = 0
                    else:
                        money = item.money
                        money = float(money) - int(amount)
                        item.money = money
                        item.save()
            query = CryptoWallet.objects.all()
            list_crypto_wallet = []
            for item in query:
                list_crypto_wallet.append(item)

                for item in list_crypto_wallet:
                    if str(item) == request.user.username:

                        # return render(request, 'debug.html', context={'list': request.POST.get('coin')})

                        for x in range(10):
                            if int(all_coins[x]['rank']) == int(request.POST.get('coin')):
                                actual_price = float(
                                    all_coins[x]['price_usd'])

                                coin_amount = round(amount/actual_price, 3)
                                coin_name = all_coins[x]['nameid']
                                coin_name = coin_name.replace('-', '')
                                code = f"item.{coin_name} += coin_amount"
                                exec(code)
                                item.save()
                                query = InvestmentPrice.objects.all()
                                list_investment_price = []
                                for item in query:
                                    list_investment_price.append(item)
                                for item in list_investment_price:
                                    if str(item) == request.user.username:

                                        price = 0
                                        code = f"""if item.{coin_name}>0:
                                            item.{coin_name} = ({actual_price}+item.{coin_name})/2"""
                                        exec(code)
                                        code = f"""if item.{coin_name} == 0:
                                            item.{coin_name} += {actual_price}"""
                                        exec(code)
                                        # if price > 0:
                                        #     code = f"item.{coin_name} = ({actual_price}+item.{coin_name})/2"
                                        #     exec(code)
                                        # else:
                                        #     code = f"item.{coin_name} += {actual_price}"
                                        #     exec(code)
                                        item.save()
                                        return HttpResponseRedirect('/')
    return render(request, 'purchase.html', context)


@login_required
def sell(request):
    response = requests.get(
        'https://api.coinlore.net/api/tickers/?start=0&limit=100')
    coin_json = response.json()['data']
    all_coins = []
    for item in coin_json:
        all_coins.append(item)
    list_crypto_wallet = []
    investment_list = []
    list_item = []
    query = CryptoWallet.objects.all()
    for item in query:
        list_crypto_wallet.append(item)

    query = Wallet.objects.all()
    for item in query:
        list_item.append(item)

    for item in list_item:
        if str(item) == request.user.username:
            if item.money == None:
                money = 0
            else:
                money = item.money

    for item in list_crypto_wallet:
        if str(item) == request.user.username:
            if item.bitcoin > 0:
                investment_list.append('Bitcoin')
            if item.ethereum > 0:
                investment_list.append('Ethereum')
            if item.tether > 0:
                investment_list.append('Tether')
            if item.usdcoin > 0:
                investment_list.append('USD Coin')
            if item.binancecoin > 0:
                investment_list.append('Binance Coin')
            if item.binanceusd > 0:
                investment_list.append('Binance USD')
            if item.ripple > 0:
                investment_list.append('XRP')
            if item.cardano > 0:
                investment_list.append('Cardano')
            if item.dogecoin > 0:
                investment_list.append('Doge Coin')
            if item.solana > 0:
                investment_list.append('Solana')

    context = {
        'investment_list': investment_list,
    }
    if request.method == 'POST':
        list_crypto_wallet = []
        first_amount = []
        last_amount = []
        amount = float(request.POST.get('amount'))
        coin = request.POST.get('coin-form')
        coin = coin.lower()
        coin = coin.replace(' ', '')
        if coin == 'xrp':
            coin = 'ripple'
        query = CryptoWallet.objects.all()
        for item in query:
            list_crypto_wallet.append(item)
        for wallet in list_crypto_wallet:
            if str(wallet) == request.user.username:
                first_amount = [wallet.bitcoin, wallet.ethereum, wallet.tether, wallet.usdcoin, wallet.binancecoin,
                                wallet.binanceusd, wallet.ripple, wallet.cardano, wallet.dogecoin, wallet.solana,]
                code = f"""if {amount} <= wallet.{coin}:
                    wallet.{coin} = wallet.{coin}-{amount}"""
                exec(code)
                wallet.save()
                last_amount = [wallet.bitcoin, wallet.ethereum, wallet.tether, wallet.usdcoin, wallet.binancecoin,
                               wallet.binanceusd, wallet.ripple, wallet.cardano, wallet.dogecoin, wallet.solana,]

                if first_amount[0] == last_amount[0] and first_amount[1] == last_amount[1] and first_amount[2] == last_amount[2] and first_amount[3] == last_amount[3] and first_amount[4] == last_amount[4] and first_amount[5] == last_amount[5] and first_amount[6] == last_amount[6] and first_amount[7] == last_amount[7] and first_amount[8] == last_amount[8] and first_amount[9] == last_amount[9]:
                    return render(request, 'sell.html', context={'message': "Coin Anda Terlalu Sedikit!", 'investment_list': investment_list})
                else:
                    query = Wallet.objects.all()
                    for item in query:
                        list_item.append(item)

                    for item in list_item:
                        if str(item) == request.user.username:
                            for coinname in all_coins:
                                if coinname['nameid'] == coin:
                                    item.money += amount * \
                                        float(coinname['price_usd'])
                                    item.save()

                    list_item = []
                    query = InvestmentPrice.objects.all()
                    for item in query:
                        list_item.append(item)

                    for item in list_item:
                        if str(item) == request.user.username:
                            for c in first_amount:
                                if c == amount:
                                    code = f"""item.{coin} = 0"""
                                    exec(code)
                                    item.save()
                    return HttpResponseRedirect('/profile/')

    return render(request, 'sell.html', context)

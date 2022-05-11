from classe_cible import LeRoboTrader, TraderChef, TraderBnp

#Définition des personnages
chief = TraderChef.TraderChef()
kerviel = LeRoboTrader.LeRoboTrader(chief)
kerviel.set_name("kerviel")
trader = TraderBnp.TraderBnp(chief)

#PnL du premier jour
kerviel.add_to_daily_yield(0.30)
trader.add_to_daily_yield(0.01)
kerviel.update_pnl_trader_chef()
trader.update_pnl_trader_chef()

print('Le PnL cumulé au premier jour est de {}%'.format(chief.get_pnl()*100))

#Deuxième jour
kerviel.add_to_daily_yield(-0.40)
trader.add_to_daily_yield(0.02)
trader.update_pnl_trader_chef()

print("Le PnL cumulé au deuxième jour est de {}% mais le robotrader kerviel n'a pas déclaré son PnL négatif de {}%...".format(chief.get_pnl()*100, kerviel.get_daily_yield()*100))

#Troisième jour
kerviel.add_to_daily_yield(-0.95)
trader.add_to_daily_yield(0.01)
trader.update_pnl_trader_chef()

print("Le PnL cumulé au troisième jour est de {}% mais le robotrader kerviel n'a pas déclaré son PnL négatif de {}%...".format(chief.get_pnl()*100, kerviel.get_daily_yield()*100))

#Quatrième jour
kerviel.update_pnl_trader_chef()
print("Le robotrader kervial a prévenu son chef, celui-ci se rend compte que la banque est en faillite avec un PnL total de {}%".format(chief.get_pnl()*100))



from classe_cible import LeRobo, TraderChef, TraderBnp

#Définition des personnages
kerviel = LeRobo.LeRobo()
kerviel.set_name("kerviel")
trader = TraderBnp.TraderBnp()
chief = TraderChef.TraderChef(trader)
kerviel.subscribe(chief)

#PnL du premier jour
kerviel.add_to_daily_yield(0.30)
trader.add_to_daily_yield(0.01)
kerviel.notify_observers()
trader.notify_observers()

#Deuxième jour
kerviel.add_to_daily_yield(-0.40)
trader.add_to_daily_yield(0.02)
trader.notify_observers()
print("Oh non, le robotrader Kerviel n'a pas prévenu son chef.")

#Troisième jour
kerviel.add_to_daily_yield(-0.95)
trader.add_to_daily_yield(0.01)
trader.notify_observers()
print("Oh non, le robotrader Kerviel n'a pas prévenu son chef.")

#Quatrième jour
kerviel.notify_observers()



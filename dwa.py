
# For the breakdown by month
# cat.loc['2019-01-01':'2019-02-01'].tail(5) # Check it out here
print("January")
cat_jan = cat.loc['2019-01-01':'2019-02-01']
cat_jan.groupby(cat_jan.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("February")
cat_feb=cat.loc['2019-02-01':'2019-03-01']
cat_feb.groupby(cat_feb.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("March")
cat_march=cat.loc['2019-03-01':'2019-04-01']
cat_march.groupby(cat_march.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("April")
cat_april=cat.loc['2019-04-01':'2019-05-01']
cat_april.groupby(cat_april.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("May")
cat_may = cat.loc['2019-05-01':'2019-06-01']
cat_may.groupby(cat_may.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("June")
cat_june=cat.loc['2019-06-01':'2019-07-01']
cat_june.groupby(cat_june.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("July")
cat_july=cat.loc['2019-07-01':'2019-08-01']
cat_july.groupby(cat_july.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("August")
cat_august=cat.loc['2019-08-01':'2019-09-01']
cat_august.groupby(cat_august.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("September")
cat_september=cat.loc['2019-09-01':'2019-10-01']
cat_september.groupby(cat_september.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("October")
cat_oct=cat.loc['2019-10-01':'2019-11-01']
cat_oct.groupby(cat_oct.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("November")
cat_nov=cat.loc['2019-11-01':'2019-12-01']
cat_nov.groupby(cat_nov.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("December")
cat_dec=cat.loc['2019-12-01':'2021-01-01']
cat_dec.groupby(cat_dec.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("2021 Jan")
cat_dec=cat.loc['2021-01-01':'2021-02-01']
cat_dec.groupby(cat_dec.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()

print("2021 Feb")
cat_dec=cat.loc['2021-02-01':'2021-03-01']
cat_dec.groupby(cat_dec.Category).Withdrawal.sum().plot(kind ='pie')
plt.show()
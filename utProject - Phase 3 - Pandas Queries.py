#Question 1
pego = df[df.company=='peugeot']
a  = pego['car'].value_counts()

hyu = df[df.company=='hyundai']
a  = hyu['car'].value_counts()

#Question 2
two = df[((df.year>1394) & (df.year<1401)| (df.year>2015))]

#Question3
p206sd = df[(df.company == 'peugeot') & (df.car == '206sd')]
p206sd.tream.value_counts()

#Question4
df.describe()
safari = df[df.kilometer == 930000.000000]

#Question5
cars = df.groupby(['company']).mean()

#Question6
df['car'].describe()

#Question7
older = df[(df.company == 'peugeot') & (df.car == '206') & (df.year > 1385) & (df.year <= 1392)]
newer = df[(df.company == 'peugeot') & (df.car == '206') & (df.year > 1392) & (df.year <= 1400)]
older['price'].describe()
newer['price'].describe()
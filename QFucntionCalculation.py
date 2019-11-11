from scipy.stats import norm

x = 5.4772
print('Q(', x, ') = ', norm.sf(x))

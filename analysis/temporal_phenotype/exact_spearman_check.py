"""Re-compute the repo's Spearman test (n=6 'unique tissues') with an exact permutation p-value. Stdlib only."""
import itertools, math
tissues = {  # exactly what the notebook's groupby('tissue') produces
 'Breast stroma': (60, 27), 'Colonic epithelium': (4, 19), 'Endometrium': (28, 22),
 'Endometrium/myometrium': (28, 28), 'Gastric epithelium': (5, 19), 'Thyroid epithelium': (2920, 28)}
x = [v[0] for v in tissues.values()]; y = [v[1] for v in tissues.values()]
def ranks(v):
    s = sorted(v); return [ (s.index(a) + 1 + s.index(a) + s.count(a)) / 2 for a in v]
def pearson(a, b):
    n=len(a); ma=sum(a)/n; mb=sum(b)/n
    return sum((p-ma)*(q-mb) for p,q in zip(a,b))/math.sqrt(sum((p-ma)**2 for p in a)*sum((q-mb)**2 for q in b))
rx, ry = ranks(x), ranks(y)
rho = pearson(rx, ry)
perms = [pearson(rx, list(p)) for p in itertools.permutations(ry)]
p_two = sum(1 for r in perms if abs(r) >= abs(rho) - 1e-12)/len(perms)
p_one = sum(1 for r in perms if r >= rho - 1e-12)/len(perms)
t = rho*math.sqrt((len(x)-2)/(1-rho**2))
print(f"n={len(x)}  Spearman rho={rho:.3f}  t-approx statistic={t:.2f} (df={len(x)-2})")
print(f"exact permutation p (two-sided)={p_two:.4f}  (one-sided)={p_one:.4f}  [{len(perms)} permutations]")
# Leave-one-out: how fragile is it?
for k in tissues:
    xs=[v[0] for kk,v in tissues.items() if kk!=k]; ys=[v[1] for kk,v in tissues.items() if kk!=k]
    r=pearson(ranks(xs), ranks(ys))
    pp=[pearson(ranks(xs), list(p)) for p in itertools.permutations(ranks(ys))]
    print(f"  drop {k:24s} rho={r:.3f}  exact two-sided p={sum(1 for q in pp if abs(q)>=abs(r)-1e-12)/len(pp):.3f}")
# Merge the two endometrial rows (same tissue compartment, earliest age) -> n=5
t5 = dict(tissues); t5.pop('Endometrium/myometrium')
xs=[v[0] for v in t5.values()]; ys=[v[1] for v in t5.values()]
r=pearson(ranks(xs), ranks(ys)); pp=[pearson(ranks(xs), list(p)) for p in itertools.permutations(ranks(ys))]
print(f"n=5 (endometrial rows merged) rho={r:.3f} exact two-sided p={sum(1 for q in pp if abs(q)>=abs(r)-1e-12)/len(pp):.3f}; smallest attainable two-sided p at n=5 = {2/120:.4f}")

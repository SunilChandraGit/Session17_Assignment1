import numpy as np
from scipy.stats import binom

#probabilty of choosing correct option
p_a=(1/4)

#number of successes required
no_of_suc = 5

#number of trials
no_of_trials = 20

p_a_5 = binom.pmf(no_of_suc, no_of_trials, p_a)

'Probability of giving exactly 5 correct answers {0:.7f}'.format(p_a_5)
from hyperopt import fmin, tpe, hp, Trials
from hyperopt.mongoexp import MongoTrials

#trials = Trials()
trials = MongoTrials('mongo://localhost:27017/hyperopt_db/jobs', exp_key='exp1')
best = fmin(fn=lambda x: x ** 2,
    space=hp.uniform('x', -10, 10),
    algo=tpe.suggest,
    max_evals=100,
    trials=trials)
print(best)

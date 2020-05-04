# Search Space and Decorator
import autogluon as ag
# import pdb

# part 1
@ag.autogluon_function(
    framework=ag.space.Categorical('mxnet', 'pytorch'),
)
def myfunc(framework):
    return framework
i = myfunc()
print(i)

# part 2
# pdb.set_trace()
@ag.autogluon_object(
    name=ag.space.Categorical('auto', 'gluon'),
    y=ag.space.Categorical(*list(range(100))),
)
class myobj:
    def __init__(self, name):
        self.name = name
h = myobj()
print(h.cs)

# part 3
@ag.autogluon_register_args(
    x=ag.space.Categorical(*list(range(100))),
    y=ag.space.Categorical(*list(range(100))),
)
def rl_simulation(args, reporter):
    x, y = args.x, args.y
    reporter(accuracy=Z[y][x])

print(rl_simulation.__dict__)

# error
# random_scheduler = ag.scheduler.FIFOScheduler(rl_simulation, rl_simulation.args,
#                                               resource={'num_cpus': 1, 'num_gpus': 0},
#                                               num_trials=300,
#                                               reward_attr="accuracy",
#                                               resume=False)

# random_scheduler.run()
# random_scheduler.join_jobs()
# print('Best config: {}, best reward: {}'.format(random_scheduler.get_best_config(), random_scheduler.get_best_reward()))
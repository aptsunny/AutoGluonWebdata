# 30_5
python benchmark.py --data-dir data --dataset shopee-iet-machine-learning-competition --num-trials 30 --num-epochs 5 --batch-size 48 --ngpus-per-trial 8 
# 180_1
python benchmark.py --data-dir data --dataset shopee-iet-machine-learning-competition --num-trials 1 --num-epochs 180 --batch-size 48 --ngpus-per-trial 1 --resume --submission

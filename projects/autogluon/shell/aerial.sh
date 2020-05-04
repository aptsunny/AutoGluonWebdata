python data_processing.py --dataset aerial --data-dir data
# 30_5
python benchmark.py --data-dir data --dataset aerial-cactus-identification --num-trials 30 --num-epochs 5 --batch-size 64 --ngpus-per-trial 8 
# 180_1
python benchmark.py --data-dir data --dataset aerial-cactus-identification --num-trials 1 --num-epochs 180 --batch-size 64 --ngpus-per-trial 1 --resume --submission

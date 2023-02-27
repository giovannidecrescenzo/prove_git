#!/bin/bash
#SBATCH --get-user-env
#SBATCH --time=0-00:05:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=5000
#SBATCH --job-name=setupfit

python vero_script.py

curl "https://api.telegram.org/bot6120806348:AAE2DmYWN5t8AmdGezmgZIgAXm6VgiFYBLk/sendMessage?chat_id=-1001827720736&text=finito_qua"



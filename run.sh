CUDA_VISIBLE_DEVICES=4,5 llamafactory-cli train trial/qwen2.5-3b-instruct_ts.yaml
modelscope download --model Qwen/Qwen2.5-3B-Instruct --local_dir models/Qwen2.5-3B-Instruct

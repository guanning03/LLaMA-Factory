from huggingface_hub import HfApi

# 初始化 Huggingface API
api = HfApi()

# 创建新的模型仓库
repo_id = "guanning/T_3b_lora-sft_step4000"
api.create_repo(repo_id, private=False)

# 上传模型文件
api.upload_folder(
    folder_path="models/T_3b_lora-sft_step4000",
    repo_id=repo_id,
    repo_type="model"
)
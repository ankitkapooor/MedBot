mkdir experiments

for epoch in 1
do
	python run_lm_finetuning.py \
	--model_name_or_path distilgpt2 \
	--model_type gpt2 \
	--train_data_file /content/Dataset/dataset_train.txt \
	--output_dir experiments/epochs_$epoch \
	--do_train \
	--per_device_train_batch_size 2 \
  --overwrite_output_dir \
	--num_train_epochs $epoch
done

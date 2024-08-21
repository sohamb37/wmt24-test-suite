import os
import json
import csv
# from comet import download_model, load_from_checkpoint
import pandas as pd
# from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from sacrebleu.metrics import BLEU

# Download and load the COMET model
# model_path = download_model("Unbabel/XCOMET-XXL")
# model = load_from_checkpoint(model_path)

# Define the folder path
base_folder = "Domains"

# df = pd.Dataframe()
ls_system_scores =[]
ls_hyp_files = []

# Iterate through each subfolder
for subfolder in sorted(os.listdir(base_folder)):
    if subfolder == "full":
        continue
    subfolder_path = os.path.join(base_folder, subfolder)
    
    # Check if the path is a directory
    if os.path.isdir(subfolder_path):
        source_file = os.path.join(subfolder_path, f"{subfolder}_source.txt")
        reference_file = os.path.join(subfolder_path, f"{subfolder}_reference.txt")
        
        # Read the source and reference files
        with open(source_file, 'r', encoding='utf-8') as src_f, open(reference_file, 'r', encoding='utf-8') as ref_f:
            sources = src_f.readlines()
            references = ref_f.readlines()
        
        # Process each hypothesis file
        for filename in sorted(os.listdir(subfolder_path)):
            if filename.endswith(".txt") and filename not in [f"{subfolder}_source.txt", f"{subfolder}_reference.txt"]:
                hypothesis_file = os.path.join(subfolder_path, filename)
                
                # Read the hypothesis file
                with open(hypothesis_file, 'r', encoding='utf-8') as hyp_f:
                    hypotheses = hyp_f.readlines()
                
                # Create data for prediction
                # data = [
                #     {
                #         "src": src.strip(), 
                #         "mt": hyp.strip(), 
                #         "ref": ref.strip()
                #     }
                #     for src, hyp, ref in zip(sources, hypotheses, references)
                # ]
                

                # Make predictions
                # model_output = model.predict(data, batch_size=32, gpus=1)
                # document_scores = sentence_bleu([references], hypotheses)                
                
                # Calculate BLEU scores for each segment
                # bleu_scores = []
                # smoothing = SmoothingFunction().method1
                # for hyp, ref in zip(hypotheses, references):
                #     score = sentence_bleu([ref.strip().split()], hyp.strip().split(), smoothing_function=smoothing)
                #     bleu_scores.append(score)
                
                # # Calculate the average BLEU score (system-level score)
                # system_bleu_score = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0

                bleu = BLEU()
                score = bleu.corpus_score(hypotheses, [references])
                bleu_score = float(str(score).split()[2])
                ls_system_scores.append(bleu_score)
                # ls_system_scores.append(system_bleu_score)
                

                base_file_name = os.path.splitext(os.path.basename(hypothesis_file))[0]
                ls_hyp_files.append(base_file_name)

                # print(reference_file)
                # print(hypothesis_file)
                # print(system_bleu_score)


df = pd.DataFrame({"file": ls_hyp_files, "bleu_scores": ls_system_scores})
print(df.head())
df.to_csv("/home/soham37/Downloads/xCOMET/xCOMET/bleu_scores.csv", index = False)

                # Save error spans to the output file
                # output_dir = os.path.join("Outputs_XXL", subfolder)
                # os.makedirs(output_dir, exist_ok=True)
                # output_file = os.path.join(output_dir, f"{filename.split('.')[0]}.json")
                # with open(output_file, 'w', encoding='utf-8') as out_f:
                #     json.dump(model_output.metadata.error_spans, out_f, ensure_ascii=False, indent=4)
                
                # # Define paths for segment and system score TSV files
                # segment_scores_file = os.path.join(output_dir, f"{filename.split('.')[0]}_segment_scores.tsv")
                # system_scores_file = os.path.join(output_dir, f"{filename.split('.')[0]}_system_scores.tsv")
                
                # # Write segment-level scores to TSV
                # with open(segment_scores_file, 'w', encoding='utf-8', newline='') as seg_f:
                #     seg_writer = csv.writer(seg_f, delimiter='\t')
                #     seg_writer.writerow(["Filename", "Segment-Level Scores"])
                #     seg_writer.writerow([filename] + model_output.scores)
                
                # # Write system-level score to TSV
                # with open(system_scores_file, 'w', encoding='utf-8', newline='') as sys_f:
                #     sys_writer = csv.writer(sys_f, delimiter='\t')
                #     sys_writer.writerow(["Filename", "System-Level Score"])
                #     sys_writer.writerow([filename, model_output.system_score])

                # # Print scores for each file
                # print(f"Scores for {filename}:")
                # print(model_output.scores)
                # print("System-level score:", model_output.system_score)


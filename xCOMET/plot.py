import os
import csv
import matplotlib.pyplot as plt

# Define the base output folder
base_output_folder = "Outputs_XXL"

# Iterate through each subfolder in the base output folder
for subfolder in sorted(os.listdir(base_output_folder)):
    subfolder_path = os.path.join(base_output_folder, subfolder)
    
    # Check if the path is a directory
    if os.path.isdir(subfolder_path):
        system_scores = []
        filenames = []

        # Iterate through each file in the subfolder
        for filename in os.listdir(subfolder_path):
            if filename.endswith("_system_scores.tsv"):
                system_scores_file = os.path.join(subfolder_path, filename)
                
                # Read the system score from the TSV file
                with open(system_scores_file, 'r', encoding='utf-8') as sys_f:
                    reader = csv.reader(sys_f, delimiter='\t')
                    next(reader)  # Skip the header
                    for row in reader:
                        # Strip subfolder name from beginning and _system_scores.tsv from the end
                        clean_filename = filename.replace(f"{subfolder}_", "").replace("_system_scores.tsv", "")
                        filenames.append(clean_filename)
                        system_scores.append(float(row[1]))
        
        # Create a bar graph for the system scores
        plt.figure(figsize=(12, 8))
        plt.bar(filenames, system_scores, color='skyblue')
        plt.xlabel('Filename')
        plt.ylabel('System-Level Score')
        plt.title(f'System-Level Scores for {subfolder}')
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        
        # Save the plot as a PNG file
        plot_file = os.path.join(subfolder_path, f"{subfolder}_system_scores_plot.png")
        plt.savefig(plot_file)
        plt.close()
        
        print(f"Plot saved for {subfolder} at {plot_file}")

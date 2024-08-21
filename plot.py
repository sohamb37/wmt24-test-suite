import os
import csv
import statistics
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
        for filename in sorted(os.listdir(subfolder_path)):
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

        # Calculate the mean of the values
        mean_value = statistics.harmonic_mean(system_scores)

        bars = plt.bar(filenames, system_scores, color='skyblue')

        # Add a line for the mean value
        plt.axhline(y=mean_value, color='black', linestyle='--', label=f'Harmonic Mean: {mean_value:.2f}')

        plt.xlabel('Filename')
        plt.ylabel('System-Level Score')
        plt.title(f'System-Level Comet Scores for {subfolder}')
        plt.legend()
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}',
                    ha='center', va='bottom')
        plt.tight_layout()


        # Save the plot as a PNG file
        plot_file = os.path.join(subfolder_path, f"{subfolder}_system_scores_plot.png")
        plt.savefig(plot_file)
        plt.close()
        
        print(f"Plot saved for {subfolder} at {plot_file}")


        # # Calculate the mean of the values
        # mean_value = df_human_domain['human_score'].mean()

        # # Create a bar plot
        # plt.figure(figsize=(10, 6))
        # # plt.bar(final_model['file'], final_model['bleu_scores'], color='skyblue', label='Values')

        # bars = plt.bar(df_human_domain['domains'], df_human_domain['human_score'], color='skyblue', label='Values')

        # # Add a line for the mean value
        # plt.axhline(y=mean_value, color='black', linestyle='--', label=f'Mean: {mean_value:.2f}')

        # # Add labels and title
        # plt.xlabel('Domains')
        # plt.ylabel('Scores')
        # plt.title('Domain wise Human Scores out of 5')
        # plt.legend()

        # # Rotate x-axis labels to vertical
        # plt.xticks(rotation=90)


        # # # Save the plot to a file
        # # plt.savefig('bar_graph_with_mean_line.png', bbox_inches='tight')
        # # Display the value on each bar
        # for bar in bars:
        #     height = bar.get_height()
        #     plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}',
        #             ha='center', va='bottom')
            
        
        
        

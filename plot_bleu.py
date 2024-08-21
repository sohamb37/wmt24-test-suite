# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Assuming your DataFrame is named df
# # For demonstration, let's create a sample DataFrame
# # data = {
# #     'Column1': np.random.rand(96),
# #     'Column2': np.random.rand(96)
# # }
# # df = pd.DataFrame(data)

# df = pd.read_csv("/home/soham37/Downloads/xCOMET/xCOMET/bleu_scores.csv")

# # Number of rows in each chunk
# chunk_size = 16

# # Total number of chunks
# n_chunks = len(df) // chunk_size

# # Split the DataFrame into chunks of 16 rows
# chunks = [df.iloc[i*chunk_size:(i+1)*chunk_size] for i in range(n_chunks)]

# # Plotting each chunk
# for i, chunk in enumerate(chunks):
#     plt.figure(figsize=(10, 6))
    
#     # Plot a bar chart for each column in the chunk
#     chunk.plot(kind='bar', ax=plt.gca(), title=f'Chunk {i+1}', legend=True)
    
#     plt.xlabel('Index')
#     plt.ylabel('Values')
#     plt.title(f'Bar Chart for Chunk {i+1}')
#     plt.show()

# print(chunks)

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Assuming your DataFrame is named df
# # For demonstration, let's create a sample DataFrame
# # data = {
# #     'Column1': np.random.rand(96),
# #     'Column2': np.random.rand(96)
# # }
# # df = pd.DataFrame(data)

# df = pd.read_csv("/home/soham37/Downloads/xCOMET/xCOMET/bleu_scores.csv")

# # Chunk names
# chunk_names = ['education', 'general', 'judicial', 'literature', 'noisy', 'review']

# # Number of rows in each chunk
# chunk_size = 16

# # Custom index labels
# # index_labels = []
# index_labels = ["Aya23", "Claude_3_5", "CommandR_plus", "CycleL", "GPT_4", "IKUN_C", "IKUN", "IOL_Research", "Llama3_70B", "NVIDIA_NeMo", "ONLINE_A", "ONLINE_B", "ONLINE_G", "TranssionMT", "Unbabel_Tower70B", "ZMT"]

# # Total number of chunks
# n_chunks = len(chunk_names)

# # Split the DataFrame into chunks of 16 rows
# chunks = [df.iloc[i*chunk_size:(i+1)*chunk_size].set_index(pd.Index(index_labels)) for i in range(n_chunks)]

# # Plotting each chunk and saving the graphs
# for i, (chunk, name) in enumerate(zip(chunks, chunk_names)):
#     plt.figure(figsize=(10, 6))
    
#     # Plot a bar chart for each column in the chunk
#     chunk.plot(kind='bar', ax=plt.gca(), title=f'Domain: {name}', legend=True)
    
#     plt.xlabel('Index')
#     plt.ylabel('Values')
#     plt.title(f'Bar Chart for {name.capitalize()} Domain')
    
#     # Save the plot to a file
#     plt.savefig(f'{name}_chunk.png', format='png', dpi=300, bbox_inches='tight')
    
#     # Optional: Display the plot
#     # plt.show()  # Uncomment this line if you want to display the plot

#     # Close the plot to free memory
#     plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your DataFrame
df = pd.read_csv("/home/soham37/Downloads/xCOMET/xCOMET/bleu_scores.csv")

# # Verify that all columns are numeric
# df = df.apply(pd.to_numeric, errors='coerce')

# # Check for any non-numeric data
# if df.isnull().values.any():
#     print("Warning: Non-numeric data found. Please check your DataFrame.")

# Chunk names
chunk_names = ['education', 'general', 'judicial', 'literature', 'noisy', 'review']

# Number of rows in each chunk
chunk_size = 16

# Custom index labels
index_labels = ["Aya23", "Claude_3_5", "CommandR_plus", "CycleL", "GPT_4", "IKUN_C", "IKUN", "IOL_Research", "Llama3_70B", "NVIDIA_NeMo", "ONLINE_A", "ONLINE_B", "ONLINE_G", "TranssionMT", "Unbabel_Tower70B", "ZMT"]

# Total number of chunks
n_chunks = len(chunk_names)

# Split the DataFrame into chunks of 16 rows
chunks = [df.iloc[i*chunk_size:(i+1)*chunk_size].set_index(pd.Index(index_labels)) for i in range(n_chunks)]

# Plotting each chunk and saving the graphs
# for i, (chunk, name) in enumerate(zip(chunks, chunk_names)):
#     plt.figure(figsize=(12, 7))
    
#     # Ensure the chunk data is numeric
#     chunk = chunk.apply(pd.to_numeric, errors='coerce')
    
#     # Plot a bar chart for each column in the chunk
#     ax = chunk.plot(kind='bar', ax=plt.gca(), title=f'Domain: {name}', legend=False, colormap='tab20')  # Use the 'tab20' colormap for default colors

#     # Annotate the bars with their values
#     for p in ax.patches:
#         ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                     ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=8)
    
#     # Calculate and plot the mean line
#     mean_value = chunk.mean().mean()
#     plt.axhline(mean_value, color='black', linestyle='--', linewidth=1)
#     plt.text(len(chunk.columns) - 1, mean_value, f'Mean: {mean_value:.2f}', color='black', ha='right', va='bottom')
    
#     plt.xlabel('Models')
#     plt.ylabel('Scores')
#     plt.title(f'Bleu Scores for {name.capitalize()} Domain')
    
#     # Save the plot to a file
#     plt.savefig(f'{name}_chunk.png', format='png', dpi=300, bbox_inches='tight')
    
#     # Close the plot to free memory
#     plt.close()

print(chunks.iloc[3][1])









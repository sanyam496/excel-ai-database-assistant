# import pandas as pd
# import random

# # -------- FILE PATHS --------

# purchase_file = "/Users/sanyamtiwari/Desktop/excel_ai_project/PURCHASE_UPDATED.xlsx"

# po_file = "/Users/sanyamtiwari/Desktop/excel_ai_project/PO_REGISTER.xlsx"

# # -------- FUNCTION --------

# def generate_rows(input_file, output_file):

#     print("\nProcessing:", input_file)

#     df = pd.read_excel(input_file)

#     print("Original rows:", len(df))

    
#     numeric_cols = df.select_dtypes(include=["int64","float64"]).columns

#     averages = {}

#     for col in numeric_cols:
#         averages[col] = df[col].mean()

#     new_rows = []

#     for i in range(50):

       
#         row = df.sample(1).iloc[0].copy()

#         for col in numeric_cols:

#             avg = averages[col]

          
#             variation = random.uniform(0.9,1.1)

#             row[col] = round(avg * variation,2)

#         new_rows.append(row)

#     new_df = pd.DataFrame(new_rows)

#     final_df = pd.concat([df,new_df],ignore_index=True)

#     print("New rows:",len(final_df))

#     final_df.to_excel(output_file,index=False)

#     print("Saved file:",output_file)


# # -------- RUN SCRIPT --------

# generate_rows(
#     purchase_file,
#     "/Users/sanyamtiwari/Desktop/excel_ai_project/PURCHASE_UPDATED.xlsx"
# )

# generate_rows(
#     po_file,
#     "/Users/sanyamtiwari/Desktop/excel_ai_project/PO_UPDATED.xlsx"
# )
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key="8f0b2d8e5197447ca7dde63d4cb036c6",  
    api_version="2023-12-01-preview",
    azure_endpoint="https://ao-dd-lexer-test.openai.azure.com/"
)

# Loop through each row in Renamed Columns & concatenate the data into a single string. Pass resulting string to the API
Renamed_Columns = dataset

for index, row in Renamed_Columns.iterrows():
    messages = [
        {
            "role": "system",
            "content": "For each movie, you will have the followwing information: Company, Price to Earnings, Price to Book, Return to Equity%, Debt to Equity, Current Ratio, Gross Margin%. Then, I will analyze the ratios and write a brief summary using the company name "
        },
        {
            "role": "user",
            "content": ''.join([str(col) for col in row])
        }
    ]
    # OpenAI Chat API
    chat = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=messages
    )
# Process the response from API
response = chat.choices[0].message.content
# Write the response Back to the Report
Renamed_Columns.at[index, "result"] = response
from openai import AzureOpenAI

dataset = pd.read_csv('https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-4/datascience/master/spotify_songs.csv')
    
client = AzureOpenAI(
    api_key="",  
    api_version="2023-12-01-preview",
    azure_endpoint="https://ao-dd-lexer-test.openai.azure.com/"
)



# Loop through each row in Renamed Columns & concatenate the data into a single string. Pass resulting string to the API
renamed_columns = dataset

system_message = 'For each song, I will give you the following information: song (containing the tile) and text (containing the lyrics). Then, analyze the text and write a brief summary of the lyrics for each song tile'
for index, row in renamed_columns.iterrows():
    messages = [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": ': '.join([str(col) for col in row])
        }
    ]
    # OpenAI Chat API
    chat = client.chat.completions.create(
    model="gpt-35-turbo", 
    messages=messages
    )
    # Process the response from API
    response = chat.choices[0].message.content
    # Write the response Back to the Report
    renamed_columns.at[index, "result"] = response
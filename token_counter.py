import tiktoken

encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens_list = encoder.encode("Voce é um categorizador de produtos")
print(tokens_list)
print(len(tokens_list))
entry_cust = (len(tokens_list) / 1000) * 0.0015
print(f"Custo de entrada: {entry_cust}")
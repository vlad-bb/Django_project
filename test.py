quote = """
"Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world,
 stimulating progress, giving birth to evolution." - Albert Einstein
"""
rfind_indx = quote.rfind('"')
lfind_indx = quote.find('"')

clear_quote = quote[lfind_indx+1:rfind_indx]
print(clear_quote)
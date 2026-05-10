from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

text = """
Yes, absolutely. Saying “God bless you” to an elder is generally acceptable and respectful in many cultures and contexts. It’s often used to express goodwill, gratitude, care, or respect.

For example:

“Thank you, uncle. God bless you.”
“Take care, aunty. God bless you.”
“God bless you for your kindness.”

However, tone and cultural context matter. In some very traditional settings, younger people may prefer phrases like:

“Bless me”
“Please keep me in your blessings”

instead of directly saying “God bless you” to elders.

But in normal English conversation, saying “God bless you” to an elder is perfectly fine and polite.
"""
res=splitter.split_text(text)

print(res)
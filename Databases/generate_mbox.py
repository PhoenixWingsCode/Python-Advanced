# generate_mbox.py

sample_data = """From: alice@example.com
From: bob@example.com
From: alice@example.com
From: carol@example.com
From: bob@example.com
From: alice@example.com
From: dave@example.com
From: carol@example.com
From: bob@example.com
From: alice@example.com
From: eve@example.com
From: frank@example.com
From: alice@example.com
From: bob@example.com
From: carol@example.com
"""

with open("mbox-short.txt", "w") as f:
    f.write(sample_data)

print("✅ mbox-short.txt created with sample email data.")
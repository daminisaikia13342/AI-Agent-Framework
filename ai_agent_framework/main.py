from agents.document_agent import run as run_document_agent
from agents.support_agent import run as run_support_agent

print("\n=== Document Analysis Agent ===")
doc_result = run_document_agent("invoice_2025.pdf")
print(doc_result)

print("\n=== Customer Support Agent ===")
support_result = run_support_agent("where is my order?")
print(support_result)

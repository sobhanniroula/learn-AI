from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


# Write a tool to read a doc
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document given and return it as a string.",
)
def read_document(
    doc_id: str = Field(description="The ID of the document to read."),
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]


# Write a tool to edit a doc
@mcp.tool(
    name="edit_doc_contents",
    description="Edit the contents of a document given by replacing a string with another string and return the updated content.",
)
def edit_document(
    doc_id: str = Field(description="The ID of the document to edit."),
    old_text: str = Field(description="The text to be replaced. Must match exactly with the text in the document."),
    new_text: str = Field(description="The text to replace with."),
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    docs[doc_id] = docs[doc_id].replace(old_text, new_text)
    return docs[doc_id]


# Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
    name="list_doc_ids",
    description="Return a list of all document IDs.",
)
def list_documents():
    return list(docs.keys())


# Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
    name="get_doc_contents",
    description="Return the contents of a specific document.",
)
def get_document_contents(doc_id: str):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]


# Write a prompt to rewrite a doc in markdown format
@mcp.prompt(
    name="format_document",
    description="Rewrite the contents of a document in markdown format.",
)
def format_document(doc_id: str=Field(description="The ID of the document to format.")) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax. 
    
    The id of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>
    
    Add in headers, bullet points, tables, etc. as necessary. 
    Feel free to add in any additional formatting that you think would make the document more readable.
    Use the 'edit_document' tool to edit the document. 
    After the document has been reformatted, use the 'read_document' tool to read the contents of the document and return it.
    """
    return [base.Message(role="user", content=prompt)]


# Write a prompt to summarize a doc
@mcp.prompt(
    name="summarize_document",
    description="Summarize the contents of a document.",
)
def summarize_document(doc_id: str=Field(description="The ID of the document to summarize.")) -> list[base.Message]:
    prompt = f"""
    Your goal is to summarize a document. 
    
    The id of the document you need to summarize is:
    <document_id>
    {doc_id}
    </document_id>
    
    Use the 'read_document' tool to read the contents of the document and return it.
    """
    return [base.Message(role="user", content=prompt)]


if __name__ == "__main__":
    mcp.run(transport="stdio")

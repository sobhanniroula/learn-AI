from pydantic import Field
from mcp.server.fastmcp import FastMCP

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

# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")

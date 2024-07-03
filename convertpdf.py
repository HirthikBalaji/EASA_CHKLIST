import glob

from markdown_pdf import MarkdownPdf, Section

for doc in glob.glob("./CHECKLISTS/*.md"):
    with open(doc) as file:
        markdown_content = file.read()

    pdf = MarkdownPdf()
    pdf.meta["title"] = 'Title'
    pdf.add_section(Section(markdown_content, toc=False))
    pdf.save(doc.replace(".md", ".pdf"))
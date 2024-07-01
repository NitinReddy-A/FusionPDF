"""
PyMuPDF demo utility
--------------------
Remove certain types of page watermarks from a PDF

Watermarks typically are used to declare the status of a page, like "DRAFT", "PRELIMINARY", "For Internal Use only", etc.

PDF supports multiple ways of applying watermarks to a page. Among them are
special annotation types and so-called pagination artifacts.

Removal of annotation-based watermarks is no problem with PyMuPDF: just
delete the respective annotation.
Pagination artifacts in contrast require using PyMuPDF's low-level features.

This script reads a PDF and removes any watermark artifacts on its pages,
that depend on images or Form XObjects. This happens by locating and deleting
the "Do" command within the watermark artifact declaration.

Usage: python remove-watermarks.py file.pdf

If watermarks were successfully removed, a new PDF 'file-nowm.pdf' is created
in the script's folder, else an information is printed on the console.
"""
import sys
import fitz




def process_page(page):
    """Process one page."""
    doc = page.parent  # the page's owning document
    page.clean_contents()  # clean page painting syntax
    xref = page.get_contents()[0]  # get xref of resulting /Contents
    changed = 0  # this will be returned
    # read sanitized contents, splitted by line
    cont_lines = page.read_contents().splitlines()
    for i in range(len(cont_lines)):  # iterate over the lines
        line = cont_lines[i]
        if not (line.startswith(b"/Artifact") and b"/Watermark" in line):
            continue  # this was not for us
        # line number i starts the definition, j ends it:
        j = cont_lines.index(b"EMC", i)
        for k in range(i, j):
            # look for image / xobject invocations in this line range
            do_line = cont_lines[k]
            if do_line.endswith(b"Do"):  # this invokes an image / xobject
                cont_lines[k] = b""  # remove / empty this line
                changed += 1
    if changed > 0:  # if we did anything, write back modified /Contents
        doc.update_stream(xref, b"\n".join(cont_lines))
    return changed


if __name__ == "__main__":
    doc = fitz.open('demo.pdf')
    changed = 0  # indicates successful removals
    for page in doc:
        changed += process_page(page)  # increase number of changes
    if changed > 0:
        x = "s" if doc.page_count > 1 else ""
        print(f"{changed} watermarks have been removed on {doc.page_count} page{x}.")
        doc.ez_save(doc.name.replace(".pdf", "-nowm.pdf"))
    else:
        print("Nothing to change")
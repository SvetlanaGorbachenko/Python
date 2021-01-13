#path to saving plug-in /usr/lib/gimp/2.0/plug-ins
#
# A GIMP plugin to save each pdf page as a separate image.

from gimpfu import *
import os
import sys

def export_pdf_as_images(pdf, path, name):
    for page in pdf.layers:
        page.visible = False 
    idx = 0
    for page in pdf.layers:
        page.visible = True
        pdf.active_layer = page
        filename = name+"_%d.jpg"%(idx+1)
        idx +=1
        fullpath = os.path.join(path, filename)
        new_pdf = pdb.gimp_image_duplicate(pdf)
        layer_n = pdb.gimp_image_merge_visible_layers(new_pdf, CLIP_TO_IMAGE)
        pdb.gimp_file_save(new_pdf,  layer_n, fullpath, filename)
        page.visible = False
        
register(
    "python-fu-export-pdf",
    "Export pdf pages as images",
    "Exports each layer(page) as a separate img-file",
    "Svetlana Gorbachenko",
    "",
    "",
    "E_xport PDF as images...",
    "*",
    [
        (PF_IMAGE, "pdf", "Input pdf", None),
        (PF_DIRNAME, "path", "Output directory", os.getcwd()),
        (PF_STRING, "name", "Output name", "")
    ],
    [],
    export_pdf_as_images,
    menu="<Image>/File/"
    )

main()

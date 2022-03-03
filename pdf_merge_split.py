import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))
        
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    
    filename = input('enter file name')
    user_choice = input('m: merge, s: split')
    
    if user_choice == 's':
        path = '{}.pdf'.format(filename)
        pdf_splitter(path)
    
    elif user_choice == 'm':
        print('Each pdf must be numbered ex filename_page_5.pdf')
        paths = glob.glob('{}_*.pdf'.format(filename))
        paths.sort()
        sel = input('a:all pages, s: specific pages')
        if sel == 'a':
            merger('{}_pdf_merge.pdf'.format(filename), paths)
            print('Created: {}_pdf_merge.pdf'.format(filename))
        elif sel == 's':
            pages = input('please specify pages ex: 1,2,5,6')
            l_pages = pages.split(',')
            path_sel = []
            for num in pages:
                for name in paths:
                    if num in name:
                        path_sel.append(name)
            merger('{}_pdf_merge_sel.pdf'.format(filename), path_sel)
            print('Created: {}_pdf_merge_sel.pdf'.format(filename))
        else:
            print('ERROR...')
    else:
        print('ERROR...')
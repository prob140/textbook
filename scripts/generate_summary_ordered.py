import nbformat as nbf
import glob
import shutil
import nb2html

retrieve_name_from_cell = lambda cell_source: cell_source.replace('#','').strip()

def retrieve_name_from_fname(fname):
    nb = nbf.read(open(fname),nbf.current_nbformat)
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            return  retrieve_name_from_cell(cell['source'])
    return 'ERROR'

def get_manual_configuration():
    import yaml
    return yaml.load(open('notebooks/config.yml'))

def get_configuration():
    configuration = []
    for chapter_folder in sorted(glob.glob("notebooks/Chapter_*")):
        all_section_fnames = sorted(glob.glob("%s/*.ipynb"%chapter_folder))
        all_section_info = [
                dict(
                    file_name=fname.rpartition('/')[2],
                    section_name=retrieve_name_from_fname(fname)
                )
            for fname in all_section_fnames]

        chapter_name = all_section_info[0]['section_name']
        configuration.append(dict(
            chapter_name=chapter_name,
            folder_name=chapter_folder[10:],
            sections=all_section_info,
                        ))
    return configuration

#
#
# In this section
#  - The summary file (SUMMARY.md) is generated
#
#
def generate_summary(configuration,cold=False):
    SUMMARY_head = """
# Summary

* [Authors and License](notebooks/README.md)
* [To the Student](notebooks/To_the_Student.ipynb)

    """

    chapter_summaries = [SUMMARY_head]

    for n,chapter in zip(range(1,len(configuration)+1),configuration):
        chapter_intro = chapter['sections'][0]['file_name']
        entries = ['* [Chapter %d: %s](notebooks/Chapter_%02d/%s)'%(n,chapter['chapter_name'],n,chapter_intro)]
        for i,section in list(enumerate(chapter['sections']))[1:]:
            section_md = section['file_name']
            section_entry = (' * [%d.%d %s](notebooks/Chapter_%02d/%s)'%(n,i,section['section_name'],n,section_md))
            entries.append(section_entry)
        chapter_summaries.append('\n'.join(entries)+'\n')

    SUMMARY_md ="\n".join(chapter_summaries)
    if cold:
        print(SUMMARY_md)
    else:
        with open("SUMMARY.md","w") as f:
            f.write(SUMMARY_md)

if __name__ == "__main__":
    configuration = get_configuration()
    generate_summary(configuration,cold=False)

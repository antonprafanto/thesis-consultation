import docx

doc = docx.Document('scratch/pedoman_docs/Template_Skripsi.docx')

for t_idx, t in enumerate(doc.tables):
    print(f"\n================ TABLE {t_idx} ================")
    for r_idx, row in enumerate(t.rows):
        cells_t = [c.text.strip().replace('\n', ' ') for c in row.cells]
        print(f"Row {r_idx}: {cells_t}")

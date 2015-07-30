from bioservices import ChEMBL

chembl=ChEMBL(verbose=False)

acc = 'P00519'

target_info = chembl.get_target_by_uniprotId(acc)
print target_info

target_chembl_id=target_info['chemblId']

bioactivities=chembl.get_target_bioactivities(str(target_chembl_id))

compound_chemblids = [ entry['ingredient_cmpd_chemblid'] for entry in bioactivities ]
print "# of compound chemblids:", len(compound_chemblids)

resjson = chembl.get_compounds_by_chemblId(chembl._chemblId_example)
print "Example compound retrieved by compound chemblid: \n", resjson

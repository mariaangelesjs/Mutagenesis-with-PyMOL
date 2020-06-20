#!/usr/bin/python
###################################################################
#Updated code based on Troels Emtekær Linnet and  Andreas Henschel
#to do #
###################################################################
import os
import pymol
from pymol import cmd
os.chdir('E:/PAPER/AlanineMutagenesis')
cmd.load("E:\V2R-ML\V2R INACTIVE WITH DUMMIES V2\V2R INACTIVE WITH DUMMIES V2\ClassA_v2r_human_Inactive_4BUO_2019-03-14_GPCRDB_B.pdb")

# 1.Get all loaded PDB object names in pymol
PDBs = cmd.get_names()

#2. We need to be able to get the chain and residue information
#a. Create empty list
ProtChainResiList = []
for PDB in PDBs:
    #print PDB
    ### Get the ID numbers of c-alpha (CA) atoms of all residues
    CAindex = cmd.identify("%s and name CA"%PDB)
    print(CAindex)
    for CAid in CAindex:
        #Using CA ID to get Chain and Residue information   
        pdbstr = cmd.get_pdbstr("%s and id %s"%(PDB,CAid))
        pdbstr_lines = pdbstr.splitlines()
        chain = pdbstr_lines[0].split()[4]
        resi = pdbstr_lines[0].split()[5]
        ProtChainResiList.append([PDB,chain,resi])
#b.check the output of the list
for output in ProtChainResiList:
    print (output)
#3.Divide PDBid,Chain, and Residue (p,c,r) present in list to do a proper selection for the PyMOL wizard.
for p,c,r in ProtChainResiList:
    cmd.wizard("mutagenesis")
    print(p,c,r)
    cmd.refresh_wizard()
    #Selection to which type of residue you want to change
    cmd.get_wizard().set_mode("ALA")
    ###############################################
    #Possible mutations for our project are :##################
    #cmd.get_wizard().set_mode('VAL') for ALA TO VAL###########
    ##cmd.get_wizard().set_mode('ALA') for any/not ALA to ALA##
    ##cmd.get_wizard().set_mode('GLY') for ALA to GLY##########
    #select each
    selection="/%s//%s/%s"%(p,c,r)
    #print selection to check the output
    print(selection)
    cmd.get_wizard().do_select(selection)
    cmd.get_wizard().apply()
    for PDB in PDBs:
        cmd.set_wizard("done")
        cmd.save((os.path.basename("E:\PAPER\AlanineMutagenesis\%s"%selection)+"-mutation.pdb"),"%s"%PDB)
        cmd.reinitialize('everything')
        cmd.load("E:\V2R-ML\V2R INACTIVE WITH DUMMIES V2\V2R INACTIVE WITH DUMMIES V2\ClassA_v2r_human_Inactive_4BUO_2019-03-14_GPCRDB_B.pdb")


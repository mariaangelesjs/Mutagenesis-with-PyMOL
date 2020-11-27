#!/usr/bin/python
#######################################################################################################
#Updated code based on Troels Emtekær Linnet's and  Andreas Henschel's mutagenesis scripts#############
#to do high-throughput mutagenesis on any protein (e.g. receptors of interest)#########################
#######################################################################################################

#Packages that you will need to install and import within python:
import os
import pymol
from pymol import cmd
import re 
################################################################################################################
#Definitions :##################################################################################################
#Directory = the path in your computer where you are working or from where you want to load or save your files.#
################################################################################################################

#1.Change where you want this code to run using os.chdir('directory').
def Mutagenesis(filename,mutation_type,start_mutation,finish_mutation):
    #2.Load your PDB file. Use V2R INACTIVE as an example or any pdb file. You can also 
    ##use cmd.fetch() to get an online pdb (search for the documentation typing 'pymol API' in Google).
    cmd.load(filename)
    #3.Get all loaded PDB object names in pymol
    PDBs = cmd.get_names()
    #4. We need to be able to get the chain and residue information
    ##a. Create empty list
    ProtChainResiList = []
    #2.Load your PDB file. Use V2R INACTIVE as an example or any pdb file. You can also
    #use cmd.fetch() to get an online pdb (search for the documentation typing 'pymol API' in Google).
    cmd.load("ClassA_v2r_human_Inactive_4BUO_2019-03-14_GPCRDB_B.pdb")
    #3.Get all loaded PDB object names in pymol
    PDBs = cmd.get_names()
    #4. We need to be able to get the chain and residue information
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
    #5.Divide PDBid,Chain, and Residue (p,c,r) present in list to do a proper selection for the PyMOL wizard.
    for p,c,r in ProtChainResiList:
        #If you want to select a range of residues you will have to add above,for example, ProtChainResiList[0:100] to select the
        ##first residue and the 100th one.
        cmd.wizard("mutagenesis")
        print(p,c,r)
        cmd.refresh_wizard()
        #Selection to which type of residue you want to change
        cmd.get_wizard().set_mode(mutation_type)
        ############################################################
        ##Possible mutation_type could be:##########################
        ##'VAL' for ALA TO VAL######################################
        ###'ALA' for any/not ALA to ALA#############################
        ###'GLY' for ALA to GLY#####################################
        ############################################################
        # #'selection' will select each residue that you have selected 
        # #on ProtChainResiList above using the PDBid,chain,and residue 
        # #present on your pdb file.If you didn't select a range on 
        # #ProteinChainResiList, it will do the mutation on all the residues
        #  #present in your protein.
        selection="/%s//%s/%s"%(p,c,r)
       #Print selection to check the output
        print(selection)
        i= 0
        for i,selection in zip(str(range(start,finish)),selection):
            #Selects where to place the mutation
            cmd.get_wizard().do_select(i)
            #Applies mutation
            cmd.get_wizard().apply()
            i+=1
        #Save each mutation and reinitialize the session before the next mutation
        ##to have pdb files only with the residue-specific single-point mutation you were
        ##interested.
        for PDB in PDBs:
            cmd.set_wizard("done")
           #Saving your mutated residue in a single pdb file. Use directory in
           ##os.path.basename("(directory)%s"%selection)to add where you want your pdb file
           ##to be saved. 
           ##This will save the residue-specific mutation with the respective file name according to
           ##mutation.
            cmd.save((os.path.basename("%s"%selection)+"-mutation.pdb"),"%s"%PDB)
           ##Reinitialize PyMOL to default settings.
            cmd.reinitialize('everything')
            #Load your original (non-mutated) PDB file.
            cmd.load(filename)

file = "ClassA_v2r_human_Inactive_4BUO_2019-03-14_GPCRDB_B.pdb"
Mutagenesis(file,'ALA',24,100)
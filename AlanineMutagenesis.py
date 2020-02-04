#!/usr/bin/python

import pymol
#start here if you are running this code in pymol
from pymol import cmd
cmd.load("4ENX.pdb")
cmd.wizard("mutagenesis")
cmd.refresh_wizard()
cmd.get_wizard().do_select(("res 1"))
cmd.get_wizard().set_mode('ALA')
cmd.get_wizard().apply()
cmd.set_wizard()
cmd.save('ALAMUT-4ENX.pdb')
reinitialize
#cmd.load("/PATH-TO-FILE/FILE.pdb")
#cmd.get_wizard().do_select(("res X")) X can be any residue present in the protein
#cmd.get_wizard().set_mode('VAL') for ALA TO VAL
#cmd.get_wizard().set_mode('ALA') for any/not ALA to ALA
#cmd.save('outfile.pdb')

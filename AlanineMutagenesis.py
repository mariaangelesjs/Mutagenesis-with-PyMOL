#run through pymol

from pymol import cmd
load 4ENX.pdb
cmd.wizard("mutagenesis")
cmd.refresh_wizard()
cmd.get_wizard().do_select(("res 1"))
cmd.get_wizard().set_mode('ALA')
cmd.get_wizard().apply()
cmd.set_wizard()
cmd.save('ALAMUT-4ENX.pdb')
reinitialize

#cmd.get_wizard().set_mode('VAL') for ALA TO VAL
#cmd.get_wizard().set_mode('ALA') for any/not ALA to ALA

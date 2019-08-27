## run through pymol

from pymol import cmd
load file.pdb
cmd.wizard("mutagenesis")
cmd.refresh_wizard()
cmd.get_wizard().do_select(("res 24"))
cmd.get_wizard().set_mode('ALA')
cmd.get_wizard().apply()
cmd.set_wizard()
cmd.save('file.pdb')
reinitialize

#cmd.get_wizard().set_mode('VAL') for ALA TO VAL
#cmd.get_wizard().set_mode('ALA') for any/not ALA to ALA

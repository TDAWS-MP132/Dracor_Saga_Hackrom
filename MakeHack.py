import os
import shutil as sh

# Directories
cwd = os.getcwd()
tables = cwd + "\\Tables"
spritans = cwd + "\\Spritans"
portraits = spritans + "\\Portraits"
classcards = spritans + "\\ClassCards"
mapsprites = spritans + "\\MapSprites"
icons = spritans + "\\Icons"
anims = spritans + "\\BattleAnimations"
palettes = spritans + "\\Palettes"
maps = cwd + "\\Maps\\tmx"
writans = cwd + "\\Writans"
wizardry = cwd + "\\Wizardry"
chax = wizardry + "\\CHAX"
sound = cwd + "\\Sound"

# Files
romclean = cwd + "\\FE8_Clean.gba"
romtarget = cwd + "\\Dracor_Saga.gba"
upstarget = cwd + "\\Dracor_Saga.ups"
symtarget = cwd + "\\Dracor_Saga.sym"
buildfile = cwd + "\\Buildfile.event"
chaxsrc = chax + "\\src.lyn.event"

# Tools
eacore = cwd + "\\EventAssembler\\ColorzCore.exe"
ups = cwd + "\\Tools\\ups\\ups.exe"
symcombo = cwd + "\\Tools\\SymCombo"
portraitformatter = cwd + "\\EventAssembler\\Tools\\PortraitFormatter.exe"
parsefile = cwd + "\\EventAssembler\\Tools\\ParseFile.exe"
parsedefs = writans + "\\ParseDefinitions.txt"
png2dmp = cwd + "\\EventAssembler\\Tools\\Png2Dmp.exe"
from Tools.TableBuilder import tablebuilder as tb
from Tools.BuildTools import buildtools as bt
from Tools.GraphicTools import portraittools as pt
from Tools.GraphicTools import mapspritetools as mst
from Tools.GraphicTools import icontools as it
from Tools.GraphicTools import animtools as at
from Tools.GraphicTools import palettetools as plt
from Tools.tmx2ea import tmx2ea as tmx
from Tools.TextProcess import textprocessclassic as tpc
from Tools.s2ea import s2ea

pt.compileportraits(portraits, portraitformatter, startindex = 0xAD, parsedefsdir = parsedefs)
pt.compileclasscards(classcards, png2dmp, startindex = 0x150)
mst.compilemapsprites(mapsprites, png2dmp, startindex = 0x6B)
it.compileicons(icons, png2dmp, startindex = 0xCA)
at.compileanimations(anims, startindex = 0xCA)
plt.compilepalettes(palettes, startindex = 0x1)
tpc.textprocess(writans, parsefile, parsedefs)
tb.rom2c(tables, romclean) 
tb.c2ea(tables, romclean)
tmx.runtmx2ea(maps)
s2ea.s2ea(sound, startindex = 1001)
#bt.make(chax, chaxsrc)

sh.copyfile(romclean, romtarget)
bt.callea(eacore, romtarget, buildfile)
bt.callups(ups, romclean, romtarget, upstarget)
bt.callsymcombo(symcombo, symtarget)

print("Fire Emblem Gaiden for the Nintendo Famicom Disk System")
input()

#import pygame
import ast
import time

from GameAssets import Water_Sea
from GameAssets import Water_Fluss
from GameAssets import Grass
from GameAssets import Bergwand
from GameAssets import Bergweg_Oben
from GameAssets import Zaun
from GameAssets import Tree
from GameAssets import Temple
from GameAssets import StatdtWeg
from GameAssets import Schild
from GameAssets import Sand
from GameAssets import QuestionMark
from GameAssets import questboard
from GameAssets import Palast_Wand_Top
from GameAssets import Palast_Wand
from GameAssets import Palast_Treppe
from GameAssets import Palast_Tor
from GameAssets import Palast
from GameAssets import House4
from GameAssets import House3
from GameAssets import House2
from GameAssets import House1
from GameAssets import Höhleneingang
from GameAssets import fountain
from GameAssets import Firtree
from GameAssets import Exclamation_Mark
from GameAssets import Durchsichtig
from GameAssets import Dummy
from GameAssets import Door4
from GameAssets import Door3
from GameAssets import Door2
from GameAssets import Door1
from GameAssets import Dirt_Weg
from GameAssets import Brucke 
from GameAssets import Bergweg_Zenter
from GameAssets import Bergweg_unten
from GameAssets import Stein
from GameAssets import Altar
from GameAssets import Fackel
from GameAssets import Schwarzes_Rechteck
from GameAssets import Haus_innen_Wand_Ecke_links_unten_Final
from GameAssets import Haus_innen_Wand_Ecke_links_oben_Final
from GameAssets import Haus_innen_Wand_Ecke_rechts_oben_Final
from GameAssets import Haus_innen_Wand_Ecke_recht_unten_Final
from GameAssets import Haus_innen_Wand_links_Final
from GameAssets import Haus_innen_Wand_oben_FInal
from GameAssets import Haus_innen_Wand_rechts_Final
from GameAssets import Haus_innen_Wand_unten_Final
from GameAssets import Haus_Wand_Visible__Front__Final
from GameAssets import Palast_Boden
from GameAssets import Palast_Wand_Ecke_Links_Oben
from GameAssets import Palast_Wand_Ecke_Links_Unten
from GameAssets import Palast_Wand_Ecke_Rechts_Oben
from GameAssets import Palast_Wand_Ecke_Rechts_Unten
from GameAssets import Palast_Wand_Front_Rest
from GameAssets import Palast_Wand_Front_Verbindung_Zum_Boden
from GameAssets import Palast_Wand_Links
from GameAssets import Palast_Wand_Oben
from GameAssets import Palast_Wand_Rechts
from GameAssets import Palast_Wand_unten
from GameAssets import Regal_Final_
from GameAssets import Stuhl_Final_links_schauend
from GameAssets import Stuhl_Final_rechts_schauend
from GameAssets import Tempel_Boden
from GameAssets import Tempel_Wand_Ecke_Links_Oben
from GameAssets import Tempel_Wand_Ecke_Links_Unten
from GameAssets import Tempel_Wand_Ecke_Rechts_Oben
from GameAssets import Tempel_Wand_Ecke_Rechts_Unten
from GameAssets import Tempel_Wand_Front_Rest
from GameAssets import Tempel_Wand_Front_Verbindung_Zum_Boden
from GameAssets import Tempel_Wand_Links
from GameAssets import Tempel_Wand_Oben

from GameAssets import Tempel_Wand_Rechts
from GameAssets import Tempel_Wand_Unten
from GameAssets import Tisch_Final
from GameAssets import Schwarzes_Rechteck

from GameAssets import cave_bottommiddle
from GameAssets import Cave_floor
from GameAssets import cave_leftwall
from GameAssets import cave_rightwall
from GameAssets import cave_topmiddle




class gameworld(object):
    def __init__(self):
        
        self.start = time.time()

        self.chunk0_0 = ast.literal_eval(open("Chunks/chunk0_0.txt").read())
        self.chunk0_1 = ast.literal_eval(open("Chunks/chunk0_1.txt").read())
        self.chunk0_2 = ast.literal_eval(open("Chunks/chunk0_2.txt").read())
        self.chunk0_3 = ast.literal_eval(open("Chunks/chunk0_3.txt").read())
        self.chunk0_4 = ast.literal_eval(open("Chunks/chunk0_4.txt").read())
        self.chunk0_5 = ast.literal_eval(open("Chunks/chunk0_5.txt").read())
        self.chunk0_6 = ast.literal_eval(open("Chunks/chunk0_6.txt").read())
        self.chunk0_7 = ast.literal_eval(open("Chunks/chunk0_7.txt").read())
        self.chunk0_8 = ast.literal_eval(open("Chunks/chunk0_8.txt").read())
        self.chunk0_9 = ast.literal_eval(open("Chunks/chunk0_9.txt").read())
        self.chunk0_10 = ast.literal_eval(open("Chunks/chunk0_10.txt").read())
        self.chunk0_11 = ast.literal_eval(open("Chunks/chunk0_11.txt").read())
        self.chunk0_12 = ast.literal_eval(open("Chunks/chunk0_12.txt").read())
        self.chunk0_13 = ast.literal_eval(open("Chunks/chunk0_13.txt").read())
        self.chunk0_14 = ast.literal_eval(open("Chunks/chunk0_14.txt").read())
        self.chunk0_15 = ast.literal_eval(open("Chunks/chunk0_15.txt").read())
        self.chunk0_16 = ast.literal_eval(open("Chunks/chunk0_16.txt").read())
        self.chunk0_17 = ast.literal_eval(open("Chunks/chunk0_17.txt").read())
        self.chunk0_18 = ast.literal_eval(open("Chunks/chunk0_18.txt").read())
        self.chunk0_19 = ast.literal_eval(open("Chunks/chunk0_19.txt").read())
        self.chunk0_20 = ast.literal_eval(open("Chunks/chunk0_20.txt").read())
        self.chunk0_21 = ast.literal_eval(open("Chunks/chunk0_21.txt").read())

        self.chunk1_0 = ast.literal_eval(open("Chunks/chunk1_0.txt").read())
        self.chunk1_1 = ast.literal_eval(open("Chunks/chunk1_1.txt").read())
        self.chunk1_2 = ast.literal_eval(open("Chunks/chunk1_2.txt").read())
        self.chunk1_3 = ast.literal_eval(open("Chunks/chunk1_3.txt").read())
        self.chunk1_4 = ast.literal_eval(open("Chunks/chunk1_4.txt").read())
        self.chunk1_5 = ast.literal_eval(open("Chunks/chunk1_5.txt").read())
        self.chunk1_6 = ast.literal_eval(open("Chunks/chunk1_6.txt").read())
        self.chunk1_7 = ast.literal_eval(open("Chunks/chunk1_7.txt").read())
        self.chunk1_8 = ast.literal_eval(open("Chunks/chunk1_8.txt").read())
        self.chunk1_9 = ast.literal_eval(open("Chunks/chunk1_9.txt").read())
        self.chunk1_10 = ast.literal_eval(open("Chunks/chunk1_10.txt").read())
        self.chunk1_11 = ast.literal_eval(open("Chunks/chunk1_11.txt").read())
        self.chunk1_12 = ast.literal_eval(open("Chunks/chunk1_12.txt").read())
        self.chunk1_13 = ast.literal_eval(open("Chunks/chunk1_13.txt").read())
        self.chunk1_14 = ast.literal_eval(open("Chunks/chunk1_14.txt").read())
        self.chunk1_15 = ast.literal_eval(open("Chunks/chunk1_15.txt").read())
        self.chunk1_16 = ast.literal_eval(open("Chunks/chunk1_16.txt").read())
        self.chunk1_17 = ast.literal_eval(open("Chunks/chunk1_17.txt").read())
        self.chunk1_18 = ast.literal_eval(open("Chunks/chunk1_18.txt").read())
        self.chunk1_19 = ast.literal_eval(open("Chunks/chunk1_19.txt").read())
        self.chunk1_20 = ast.literal_eval(open("Chunks/chunk1_20.txt").read())
        self.chunk1_21 = ast.literal_eval(open("Chunks/chunk1_21.txt").read())

        self.chunk2_0 = ast.literal_eval(open("Chunks/chunk2_0.txt").read())
        self.chunk2_1 = ast.literal_eval(open("Chunks/chunk2_1.txt").read())
        self.chunk2_2 = ast.literal_eval(open("Chunks/chunk2_2.txt").read())
        self.chunk2_3 = ast.literal_eval(open("Chunks/chunk2_3.txt").read())
        self.chunk2_4 = ast.literal_eval(open("Chunks/chunk2_4.txt").read())
        self.chunk2_5 = ast.literal_eval(open("Chunks/chunk2_5.txt").read())
        self.chunk2_6 = ast.literal_eval(open("Chunks/chunk2_6.txt").read())
        self.chunk2_7 = ast.literal_eval(open("Chunks/chunk2_7.txt").read())
        self.chunk2_8 = ast.literal_eval(open("Chunks/chunk2_8.txt").read())
        self.chunk2_9 = ast.literal_eval(open("Chunks/chunk2_9.txt").read())
        self.chunk2_10 = ast.literal_eval(open("Chunks/chunk2_10.txt").read())
        self.chunk2_11 = ast.literal_eval(open("Chunks/chunk2_11.txt").read())
        self.chunk2_12 = ast.literal_eval(open("Chunks/chunk2_12.txt").read())
        self.chunk2_13 = ast.literal_eval(open("Chunks/chunk2_13.txt").read())
        self.chunk2_14 = ast.literal_eval(open("Chunks/chunk2_14.txt").read())
        self.chunk2_15 = ast.literal_eval(open("Chunks/chunk2_15.txt").read())
        self.chunk2_16 = ast.literal_eval(open("Chunks/chunk2_16.txt").read())
        self.chunk2_17 = ast.literal_eval(open("Chunks/chunk2_17.txt").read())
        self.chunk2_18 = ast.literal_eval(open("Chunks/chunk2_18.txt").read())
        self.chunk2_19 = ast.literal_eval(open("Chunks/chunk2_19.txt").read())
        self.chunk2_20 = ast.literal_eval(open("Chunks/chunk2_20.txt").read())
        self.chunk2_21 = ast.literal_eval(open("Chunks/chunk2_21.txt").read())

        self.chunk3_0 = ast.literal_eval(open("Chunks/chunk3_0.txt").read())
        self.chunk3_1 = ast.literal_eval(open("Chunks/chunk3_1.txt").read())
        self.chunk3_2 = ast.literal_eval(open("Chunks/chunk3_2.txt").read())
        self.chunk3_3 = ast.literal_eval(open("Chunks/chunk3_3.txt").read())
        self.chunk3_4 = ast.literal_eval(open("Chunks/chunk3_4.txt").read())
        self.chunk3_5 = ast.literal_eval(open("Chunks/chunk3_5.txt").read())
        self.chunk3_6 = ast.literal_eval(open("Chunks/chunk3_6.txt").read())
        self.chunk3_7 = ast.literal_eval(open("Chunks/chunk3_7.txt").read())
        self.chunk3_8 = ast.literal_eval(open("Chunks/chunk3_8.txt").read())
        self.chunk3_9 = ast.literal_eval(open("Chunks/chunk3_9.txt").read())
        self.chunk3_10 = ast.literal_eval(open("Chunks/chunk3_10.txt").read())
        self.chunk3_11 = ast.literal_eval(open("Chunks/chunk3_11.txt").read())
        self.chunk3_12 = ast.literal_eval(open("Chunks/chunk3_12.txt").read())
        self.chunk3_13 = ast.literal_eval(open("Chunks/chunk3_13.txt").read())
        self.chunk3_14 = ast.literal_eval(open("Chunks/chunk3_14.txt").read())
        self.chunk3_15 = ast.literal_eval(open("Chunks/chunk3_15.txt").read())
        self.chunk3_16 = ast.literal_eval(open("Chunks/chunk3_16.txt").read())
        self.chunk3_17 = ast.literal_eval(open("Chunks/chunk3_17.txt").read())
        self.chunk3_18 = ast.literal_eval(open("Chunks/chunk3_18.txt").read())
        self.chunk3_19 = ast.literal_eval(open("Chunks/chunk3_19.txt").read())
        self.chunk3_20 = ast.literal_eval(open("Chunks/chunk3_20.txt").read())
        self.chunk3_21 = ast.literal_eval(open("Chunks/chunk3_21.txt").read())

        self.chunk4_0 = ast.literal_eval(open("Chunks/chunk4_0.txt").read())
        self.chunk4_1 = ast.literal_eval(open("Chunks/chunk4_1.txt").read())
        self.chunk4_2 = ast.literal_eval(open("Chunks/chunk4_2.txt").read())
        self.chunk4_3 = ast.literal_eval(open("Chunks/chunk4_3.txt").read())
        self.chunk4_4 = ast.literal_eval(open("Chunks/chunk4_4.txt").read())
        self.chunk4_5 = ast.literal_eval(open("Chunks/chunk4_5.txt").read())
        self.chunk4_6 = ast.literal_eval(open("Chunks/chunk4_6.txt").read())
        self.chunk4_7 = ast.literal_eval(open("Chunks/chunk4_7.txt").read())
        self.chunk4_8 = ast.literal_eval(open("Chunks/chunk4_8.txt").read())
        self.chunk4_9 = ast.literal_eval(open("Chunks/chunk4_9.txt").read())
        self.chunk4_10 = ast.literal_eval(open("Chunks/chunk4_10.txt").read())
        self.chunk4_11 = ast.literal_eval(open("Chunks/chunk4_11.txt").read())
        self.chunk4_12 = ast.literal_eval(open("Chunks/chunk4_12.txt").read())
        self.chunk4_13 = ast.literal_eval(open("Chunks/chunk4_13.txt").read())
        self.chunk4_14 = ast.literal_eval(open("Chunks/chunk4_14.txt").read())
        self.chunk4_15 = ast.literal_eval(open("Chunks/chunk4_15.txt").read())
        self.chunk4_16 = ast.literal_eval(open("Chunks/chunk4_16.txt").read())
        self.chunk4_17 = ast.literal_eval(open("Chunks/chunk4_17.txt").read())
        self.chunk4_18 = ast.literal_eval(open("Chunks/chunk4_18.txt").read())
        self.chunk4_19 = ast.literal_eval(open("Chunks/chunk4_19.txt").read())
        self.chunk4_20 = ast.literal_eval(open("Chunks/chunk4_20.txt").read())
        self.chunk4_21 = ast.literal_eval(open("Chunks/chunk4_21.txt").read())
        
        self.chunk5_0 = ast.literal_eval(open("Chunks/chunk5_0.txt").read())
        self.chunk5_1 = ast.literal_eval(open("Chunks/chunk5_1.txt").read())
        self.chunk5_2 = ast.literal_eval(open("Chunks/chunk5_2.txt").read())
        self.chunk5_3 = ast.literal_eval(open("Chunks/chunk5_3.txt").read())
        self.chunk5_4 = ast.literal_eval(open("Chunks/chunk5_4.txt").read())
        self.chunk5_5 = ast.literal_eval(open("Chunks/chunk5_5.txt").read())
        self.chunk5_6 = ast.literal_eval(open("Chunks/chunk5_6.txt").read())
        self.chunk5_7 = ast.literal_eval(open("Chunks/chunk5_7.txt").read())
        self.chunk5_8 = ast.literal_eval(open("Chunks/chunk5_8.txt").read())
        self.chunk5_9 = ast.literal_eval(open("Chunks/chunk5_9.txt").read())
        self.chunk5_10 = ast.literal_eval(open("Chunks/chunk5_10.txt").read())
        self.chunk5_11 = ast.literal_eval(open("Chunks/chunk5_11.txt").read())
        self.chunk5_12 = ast.literal_eval(open("Chunks/chunk5_12.txt").read())
        self.chunk5_13 = ast.literal_eval(open("Chunks/chunk5_13.txt").read())
        self.chunk5_14 = ast.literal_eval(open("Chunks/chunk5_14.txt").read())
        self.chunk5_15 = ast.literal_eval(open("Chunks/chunk5_15.txt").read())
        self.chunk5_16 = ast.literal_eval(open("Chunks/chunk5_16.txt").read())
        self.chunk5_17 = ast.literal_eval(open("Chunks/chunk5_17.txt").read())
        self.chunk5_18 = ast.literal_eval(open("Chunks/chunk5_18.txt").read())
        self.chunk5_19 = ast.literal_eval(open("Chunks/chunk5_19.txt").read())
        self.chunk5_20 = ast.literal_eval(open("Chunks/chunk5_20.txt").read())
        self.chunk5_21 = ast.literal_eval(open("Chunks/chunk5_21.txt").read())

        self.chunk6_0 = ast.literal_eval(open("Chunks/chunk6_0.txt").read())
        self.chunk6_1 = ast.literal_eval(open("Chunks/chunk6_1.txt").read())
        self.chunk6_2 = ast.literal_eval(open("Chunks/chunk6_2.txt").read())
        self.chunk6_3 = ast.literal_eval(open("Chunks/chunk6_3.txt").read())
        self.chunk6_4 = ast.literal_eval(open("Chunks/chunk6_4.txt").read())
        self.chunk6_5 = ast.literal_eval(open("Chunks/chunk6_5.txt").read())
        self.chunk6_6 = ast.literal_eval(open("Chunks/chunk6_6.txt").read())
        self.chunk6_7 = ast.literal_eval(open("Chunks/chunk6_7.txt").read())
        self.chunk6_8 = ast.literal_eval(open("Chunks/chunk6_8.txt").read())
        self.chunk6_9 = ast.literal_eval(open("Chunks/chunk6_9.txt").read())
        self.chunk6_10 = ast.literal_eval(open("Chunks/chunk6_10.txt").read())
        self.chunk6_11 = ast.literal_eval(open("Chunks/chunk6_11.txt").read())
        self.chunk6_12 = ast.literal_eval(open("Chunks/chunk6_12.txt").read())
        self.chunk6_13 = ast.literal_eval(open("Chunks/chunk6_13.txt").read())
        self.chunk6_14 = ast.literal_eval(open("Chunks/chunk6_14.txt").read())
        self.chunk6_15 = ast.literal_eval(open("Chunks/chunk6_15.txt").read())
        self.chunk6_16 = ast.literal_eval(open("Chunks/chunk6_16.txt").read())
        self.chunk6_17 = ast.literal_eval(open("Chunks/chunk6_17.txt").read())
        self.chunk6_18 = ast.literal_eval(open("Chunks/chunk6_18.txt").read())
        self.chunk6_19 = ast.literal_eval(open("Chunks/chunk6_19.txt").read())
        self.chunk6_20 = ast.literal_eval(open("Chunks/chunk6_20.txt").read())
        self.chunk6_21 = ast.literal_eval(open("Chunks/chunk6_21.txt").read())

        self.chunk7_0 = ast.literal_eval(open("Chunks/chunk7_0.txt").read())
        self.chunk7_1 = ast.literal_eval(open("Chunks/chunk7_1.txt").read())
        self.chunk7_2 = ast.literal_eval(open("Chunks/chunk7_2.txt").read())
        self.chunk7_3 = ast.literal_eval(open("Chunks/chunk7_3.txt").read())
        self.chunk7_4 = ast.literal_eval(open("Chunks/chunk7_4.txt").read())
        self.chunk7_5 = ast.literal_eval(open("Chunks/chunk7_5.txt").read())
        self.chunk7_6 = ast.literal_eval(open("Chunks/chunk7_6.txt").read())
        self.chunk7_7 = ast.literal_eval(open("Chunks/chunk7_7.txt").read())
        self.chunk7_8 = ast.literal_eval(open("Chunks/chunk7_8.txt").read())
        self.chunk7_9 = ast.literal_eval(open("Chunks/chunk7_9.txt").read())
        self.chunk7_10 = ast.literal_eval(open("Chunks/chunk7_10.txt").read())
        self.chunk7_11 = ast.literal_eval(open("Chunks/chunk7_11.txt").read())
        self.chunk7_12 = ast.literal_eval(open("Chunks/chunk7_12.txt").read())
        self.chunk7_13 = ast.literal_eval(open("Chunks/chunk7_13.txt").read())
        self.chunk7_14 = ast.literal_eval(open("Chunks/chunk7_14.txt").read())
        self.chunk7_15 = ast.literal_eval(open("Chunks/chunk7_15.txt").read())
        self.chunk7_16 = ast.literal_eval(open("Chunks/chunk7_16.txt").read())
        self.chunk7_17 = ast.literal_eval(open("Chunks/chunk7_17.txt").read())
        self.chunk7_18 = ast.literal_eval(open("Chunks/chunk7_18.txt").read())
        self.chunk7_19 = ast.literal_eval(open("Chunks/chunk7_19.txt").read())
        self.chunk7_20 = ast.literal_eval(open("Chunks/chunk7_20.txt").read())
        self.chunk7_21 = ast.literal_eval(open("Chunks/chunk7_21.txt").read())

        self.chunk8_0 = ast.literal_eval(open("Chunks/chunk8_0.txt").read())
        self.chunk8_1 = ast.literal_eval(open("Chunks/chunk8_1.txt").read())
        self.chunk8_2 = ast.literal_eval(open("Chunks/chunk8_2.txt").read())
        self.chunk8_3 = ast.literal_eval(open("Chunks/chunk8_3.txt").read())
        self.chunk8_4 = ast.literal_eval(open("Chunks/chunk8_4.txt").read())
        self.chunk8_5 = ast.literal_eval(open("Chunks/chunk8_5.txt").read())
        self.chunk8_6 = ast.literal_eval(open("Chunks/chunk8_6.txt").read())
        self.chunk8_7 = ast.literal_eval(open("Chunks/chunk8_7.txt").read())
        self.chunk8_8 = ast.literal_eval(open("Chunks/chunk8_8.txt").read())
        self.chunk8_9 = ast.literal_eval(open("Chunks/chunk8_9.txt").read())
        self.chunk8_10 = ast.literal_eval(open("Chunks/chunk8_10.txt").read())
        self.chunk8_11 = ast.literal_eval(open("Chunks/chunk8_11.txt").read())
        self.chunk8_12 = ast.literal_eval(open("Chunks/chunk8_12.txt").read())
        self.chunk8_13 = ast.literal_eval(open("Chunks/chunk8_13.txt").read())
        self.chunk8_14 = ast.literal_eval(open("Chunks/chunk8_14.txt").read())
        self.chunk8_15 = ast.literal_eval(open("Chunks/chunk8_15.txt").read())
        self.chunk8_16 = ast.literal_eval(open("Chunks/chunk8_16.txt").read())
        self.chunk8_17 = ast.literal_eval(open("Chunks/chunk8_17.txt").read())
        self.chunk8_18 = ast.literal_eval(open("Chunks/chunk8_18.txt").read())
        self.chunk8_19 = ast.literal_eval(open("Chunks/chunk8_19.txt").read())
        self.chunk8_20 = ast.literal_eval(open("Chunks/chunk8_20.txt").read())
        self.chunk8_21 = ast.literal_eval(open("Chunks/chunk8_21.txt").read())

        self.chunk9_0 = ast.literal_eval(open("Chunks/chunk9_0.txt").read())
        self.chunk9_1 = ast.literal_eval(open("Chunks/chunk9_1.txt").read())
        self.chunk9_2 = ast.literal_eval(open("Chunks/chunk9_2.txt").read())
        self.chunk9_3 = ast.literal_eval(open("Chunks/chunk9_3.txt").read())
        self.chunk9_4 = ast.literal_eval(open("Chunks/chunk9_4.txt").read())
        self.chunk9_5 = ast.literal_eval(open("Chunks/chunk9_5.txt").read())
        self.chunk9_6 = ast.literal_eval(open("Chunks/chunk9_6.txt").read())
        self.chunk9_7 = ast.literal_eval(open("Chunks/chunk9_7.txt").read())
        self.chunk9_8 = ast.literal_eval(open("Chunks/chunk9_8.txt").read())
        self.chunk9_9 = ast.literal_eval(open("Chunks/chunk9_9.txt").read())
        self.chunk9_10 = ast.literal_eval(open("Chunks/chunk9_10.txt").read())
        self.chunk9_11 = ast.literal_eval(open("Chunks/chunk9_11.txt").read())
        self.chunk9_12 = ast.literal_eval(open("Chunks/chunk9_12.txt").read())
        self.chunk9_13 = ast.literal_eval(open("Chunks/chunk9_13.txt").read())
        self.chunk9_14 = ast.literal_eval(open("Chunks/chunk9_14.txt").read())
        self.chunk9_15 = ast.literal_eval(open("Chunks/chunk9_15.txt").read())
        self.chunk9_16 = ast.literal_eval(open("Chunks/chunk9_16.txt").read())
        self.chunk9_17 = ast.literal_eval(open("Chunks/chunk9_17.txt").read())
        self.chunk9_18 = ast.literal_eval(open("Chunks/chunk9_18.txt").read())
        self.chunk9_19 = ast.literal_eval(open("Chunks/chunk9_19.txt").read())
        self.chunk9_20 = ast.literal_eval(open("Chunks/chunk9_20.txt").read())
        self.chunk9_21 = ast.literal_eval(open("Chunks/chunk9_21.txt").read())

        self.chunk10_0 = ast.literal_eval(open("Chunks/chunk10_0.txt").read())
        self.chunk10_1 = ast.literal_eval(open("Chunks/chunk10_1.txt").read())
        self.chunk10_2 = ast.literal_eval(open("Chunks/chunk10_2.txt").read())
        self.chunk10_3 = ast.literal_eval(open("Chunks/chunk10_3.txt").read())
        self.chunk10_4 = ast.literal_eval(open("Chunks/chunk10_4.txt").read())
        self.chunk10_5 = ast.literal_eval(open("Chunks/chunk10_5.txt").read())
        self.chunk10_6 = ast.literal_eval(open("Chunks/chunk10_6.txt").read())
        self.chunk10_7 = ast.literal_eval(open("Chunks/chunk10_7.txt").read())
        self.chunk10_8 = ast.literal_eval(open("Chunks/chunk10_8.txt").read())
        self.chunk10_9 = ast.literal_eval(open("Chunks/chunk10_9.txt").read())
        self.chunk10_10 = ast.literal_eval(open("Chunks/chunk10_10.txt").read())
        self.chunk10_11 = ast.literal_eval(open("Chunks/chunk10_11.txt").read())
        self.chunk10_12 = ast.literal_eval(open("Chunks/chunk10_12.txt").read())
        self.chunk10_13 = ast.literal_eval(open("Chunks/chunk10_13.txt").read())
        self.chunk10_14 = ast.literal_eval(open("Chunks/chunk10_14.txt").read())
        self.chunk10_15 = ast.literal_eval(open("Chunks/chunk10_15.txt").read())
        self.chunk10_16 = ast.literal_eval(open("Chunks/chunk10_16.txt").read())
        self.chunk10_17 = ast.literal_eval(open("Chunks/chunk10_17.txt").read())
        self.chunk10_18 = ast.literal_eval(open("Chunks/chunk10_18.txt").read())
        self.chunk10_19 = ast.literal_eval(open("Chunks/chunk10_19.txt").read())
        self.chunk10_20 = ast.literal_eval(open("Chunks/chunk10_20.txt").read())
        self.chunk10_21 = ast.literal_eval(open("Chunks/chunk10_21.txt").read())

        self.chunk11_0 = ast.literal_eval(open("Chunks/chunk11_0.txt").read())
        self.chunk11_1 = ast.literal_eval(open("Chunks/chunk11_1.txt").read())
        self.chunk11_2 = ast.literal_eval(open("Chunks/chunk11_2.txt").read())
        self.chunk11_3 = ast.literal_eval(open("Chunks/chunk11_3.txt").read())
        self.chunk11_4 = ast.literal_eval(open("Chunks/chunk11_4.txt").read())
        self.chunk11_5 = ast.literal_eval(open("Chunks/chunk11_5.txt").read())
        self.chunk11_6 = ast.literal_eval(open("Chunks/chunk11_6.txt").read())
        self.chunk11_7 = ast.literal_eval(open("Chunks/chunk11_7.txt").read())
        self.chunk11_8 = ast.literal_eval(open("Chunks/chunk11_8.txt").read())
        self.chunk11_9 = ast.literal_eval(open("Chunks/chunk11_9.txt").read())
        self.chunk11_10 = ast.literal_eval(open("Chunks/chunk11_10.txt").read())
        self.chunk11_11 = ast.literal_eval(open("Chunks/chunk11_11.txt").read())
        self.chunk11_12 = ast.literal_eval(open("Chunks/chunk11_12.txt").read())
        self.chunk11_13 = ast.literal_eval(open("Chunks/chunk11_13.txt").read())
        self.chunk11_14 = ast.literal_eval(open("Chunks/chunk11_14.txt").read())
        self.chunk11_15 = ast.literal_eval(open("Chunks/chunk11_15.txt").read())
        self.chunk11_16 = ast.literal_eval(open("Chunks/chunk11_16.txt").read())
        self.chunk11_17 = ast.literal_eval(open("Chunks/chunk11_17.txt").read())
        self.chunk11_18 = ast.literal_eval(open("Chunks/chunk11_18.txt").read())
        self.chunk11_19 = ast.literal_eval(open("Chunks/chunk11_19.txt").read())
        self.chunk11_20 = ast.literal_eval(open("Chunks/chunk11_20.txt").read())
        self.chunk11_21 = ast.literal_eval(open("Chunks/chunk11_21.txt").read())

        self.chunk12_0 = ast.literal_eval(open("Chunks/chunk12_0.txt").read())
        self.chunk12_1 = ast.literal_eval(open("Chunks/chunk12_1.txt").read())
        self.chunk12_2 = ast.literal_eval(open("Chunks/chunk12_2.txt").read())
        self.chunk12_3 = ast.literal_eval(open("Chunks/chunk12_3.txt").read())
        self.chunk12_4 = ast.literal_eval(open("Chunks/chunk12_4.txt").read())
        self.chunk12_5 = ast.literal_eval(open("Chunks/chunk12_5.txt").read())
        self.chunk12_6 = ast.literal_eval(open("Chunks/chunk12_6.txt").read())
        self.chunk12_7 = ast.literal_eval(open("Chunks/chunk12_7.txt").read())
        self.chunk12_8 = ast.literal_eval(open("Chunks/chunk12_8.txt").read())
        self.chunk12_9 = ast.literal_eval(open("Chunks/chunk12_9.txt").read())
        self.chunk12_10 = ast.literal_eval(open("Chunks/chunk12_10.txt").read())
        self.chunk12_11 = ast.literal_eval(open("Chunks/chunk12_11.txt").read())
        self.chunk12_12 = ast.literal_eval(open("Chunks/chunk12_12.txt").read())
        self.chunk12_13 = ast.literal_eval(open("Chunks/chunk12_13.txt").read())
        self.chunk12_14 = ast.literal_eval(open("Chunks/chunk12_14.txt").read())
        self.chunk12_15 = ast.literal_eval(open("Chunks/chunk12_15.txt").read())
        self.chunk12_16 = ast.literal_eval(open("Chunks/chunk12_16.txt").read())
        self.chunk12_17 = ast.literal_eval(open("Chunks/chunk12_17.txt").read())
        self.chunk12_18 = ast.literal_eval(open("Chunks/chunk12_18.txt").read())
        self.chunk12_19 = ast.literal_eval(open("Chunks/chunk12_19.txt").read())
        self.chunk12_20 = ast.literal_eval(open("Chunks/chunk12_20.txt").read())
        self.chunk12_21 = ast.literal_eval(open("Chunks/chunk12_21.txt").read())

        self.chunk13_0 = ast.literal_eval(open("Chunks/chunk13_0.txt").read())
        self.chunk13_1 = ast.literal_eval(open("Chunks/chunk13_1.txt").read())
        self.chunk13_2 = ast.literal_eval(open("Chunks/chunk13_2.txt").read())
        self.chunk13_3 = ast.literal_eval(open("Chunks/chunk13_3.txt").read())
        self.chunk13_4 = ast.literal_eval(open("Chunks/chunk13_4.txt").read())
        self.chunk13_5 = ast.literal_eval(open("Chunks/chunk13_5.txt").read())
        self.chunk13_6 = ast.literal_eval(open("Chunks/chunk13_6.txt").read())
        self.chunk13_7 = ast.literal_eval(open("Chunks/chunk13_7.txt").read())
        self.chunk13_8 = ast.literal_eval(open("Chunks/chunk13_8.txt").read())
        self.chunk13_9 = ast.literal_eval(open("Chunks/chunk13_9.txt").read())
        self.chunk13_10 = ast.literal_eval(open("Chunks/chunk13_10.txt").read())
        self.chunk13_11 = ast.literal_eval(open("Chunks/chunk13_11.txt").read())
        self.chunk13_12 = ast.literal_eval(open("Chunks/chunk13_12.txt").read())
        self.chunk13_13 = ast.literal_eval(open("Chunks/chunk13_13.txt").read())
        self.chunk13_14 = ast.literal_eval(open("Chunks/chunk13_14.txt").read())
        self.chunk13_15 = ast.literal_eval(open("Chunks/chunk13_15.txt").read())
        self.chunk13_16 = ast.literal_eval(open("Chunks/chunk13_16.txt").read())
        self.chunk13_17 = ast.literal_eval(open("Chunks/chunk13_17.txt").read())
        self.chunk13_18 = ast.literal_eval(open("Chunks/chunk13_18.txt").read())
        self.chunk13_19 = ast.literal_eval(open("Chunks/chunk13_19.txt").read())
        self.chunk13_20 = ast.literal_eval(open("Chunks/chunk13_20.txt").read())
        self.chunk13_21 = ast.literal_eval(open("Chunks/chunk13_21.txt").read())

        self.chunk14_0 = ast.literal_eval(open("Chunks/chunk14_0.txt").read())
        self.chunk14_1 = ast.literal_eval(open("Chunks/chunk14_1.txt").read())
        self.chunk14_2 = ast.literal_eval(open("Chunks/chunk14_2.txt").read())
        self.chunk14_3 = ast.literal_eval(open("Chunks/chunk14_3.txt").read())
        self.chunk14_4 = ast.literal_eval(open("Chunks/chunk14_4.txt").read())
        self.chunk14_5 = ast.literal_eval(open("Chunks/chunk14_5.txt").read())
        self.chunk14_6 = ast.literal_eval(open("Chunks/chunk14_6.txt").read())
        self.chunk14_7 = ast.literal_eval(open("Chunks/chunk14_7.txt").read())
        self.chunk14_8 = ast.literal_eval(open("Chunks/chunk14_8.txt").read())
        self.chunk14_9 = ast.literal_eval(open("Chunks/chunk14_9.txt").read())
        self.chunk14_10 = ast.literal_eval(open("Chunks/chunk14_10.txt").read())
        self.chunk14_11 = ast.literal_eval(open("Chunks/chunk14_11.txt").read())
        self.chunk14_12 = ast.literal_eval(open("Chunks/chunk14_12.txt").read())
        self.chunk14_13 = ast.literal_eval(open("Chunks/chunk14_13.txt").read())
        self.chunk14_14 = ast.literal_eval(open("Chunks/chunk14_14.txt").read())
        self.chunk14_15 = ast.literal_eval(open("Chunks/chunk14_15.txt").read())
        self.chunk14_16 = ast.literal_eval(open("Chunks/chunk14_16.txt").read())
        self.chunk14_17 = ast.literal_eval(open("Chunks/chunk14_17.txt").read())
        self.chunk14_18 = ast.literal_eval(open("Chunks/chunk14_18.txt").read())
        self.chunk14_19 = ast.literal_eval(open("Chunks/chunk14_19.txt").read())
        self.chunk14_20 = ast.literal_eval(open("Chunks/chunk14_20.txt").read())
        self.chunk14_21 = ast.literal_eval(open("Chunks/chunk14_21.txt").read())

        self.chunk15_0 = ast.literal_eval(open("Chunks/chunk15_0.txt").read())
        self.chunk15_1 = ast.literal_eval(open("Chunks/chunk15_1.txt").read())
        self.chunk15_2 = ast.literal_eval(open("Chunks/chunk15_2.txt").read())
        self.chunk15_3 = ast.literal_eval(open("Chunks/chunk15_3.txt").read())
        self.chunk15_4 = ast.literal_eval(open("Chunks/chunk15_4.txt").read())
        self.chunk15_5 = ast.literal_eval(open("Chunks/chunk15_5.txt").read())
        self.chunk15_6 = ast.literal_eval(open("Chunks/chunk15_6.txt").read())
        self.chunk15_7 = ast.literal_eval(open("Chunks/chunk15_7.txt").read())
        self.chunk15_8 = ast.literal_eval(open("Chunks/chunk15_8.txt").read())
        self.chunk15_9 = ast.literal_eval(open("Chunks/chunk15_9.txt").read())
        self.chunk15_10 = ast.literal_eval(open("Chunks/chunk15_10.txt").read())
        self.chunk15_11 = ast.literal_eval(open("Chunks/chunk15_11.txt").read())
        self.chunk15_12 = ast.literal_eval(open("Chunks/chunk15_12.txt").read())
        self.chunk15_13 = ast.literal_eval(open("Chunks/chunk15_13.txt").read())
        self.chunk15_14 = ast.literal_eval(open("Chunks/chunk15_14.txt").read())
        self.chunk15_15 = ast.literal_eval(open("Chunks/chunk15_15.txt").read())
        self.chunk15_16 = ast.literal_eval(open("Chunks/chunk15_16.txt").read())
        self.chunk15_17 = ast.literal_eval(open("Chunks/chunk15_17.txt").read())
        self.chunk15_18 = ast.literal_eval(open("Chunks/chunk15_18.txt").read())
        self.chunk15_19 = ast.literal_eval(open("Chunks/chunk15_19.txt").read())
        self.chunk15_20 = ast.literal_eval(open("Chunks/chunk15_20.txt").read())
        self.chunk15_21 = ast.literal_eval(open("Chunks/chunk15_21.txt").read())

        self.chunk16_0 = ast.literal_eval(open("Chunks/chunk16_0.txt").read())
        self.chunk16_1 = ast.literal_eval(open("Chunks/chunk16_1.txt").read())
        self.chunk16_2 = ast.literal_eval(open("Chunks/chunk16_2.txt").read())
        self.chunk16_3 = ast.literal_eval(open("Chunks/chunk16_3.txt").read())
        self.chunk16_4 = ast.literal_eval(open("Chunks/chunk16_4.txt").read())
        self.chunk16_5 = ast.literal_eval(open("Chunks/chunk16_5.txt").read())
        self.chunk16_6 = ast.literal_eval(open("Chunks/chunk16_6.txt").read())
        self.chunk16_7 = ast.literal_eval(open("Chunks/chunk16_7.txt").read())
        self.chunk16_8 = ast.literal_eval(open("Chunks/chunk16_8.txt").read())
        self.chunk16_9 = ast.literal_eval(open("Chunks/chunk16_9.txt").read())
        self.chunk16_10 = ast.literal_eval(open("Chunks/chunk16_10.txt").read())
        self.chunk16_11 = ast.literal_eval(open("Chunks/chunk16_11.txt").read())
        self.chunk16_12 = ast.literal_eval(open("Chunks/chunk16_12.txt").read())
        self.chunk16_13 = ast.literal_eval(open("Chunks/chunk16_13.txt").read())
        self.chunk16_14 = ast.literal_eval(open("Chunks/chunk16_14.txt").read())
        self.chunk16_15 = ast.literal_eval(open("Chunks/chunk16_15.txt").read())
        self.chunk16_16 = ast.literal_eval(open("Chunks/chunk16_16.txt").read())
        self.chunk16_17 = ast.literal_eval(open("Chunks/chunk16_17.txt").read())
        self.chunk16_18 = ast.literal_eval(open("Chunks/chunk16_18.txt").read())
        self.chunk16_19 = ast.literal_eval(open("Chunks/chunk16_19.txt").read())
        self.chunk16_20 = ast.literal_eval(open("Chunks/chunk16_20.txt").read())
        self.chunk16_21 = ast.literal_eval(open("Chunks/chunk16_21.txt").read())

        self.chunk17_0 = ast.literal_eval(open("Chunks/chunk17_0.txt").read())
        self.chunk17_1 = ast.literal_eval(open("Chunks/chunk17_1.txt").read())
        self.chunk17_2 = ast.literal_eval(open("Chunks/chunk17_2.txt").read())
        self.chunk17_3 = ast.literal_eval(open("Chunks/chunk17_3.txt").read())
        self.chunk17_4 = ast.literal_eval(open("Chunks/chunk17_4.txt").read())
        self.chunk17_5 = ast.literal_eval(open("Chunks/chunk17_5.txt").read())
        self.chunk17_6 = ast.literal_eval(open("Chunks/chunk17_6.txt").read())
        self.chunk17_7 = ast.literal_eval(open("Chunks/chunk17_7.txt").read())
        self.chunk17_8 = ast.literal_eval(open("Chunks/chunk17_8.txt").read())
        self.chunk17_9 = ast.literal_eval(open("Chunks/chunk17_9.txt").read())
        self.chunk17_10 = ast.literal_eval(open("Chunks/chunk17_10.txt").read())
        self.chunk17_11 = ast.literal_eval(open("Chunks/chunk17_11.txt").read())
        self.chunk17_12 = ast.literal_eval(open("Chunks/chunk17_12.txt").read())
        self.chunk17_13 = ast.literal_eval(open("Chunks/chunk17_13.txt").read())
        self.chunk17_14 = ast.literal_eval(open("Chunks/chunk17_14.txt").read())
        self.chunk17_15 = ast.literal_eval(open("Chunks/chunk17_15.txt").read())
        self.chunk17_16 = ast.literal_eval(open("Chunks/chunk17_16.txt").read())
        self.chunk17_17 = ast.literal_eval(open("Chunks/chunk17_17.txt").read())
        self.chunk17_18 = ast.literal_eval(open("Chunks/chunk17_18.txt").read())
        self.chunk17_19 = ast.literal_eval(open("Chunks/chunk17_19.txt").read())
        self.chunk17_20 = ast.literal_eval(open("Chunks/chunk17_20.txt").read())
        self.chunk17_21 = ast.literal_eval(open("Chunks/chunk17_21.txt").read())

        self.chunk18_0 = ast.literal_eval(open("Chunks/chunk18_0.txt").read())
        self.chunk18_1 = ast.literal_eval(open("Chunks/chunk18_1.txt").read())
        self.chunk18_2 = ast.literal_eval(open("Chunks/chunk18_2.txt").read())
        self.chunk18_3 = ast.literal_eval(open("Chunks/chunk18_3.txt").read())
        self.chunk18_4 = ast.literal_eval(open("Chunks/chunk18_4.txt").read())
        self.chunk18_5 = ast.literal_eval(open("Chunks/chunk18_5.txt").read())
        self.chunk18_6 = ast.literal_eval(open("Chunks/chunk18_6.txt").read())
        self.chunk18_7 = ast.literal_eval(open("Chunks/chunk18_7.txt").read())
        self.chunk18_8 = ast.literal_eval(open("Chunks/chunk18_8.txt").read())
        self.chunk18_9 = ast.literal_eval(open("Chunks/chunk18_9.txt").read())
        self.chunk18_10 = ast.literal_eval(open("Chunks/chunk18_10.txt").read())
        self.chunk18_11 = ast.literal_eval(open("Chunks/chunk18_11.txt").read())
        self.chunk18_12 = ast.literal_eval(open("Chunks/chunk18_12.txt").read())
        self.chunk18_13 = ast.literal_eval(open("Chunks/chunk18_13.txt").read())
        self.chunk18_14 = ast.literal_eval(open("Chunks/chunk18_14.txt").read())
        self.chunk18_15 = ast.literal_eval(open("Chunks/chunk18_15.txt").read())
        self.chunk18_16 = ast.literal_eval(open("Chunks/chunk18_16.txt").read())
        self.chunk18_17 = ast.literal_eval(open("Chunks/chunk18_17.txt").read())
        self.chunk18_18 = ast.literal_eval(open("Chunks/chunk18_18.txt").read())
        self.chunk18_19 = ast.literal_eval(open("Chunks/chunk18_19.txt").read())
        self.chunk18_20 = ast.literal_eval(open("Chunks/chunk18_20.txt").read())
        self.chunk18_21 = ast.literal_eval(open("Chunks/chunk18_21.txt").read())

        self.chunk19_0 = ast.literal_eval(open("Chunks/chunk19_0.txt").read())
        self.chunk19_1 = ast.literal_eval(open("Chunks/chunk19_1.txt").read())
        self.chunk19_2 = ast.literal_eval(open("Chunks/chunk19_2.txt").read())
        self.chunk19_3 = ast.literal_eval(open("Chunks/chunk19_3.txt").read())
        self.chunk19_4 = ast.literal_eval(open("Chunks/chunk19_4.txt").read())
        self.chunk19_5 = ast.literal_eval(open("Chunks/chunk19_5.txt").read())
        self.chunk19_6 = ast.literal_eval(open("Chunks/chunk19_6.txt").read())
        self.chunk19_7 = ast.literal_eval(open("Chunks/chunk19_7.txt").read())
        self.chunk19_8 = ast.literal_eval(open("Chunks/chunk19_8.txt").read())
        self.chunk19_9 = ast.literal_eval(open("Chunks/chunk19_9.txt").read())
        self.chunk19_10 = ast.literal_eval(open("Chunks/chunk19_10.txt").read())
        self.chunk19_11 = ast.literal_eval(open("Chunks/chunk19_11.txt").read())
        self.chunk19_12 = ast.literal_eval(open("Chunks/chunk19_12.txt").read())
        self.chunk19_13 = ast.literal_eval(open("Chunks/chunk19_13.txt").read())
        self.chunk19_14 = ast.literal_eval(open("Chunks/chunk19_14.txt").read())
        self.chunk19_15 = ast.literal_eval(open("Chunks/chunk19_15.txt").read())
        self.chunk19_16 = ast.literal_eval(open("Chunks/chunk19_16.txt").read())
        self.chunk19_17 = ast.literal_eval(open("Chunks/chunk19_17.txt").read())
        self.chunk19_18 = ast.literal_eval(open("Chunks/chunk19_18.txt").read())
        self.chunk19_19 = ast.literal_eval(open("Chunks/chunk19_19.txt").read())
        self.chunk19_20 = ast.literal_eval(open("Chunks/chunk19_20.txt").read())
        self.chunk19_21 = ast.literal_eval(open("Chunks/chunk19_21.txt").read())

        self.chunk20_0 = ast.literal_eval(open("Chunks/chunk20_0.txt").read())
        self.chunk20_1 = ast.literal_eval(open("Chunks/chunk20_1.txt").read())
        self.chunk20_2 = ast.literal_eval(open("Chunks/chunk20_2.txt").read())
        self.chunk20_3 = ast.literal_eval(open("Chunks/chunk20_3.txt").read())
        self.chunk20_4 = ast.literal_eval(open("Chunks/chunk20_4.txt").read())
        self.chunk20_5 = ast.literal_eval(open("Chunks/chunk20_5.txt").read())
        self.chunk20_6 = ast.literal_eval(open("Chunks/chunk20_6.txt").read())
        self.chunk20_7 = ast.literal_eval(open("Chunks/chunk20_7.txt").read())
        self.chunk20_8 = ast.literal_eval(open("Chunks/chunk20_8.txt").read())
        self.chunk20_9 = ast.literal_eval(open("Chunks/chunk20_9.txt").read())
        self.chunk20_10 = ast.literal_eval(open("Chunks/chunk20_10.txt").read())
        self.chunk20_11 = ast.literal_eval(open("Chunks/chunk20_11.txt").read())
        self.chunk20_12 = ast.literal_eval(open("Chunks/chunk20_12.txt").read())
        self.chunk20_13 = ast.literal_eval(open("Chunks/chunk20_13.txt").read())
        self.chunk20_14 = ast.literal_eval(open("Chunks/chunk20_14.txt").read())
        self.chunk20_15 = ast.literal_eval(open("Chunks/chunk20_15.txt").read())
        self.chunk20_16 = ast.literal_eval(open("Chunks/chunk20_16.txt").read())
        self.chunk20_17 = ast.literal_eval(open("Chunks/chunk20_17.txt").read())
        self.chunk20_18 = ast.literal_eval(open("Chunks/chunk20_18.txt").read())
        self.chunk20_19 = ast.literal_eval(open("Chunks/chunk20_19.txt").read())
        self.chunk20_20 = ast.literal_eval(open("Chunks/chunk20_20.txt").read())
        self.chunk20_21 = ast.literal_eval(open("Chunks/chunk20_21.txt").read())

        self.chunk21_0 = ast.literal_eval(open("Chunks/chunk21_0.txt").read())
        self.chunk21_1 = ast.literal_eval(open("Chunks/chunk21_1.txt").read())
        self.chunk21_2 = ast.literal_eval(open("Chunks/chunk21_2.txt").read())
        self.chunk21_3 = ast.literal_eval(open("Chunks/chunk21_3.txt").read())
        self.chunk21_4 = ast.literal_eval(open("Chunks/chunk21_4.txt").read())
        self.chunk21_5 = ast.literal_eval(open("Chunks/chunk21_5.txt").read())
        self.chunk21_6 = ast.literal_eval(open("Chunks/chunk21_6.txt").read())
        self.chunk21_7 = ast.literal_eval(open("Chunks/chunk21_7.txt").read())
        self.chunk21_8 = ast.literal_eval(open("Chunks/chunk21_8.txt").read())
        self.chunk21_9 = ast.literal_eval(open("Chunks/chunk21_9.txt").read())
        self.chunk21_10 = ast.literal_eval(open("Chunks/chunk21_10.txt").read())
        self.chunk21_11 = ast.literal_eval(open("Chunks/chunk21_11.txt").read())
        self.chunk21_12 = ast.literal_eval(open("Chunks/chunk21_12.txt").read())
        self.chunk21_13 = ast.literal_eval(open("Chunks/chunk21_13.txt").read())
        self.chunk21_14 = ast.literal_eval(open("Chunks/chunk21_14.txt").read())
        self.chunk21_15 = ast.literal_eval(open("Chunks/chunk21_15.txt").read())
        self.chunk21_16 = ast.literal_eval(open("Chunks/chunk21_16.txt").read())
        self.chunk21_17 = ast.literal_eval(open("Chunks/chunk21_17.txt").read())
        self.chunk21_18 = ast.literal_eval(open("Chunks/chunk21_18.txt").read())
        self.chunk21_19 = ast.literal_eval(open("Chunks/chunk21_19.txt").read())
        self.chunk21_20 = ast.literal_eval(open("Chunks/chunk21_20.txt").read())
        self.chunk21_21 = ast.literal_eval(open("Chunks/chunk21_21.txt").read())

        self.chunk22_0 = ast.literal_eval(open("Chunks/chunk22_0.txt").read())
        self.chunk22_1 = ast.literal_eval(open("Chunks/chunk22_1.txt").read())
        self.chunk22_2 = ast.literal_eval(open("Chunks/chunk22_2.txt").read())
        self.chunk22_3 = ast.literal_eval(open("Chunks/chunk22_3.txt").read())
        self.chunk22_4 = ast.literal_eval(open("Chunks/chunk22_4.txt").read())
        self.chunk22_5 = ast.literal_eval(open("Chunks/chunk22_5.txt").read())
        self.chunk22_6 = ast.literal_eval(open("Chunks/chunk22_6.txt").read())
        self.chunk22_7 = ast.literal_eval(open("Chunks/chunk22_7.txt").read())
        self.chunk22_8 = ast.literal_eval(open("Chunks/chunk22_8.txt").read())
        self.chunk22_9 = ast.literal_eval(open("Chunks/chunk22_9.txt").read())
        self.chunk22_10 = ast.literal_eval(open("Chunks/chunk22_10.txt").read())
        self.chunk22_11 = ast.literal_eval(open("Chunks/chunk22_11.txt").read())
        self.chunk22_12 = ast.literal_eval(open("Chunks/chunk22_12.txt").read())
        self.chunk22_13 = ast.literal_eval(open("Chunks/chunk22_13.txt").read())
        self.chunk22_14 = ast.literal_eval(open("Chunks/chunk22_14.txt").read())
        self.chunk22_15 = ast.literal_eval(open("Chunks/chunk22_15.txt").read())
        self.chunk22_16 = ast.literal_eval(open("Chunks/chunk22_16.txt").read())
        self.chunk22_17 = ast.literal_eval(open("Chunks/chunk22_17.txt").read())
        self.chunk22_18 = ast.literal_eval(open("Chunks/chunk22_18.txt").read())
        self.chunk22_19 = ast.literal_eval(open("Chunks/chunk22_19.txt").read())
        self.chunk22_20 = ast.literal_eval(open("Chunks/chunk22_20.txt").read())
        self.chunk22_21 = ast.literal_eval(open("Chunks/chunk22_21.txt").read())

        self.chunk23_0 = ast.literal_eval(open("Chunks/chunk23_0.txt").read())
        self.chunk23_1 = ast.literal_eval(open("Chunks/chunk23_1.txt").read())
        self.chunk23_2 = ast.literal_eval(open("Chunks/chunk23_2.txt").read())
        self.chunk23_3 = ast.literal_eval(open("Chunks/chunk23_3.txt").read())
        self.chunk23_4 = ast.literal_eval(open("Chunks/chunk23_4.txt").read())
        self.chunk23_5 = ast.literal_eval(open("Chunks/chunk23_5.txt").read())
        self.chunk23_6 = ast.literal_eval(open("Chunks/chunk23_6.txt").read())
        self.chunk23_7 = ast.literal_eval(open("Chunks/chunk23_7.txt").read())
        self.chunk23_8 = ast.literal_eval(open("Chunks/chunk23_8.txt").read())
        self.chunk23_9 = ast.literal_eval(open("Chunks/chunk23_9.txt").read())
        self.chunk23_10 = ast.literal_eval(open("Chunks/chunk23_10.txt").read())
        self.chunk23_11 = ast.literal_eval(open("Chunks/chunk23_11.txt").read())
        self.chunk23_12 = ast.literal_eval(open("Chunks/chunk23_12.txt").read())
        self.chunk23_13 = ast.literal_eval(open("Chunks/chunk23_13.txt").read())
        self.chunk23_14 = ast.literal_eval(open("Chunks/chunk23_14.txt").read())
        self.chunk23_15 = ast.literal_eval(open("Chunks/chunk23_15.txt").read())
        self.chunk23_16 = ast.literal_eval(open("Chunks/chunk23_16.txt").read())
        self.chunk23_17 = ast.literal_eval(open("Chunks/chunk23_17.txt").read())
        self.chunk23_18 = ast.literal_eval(open("Chunks/chunk23_18.txt").read())
        self.chunk23_19 = ast.literal_eval(open("Chunks/chunk23_19.txt").read())
        self.chunk23_20 = ast.literal_eval(open("Chunks/chunk23_20.txt").read())
        self.chunk23_21 = ast.literal_eval(open("Chunks/chunk23_21.txt").read())

        self.chunk24_0 = ast.literal_eval(open("Chunks/chunk24_0.txt").read())
        self.chunk24_1 = ast.literal_eval(open("Chunks/chunk24_1.txt").read())
        self.chunk24_2 = ast.literal_eval(open("Chunks/chunk24_2.txt").read())
        self.chunk24_3 = ast.literal_eval(open("Chunks/chunk24_3.txt").read())
        self.chunk24_4 = ast.literal_eval(open("Chunks/chunk24_4.txt").read())
        self.chunk24_5 = ast.literal_eval(open("Chunks/chunk24_5.txt").read())
        self.chunk24_6 = ast.literal_eval(open("Chunks/chunk24_6.txt").read())
        self.chunk24_7 = ast.literal_eval(open("Chunks/chunk24_7.txt").read())
        self.chunk24_8 = ast.literal_eval(open("Chunks/chunk24_8.txt").read())
        self.chunk24_9 = ast.literal_eval(open("Chunks/chunk24_9.txt").read())
        self.chunk24_10 = ast.literal_eval(open("Chunks/chunk24_10.txt").read())
        self.chunk24_11 = ast.literal_eval(open("Chunks/chunk24_11.txt").read())
        self.chunk24_12 = ast.literal_eval(open("Chunks/chunk24_12.txt").read())
        self.chunk24_13 = ast.literal_eval(open("Chunks/chunk24_13.txt").read())
        self.chunk24_14 = ast.literal_eval(open("Chunks/chunk24_14.txt").read())
        self.chunk24_15 = ast.literal_eval(open("Chunks/chunk24_15.txt").read())
        self.chunk24_16 = ast.literal_eval(open("Chunks/chunk24_16.txt").read())
        self.chunk24_17 = ast.literal_eval(open("Chunks/chunk24_17.txt").read())
        self.chunk24_18 = ast.literal_eval(open("Chunks/chunk24_18.txt").read())
        self.chunk24_19 = ast.literal_eval(open("Chunks/chunk24_19.txt").read())
        self.chunk24_20 = ast.literal_eval(open("Chunks/chunk24_20.txt").read())
        self.chunk24_21 = ast.literal_eval(open("Chunks/chunk24_21.txt").read())

        self.chunk25_0 = ast.literal_eval(open("Chunks/chunk25_0.txt").read())
        self.chunk25_1 = ast.literal_eval(open("Chunks/chunk25_1.txt").read())
        self.chunk25_2 = ast.literal_eval(open("Chunks/chunk25_2.txt").read())
        self.chunk25_3 = ast.literal_eval(open("Chunks/chunk25_3.txt").read())
        self.chunk25_4 = ast.literal_eval(open("Chunks/chunk25_4.txt").read())
        self.chunk25_5 = ast.literal_eval(open("Chunks/chunk25_5.txt").read())
        self.chunk25_6 = ast.literal_eval(open("Chunks/chunk25_6.txt").read())
        self.chunk25_7 = ast.literal_eval(open("Chunks/chunk25_7.txt").read())
        self.chunk25_8 = ast.literal_eval(open("Chunks/chunk25_8.txt").read())
        self.chunk25_9 = ast.literal_eval(open("Chunks/chunk25_9.txt").read())
        self.chunk25_10 = ast.literal_eval(open("Chunks/chunk25_10.txt").read())
        self.chunk25_11 = ast.literal_eval(open("Chunks/chunk25_11.txt").read())
        self.chunk25_12 = ast.literal_eval(open("Chunks/chunk25_12.txt").read())
        self.chunk25_13 = ast.literal_eval(open("Chunks/chunk25_13.txt").read())
        self.chunk25_14 = ast.literal_eval(open("Chunks/chunk25_14.txt").read())
        self.chunk25_15 = ast.literal_eval(open("Chunks/chunk25_15.txt").read())
        self.chunk25_16 = ast.literal_eval(open("Chunks/chunk25_16.txt").read())
        self.chunk25_17 = ast.literal_eval(open("Chunks/chunk25_17.txt").read())
        self.chunk25_18 = ast.literal_eval(open("Chunks/chunk25_18.txt").read())
        self.chunk25_19 = ast.literal_eval(open("Chunks/chunk25_19.txt").read())
        self.chunk25_20 = ast.literal_eval(open("Chunks/chunk25_20.txt").read())
        self.chunk25_21 = ast.literal_eval(open("Chunks/chunk25_21.txt").read())

        self.chunk26_0 = ast.literal_eval(open("Chunks/chunk26_0.txt").read())
        self.chunk26_1 = ast.literal_eval(open("Chunks/chunk26_1.txt").read())
        self.chunk26_2 = ast.literal_eval(open("Chunks/chunk26_2.txt").read())
        self.chunk26_3 = ast.literal_eval(open("Chunks/chunk26_3.txt").read())
        self.chunk26_4 = ast.literal_eval(open("Chunks/chunk26_4.txt").read())
        self.chunk26_5 = ast.literal_eval(open("Chunks/chunk26_5.txt").read())
        self.chunk26_6 = ast.literal_eval(open("Chunks/chunk26_6.txt").read())
        self.chunk26_7 = ast.literal_eval(open("Chunks/chunk26_7.txt").read())
        self.chunk26_8 = ast.literal_eval(open("Chunks/chunk26_8.txt").read())
        self.chunk26_9 = ast.literal_eval(open("Chunks/chunk26_9.txt").read())
        self.chunk26_10 = ast.literal_eval(open("Chunks/chunk26_10.txt").read())
        self.chunk26_11 = ast.literal_eval(open("Chunks/chunk26_11.txt").read())
        self.chunk26_12 = ast.literal_eval(open("Chunks/chunk26_12.txt").read())
        self.chunk26_13 = ast.literal_eval(open("Chunks/chunk26_13.txt").read())
        self.chunk26_14 = ast.literal_eval(open("Chunks/chunk26_14.txt").read())
        self.chunk26_15 = ast.literal_eval(open("Chunks/chunk26_15.txt").read())
        self.chunk26_16 = ast.literal_eval(open("Chunks/chunk26_16.txt").read())
        self.chunk26_17 = ast.literal_eval(open("Chunks/chunk26_17.txt").read())
        self.chunk26_18 = ast.literal_eval(open("Chunks/chunk26_18.txt").read())
        self.chunk26_19 = ast.literal_eval(open("Chunks/chunk26_19.txt").read())
        self.chunk26_20 = ast.literal_eval(open("Chunks/chunk26_20.txt").read())
        self.chunk26_21 = ast.literal_eval(open("Chunks/chunk26_21.txt").read())

        self.chunk27_0 = ast.literal_eval(open("Chunks/chunk27_0.txt").read())
        self.chunk27_1 = ast.literal_eval(open("Chunks/chunk27_1.txt").read())
        self.chunk27_2 = ast.literal_eval(open("Chunks/chunk27_2.txt").read())
        self.chunk27_3 = ast.literal_eval(open("Chunks/chunk27_3.txt").read())
        self.chunk27_4 = ast.literal_eval(open("Chunks/chunk27_4.txt").read())
        self.chunk27_5 = ast.literal_eval(open("Chunks/chunk27_5.txt").read())
        self.chunk27_6 = ast.literal_eval(open("Chunks/chunk27_6.txt").read())
        self.chunk27_7 = ast.literal_eval(open("Chunks/chunk27_7.txt").read())
        self.chunk27_8 = ast.literal_eval(open("Chunks/chunk27_8.txt").read())
        self.chunk27_9 = ast.literal_eval(open("Chunks/chunk27_9.txt").read())
        self.chunk27_10 = ast.literal_eval(open("Chunks/chunk27_10.txt").read())
        self.chunk27_11 = ast.literal_eval(open("Chunks/chunk27_11.txt").read())
        self.chunk27_12 = ast.literal_eval(open("Chunks/chunk27_12.txt").read())
        self.chunk27_13 = ast.literal_eval(open("Chunks/chunk27_13.txt").read())
        self.chunk27_14 = ast.literal_eval(open("Chunks/chunk27_14.txt").read())
        self.chunk27_15 = ast.literal_eval(open("Chunks/chunk27_15.txt").read())
        self.chunk27_16 = ast.literal_eval(open("Chunks/chunk27_16.txt").read())
        self.chunk27_17 = ast.literal_eval(open("Chunks/chunk27_17.txt").read())
        self.chunk27_18 = ast.literal_eval(open("Chunks/chunk27_18.txt").read())
        self.chunk27_19 = ast.literal_eval(open("Chunks/chunk27_19.txt").read())
        self.chunk27_20 = ast.literal_eval(open("Chunks/chunk27_20.txt").read())
        self.chunk27_21 = ast.literal_eval(open("Chunks/chunk27_21.txt").read())

        self.chunk28_0 = ast.literal_eval(open("Chunks/chunk28_0.txt").read())
        self.chunk28_1 = ast.literal_eval(open("Chunks/chunk28_1.txt").read())
        self.chunk28_2 = ast.literal_eval(open("Chunks/chunk28_2.txt").read())
        self.chunk28_3 = ast.literal_eval(open("Chunks/chunk28_3.txt").read())
        self.chunk28_4 = ast.literal_eval(open("Chunks/chunk28_4.txt").read())
        self.chunk28_5 = ast.literal_eval(open("Chunks/chunk28_5.txt").read())
        self.chunk28_6 = ast.literal_eval(open("Chunks/chunk28_6.txt").read())
        self.chunk28_7 = ast.literal_eval(open("Chunks/chunk28_7.txt").read())
        self.chunk28_8 = ast.literal_eval(open("Chunks/chunk28_8.txt").read())
        self.chunk28_9 = ast.literal_eval(open("Chunks/chunk28_9.txt").read())
        self.chunk28_10 = ast.literal_eval(open("Chunks/chunk28_10.txt").read())
        self.chunk28_11 = ast.literal_eval(open("Chunks/chunk28_11.txt").read())
        self.chunk28_12 = ast.literal_eval(open("Chunks/chunk28_12.txt").read())
        self.chunk28_13 = ast.literal_eval(open("Chunks/chunk28_13.txt").read())
        self.chunk28_14 = ast.literal_eval(open("Chunks/chunk28_14.txt").read())
        self.chunk28_15 = ast.literal_eval(open("Chunks/chunk28_15.txt").read())
        self.chunk28_16 = ast.literal_eval(open("Chunks/chunk28_16.txt").read())
        self.chunk28_17 = ast.literal_eval(open("Chunks/chunk28_17.txt").read())
        self.chunk28_18 = ast.literal_eval(open("Chunks/chunk28_18.txt").read())
        self.chunk28_19 = ast.literal_eval(open("Chunks/chunk28_19.txt").read())
        self.chunk28_20 = ast.literal_eval(open("Chunks/chunk28_20.txt").read())
        self.chunk28_21 = ast.literal_eval(open("Chunks/chunk28_21.txt").read())

        self.chunk29_0 = ast.literal_eval(open("Chunks/chunk29_0.txt").read())
        self.chunk29_1 = ast.literal_eval(open("Chunks/chunk29_1.txt").read())
        self.chunk29_2 = ast.literal_eval(open("Chunks/chunk29_2.txt").read())
        self.chunk29_3 = ast.literal_eval(open("Chunks/chunk29_3.txt").read())
        self.chunk29_4 = ast.literal_eval(open("Chunks/chunk29_4.txt").read())
        self.chunk29_5 = ast.literal_eval(open("Chunks/chunk29_5.txt").read())
        self.chunk29_6 = ast.literal_eval(open("Chunks/chunk29_6.txt").read())
        self.chunk29_7 = ast.literal_eval(open("Chunks/chunk29_7.txt").read())
        self.chunk29_8 = ast.literal_eval(open("Chunks/chunk29_8.txt").read())
        self.chunk29_9 = ast.literal_eval(open("Chunks/chunk29_9.txt").read())
        self.chunk29_10 = ast.literal_eval(open("Chunks/chunk29_10.txt").read())
        self.chunk29_11 = ast.literal_eval(open("Chunks/chunk29_11.txt").read())
        self.chunk29_12 = ast.literal_eval(open("Chunks/chunk29_12.txt").read())
        self.chunk29_13 = ast.literal_eval(open("Chunks/chunk29_13.txt").read())
        self.chunk29_14 = ast.literal_eval(open("Chunks/chunk29_14.txt").read())
        self.chunk29_15 = ast.literal_eval(open("Chunks/chunk29_15.txt").read())
        self.chunk29_16 = ast.literal_eval(open("Chunks/chunk29_16.txt").read())
        self.chunk29_17 = ast.literal_eval(open("Chunks/chunk29_17.txt").read())
        self.chunk29_18 = ast.literal_eval(open("Chunks/chunk29_18.txt").read())
        self.chunk29_19 = ast.literal_eval(open("Chunks/chunk29_19.txt").read())
        self.chunk29_20 = ast.literal_eval(open("Chunks/chunk29_20.txt").read())
        self.chunk29_21 = ast.literal_eval(open("Chunks/chunk29_21.txt").read())

        self.chunk30_0 = ast.literal_eval(open("Chunks/chunk30_0.txt").read())
        self.chunk30_1 = ast.literal_eval(open("Chunks/chunk30_1.txt").read())
        self.chunk30_2 = ast.literal_eval(open("Chunks/chunk30_2.txt").read())
        self.chunk30_3 = ast.literal_eval(open("Chunks/chunk30_3.txt").read())
        self.chunk30_4 = ast.literal_eval(open("Chunks/chunk30_4.txt").read())
        self.chunk30_5 = ast.literal_eval(open("Chunks/chunk30_5.txt").read())
        self.chunk30_6 = ast.literal_eval(open("Chunks/chunk30_6.txt").read())
        self.chunk30_7 = ast.literal_eval(open("Chunks/chunk30_7.txt").read())
        self.chunk30_8 = ast.literal_eval(open("Chunks/chunk30_8.txt").read())
        self.chunk30_9 = ast.literal_eval(open("Chunks/chunk30_9.txt").read())
        self.chunk30_10 = ast.literal_eval(open("Chunks/chunk30_10.txt").read())
        self.chunk30_11 = ast.literal_eval(open("Chunks/chunk30_11.txt").read())
        self.chunk30_12 = ast.literal_eval(open("Chunks/chunk30_12.txt").read())
        self.chunk30_13 = ast.literal_eval(open("Chunks/chunk30_13.txt").read())
        self.chunk30_14 = ast.literal_eval(open("Chunks/chunk30_14.txt").read())
        self.chunk30_15 = ast.literal_eval(open("Chunks/chunk30_15.txt").read())
        self.chunk30_16 = ast.literal_eval(open("Chunks/chunk30_16.txt").read())
        self.chunk30_17 = ast.literal_eval(open("Chunks/chunk30_17.txt").read())
        self.chunk30_18 = ast.literal_eval(open("Chunks/chunk30_18.txt").read())
        self.chunk30_19 = ast.literal_eval(open("Chunks/chunk30_19.txt").read())
        self.chunk30_20 = ast.literal_eval(open("Chunks/chunk30_20.txt").read())
        self.chunk30_21 = ast.literal_eval(open("Chunks/chunk30_21.txt").read())

        self.chunk31_0 = ast.literal_eval(open("Chunks/chunk31_0.txt").read())
        self.chunk31_1 = ast.literal_eval(open("Chunks/chunk31_1.txt").read())
        self.chunk31_2 = ast.literal_eval(open("Chunks/chunk31_2.txt").read())
        self.chunk31_3 = ast.literal_eval(open("Chunks/chunk31_3.txt").read())
        self.chunk31_4 = ast.literal_eval(open("Chunks/chunk31_4.txt").read())
        self.chunk31_5 = ast.literal_eval(open("Chunks/chunk31_5.txt").read())
        self.chunk31_6 = ast.literal_eval(open("Chunks/chunk31_6.txt").read())
        self.chunk31_7 = ast.literal_eval(open("Chunks/chunk31_7.txt").read())
        self.chunk31_8 = ast.literal_eval(open("Chunks/chunk31_8.txt").read())
        self.chunk31_9 = ast.literal_eval(open("Chunks/chunk31_9.txt").read())
        self.chunk31_10 = ast.literal_eval(open("Chunks/chunk31_10.txt").read())
        self.chunk31_11 = ast.literal_eval(open("Chunks/chunk31_11.txt").read())
        self.chunk31_12 = ast.literal_eval(open("Chunks/chunk31_12.txt").read())
        self.chunk31_13 = ast.literal_eval(open("Chunks/chunk31_13.txt").read())
        self.chunk31_14 = ast.literal_eval(open("Chunks/chunk31_14.txt").read())
        self.chunk31_15 = ast.literal_eval(open("Chunks/chunk31_15.txt").read())
        self.chunk31_16 = ast.literal_eval(open("Chunks/chunk31_16.txt").read())
        self.chunk31_17 = ast.literal_eval(open("Chunks/chunk31_17.txt").read())
        self.chunk31_18 = ast.literal_eval(open("Chunks/chunk31_18.txt").read())
        self.chunk31_19 = ast.literal_eval(open("Chunks/chunk31_19.txt").read())
        self.chunk31_20 = ast.literal_eval(open("Chunks/chunk31_20.txt").read())
        self.chunk31_21 = ast.literal_eval(open("Chunks/chunk31_21.txt").read())

        self.chunk32_0 = ast.literal_eval(open("Chunks/chunk32_0.txt").read())
        self.chunk32_1 = ast.literal_eval(open("Chunks/chunk32_1.txt").read())
        self.chunk32_2 = ast.literal_eval(open("Chunks/chunk32_2.txt").read())
        self.chunk32_3 = ast.literal_eval(open("Chunks/chunk32_3.txt").read())
        self.chunk32_4 = ast.literal_eval(open("Chunks/chunk32_4.txt").read())
        self.chunk32_5 = ast.literal_eval(open("Chunks/chunk32_5.txt").read())
        self.chunk32_6 = ast.literal_eval(open("Chunks/chunk32_6.txt").read())
        self.chunk32_7 = ast.literal_eval(open("Chunks/chunk32_7.txt").read())
        self.chunk32_8 = ast.literal_eval(open("Chunks/chunk32_8.txt").read())
        self.chunk32_9 = ast.literal_eval(open("Chunks/chunk32_9.txt").read())
        self.chunk32_10 = ast.literal_eval(open("Chunks/chunk32_10.txt").read())
        self.chunk32_11 = ast.literal_eval(open("Chunks/chunk32_11.txt").read())
        self.chunk32_12 = ast.literal_eval(open("Chunks/chunk32_12.txt").read())
        self.chunk32_13 = ast.literal_eval(open("Chunks/chunk32_13.txt").read())
        self.chunk32_14 = ast.literal_eval(open("Chunks/chunk32_14.txt").read())
        self.chunk32_15 = ast.literal_eval(open("Chunks/chunk32_15.txt").read())
        self.chunk32_16 = ast.literal_eval(open("Chunks/chunk32_16.txt").read())
        self.chunk32_17 = ast.literal_eval(open("Chunks/chunk32_17.txt").read())
        self.chunk32_18 = ast.literal_eval(open("Chunks/chunk32_18.txt").read())
        self.chunk32_19 = ast.literal_eval(open("Chunks/chunk32_19.txt").read())
        self.chunk32_20 = ast.literal_eval(open("Chunks/chunk32_20.txt").read())
        self.chunk32_21 = ast.literal_eval(open("Chunks/chunk32_21.txt").read())

        self.chunk33_0 = ast.literal_eval(open("Chunks/chunk33_0.txt").read())
        self.chunk33_1 = ast.literal_eval(open("Chunks/chunk33_1.txt").read())
        self.chunk33_2 = ast.literal_eval(open("Chunks/chunk33_2.txt").read())
        self.chunk33_3 = ast.literal_eval(open("Chunks/chunk33_3.txt").read())
        self.chunk33_4 = ast.literal_eval(open("Chunks/chunk33_4.txt").read())
        self.chunk33_5 = ast.literal_eval(open("Chunks/chunk33_5.txt").read())
        self.chunk33_6 = ast.literal_eval(open("Chunks/chunk33_6.txt").read())
        self.chunk33_7 = ast.literal_eval(open("Chunks/chunk33_7.txt").read())
        self.chunk33_8 = ast.literal_eval(open("Chunks/chunk33_8.txt").read())
        self.chunk33_9 = ast.literal_eval(open("Chunks/chunk33_9.txt").read())
        self.chunk33_10 = ast.literal_eval(open("Chunks/chunk33_10.txt").read())
        self.chunk33_11 = ast.literal_eval(open("Chunks/chunk33_11.txt").read())
        self.chunk33_12 = ast.literal_eval(open("Chunks/chunk33_12.txt").read())
        self.chunk33_13 = ast.literal_eval(open("Chunks/chunk33_13.txt").read())
        self.chunk33_14 = ast.literal_eval(open("Chunks/chunk33_14.txt").read())
        self.chunk33_15 = ast.literal_eval(open("Chunks/chunk33_15.txt").read())
        self.chunk33_16 = ast.literal_eval(open("Chunks/chunk33_16.txt").read())
        self.chunk33_17 = ast.literal_eval(open("Chunks/chunk33_17.txt").read())
        self.chunk33_18 = ast.literal_eval(open("Chunks/chunk33_18.txt").read())
        self.chunk33_19 = ast.literal_eval(open("Chunks/chunk33_19.txt").read())
        self.chunk33_20 = ast.literal_eval(open("Chunks/chunk33_20.txt").read())
        self.chunk33_21 = ast.literal_eval(open("Chunks/chunk33_21.txt").read())

        self.chunk34_0 = ast.literal_eval(open("Chunks/chunk34_0.txt").read())
        self.chunk34_1 = ast.literal_eval(open("Chunks/chunk34_1.txt").read())
        self.chunk34_2 = ast.literal_eval(open("Chunks/chunk34_2.txt").read())
        self.chunk34_3 = ast.literal_eval(open("Chunks/chunk34_3.txt").read())
        self.chunk34_4 = ast.literal_eval(open("Chunks/chunk34_4.txt").read())
        self.chunk34_5 = ast.literal_eval(open("Chunks/chunk34_5.txt").read())
        self.chunk34_6 = ast.literal_eval(open("Chunks/chunk34_6.txt").read())
        self.chunk34_7 = ast.literal_eval(open("Chunks/chunk34_7.txt").read())
        self.chunk34_8 = ast.literal_eval(open("Chunks/chunk34_8.txt").read())
        self.chunk34_9 = ast.literal_eval(open("Chunks/chunk34_9.txt").read())
        self.chunk34_10 = ast.literal_eval(open("Chunks/chunk34_10.txt").read())
        self.chunk34_11 = ast.literal_eval(open("Chunks/chunk34_11.txt").read())
        self.chunk34_12 = ast.literal_eval(open("Chunks/chunk34_12.txt").read())
        self.chunk34_13 = ast.literal_eval(open("Chunks/chunk34_13.txt").read())
        self.chunk34_14 = ast.literal_eval(open("Chunks/chunk34_14.txt").read())
        self.chunk34_15 = ast.literal_eval(open("Chunks/chunk34_15.txt").read())
        self.chunk34_16 = ast.literal_eval(open("Chunks/chunk34_16.txt").read())
        self.chunk34_17 = ast.literal_eval(open("Chunks/chunk34_17.txt").read())
        self.chunk34_18 = ast.literal_eval(open("Chunks/chunk34_18.txt").read())
        self.chunk34_19 = ast.literal_eval(open("Chunks/chunk34_19.txt").read())
        self.chunk34_20 = ast.literal_eval(open("Chunks/chunk34_20.txt").read())
        self.chunk34_21 = ast.literal_eval(open("Chunks/chunk34_21.txt").read())

        self.chunk35_0 = ast.literal_eval(open("Chunks/chunk35_0.txt").read())
        self.chunk35_1 = ast.literal_eval(open("Chunks/chunk35_1.txt").read())
        self.chunk35_2 = ast.literal_eval(open("Chunks/chunk35_2.txt").read())
        self.chunk35_3 = ast.literal_eval(open("Chunks/chunk35_3.txt").read())
        self.chunk35_4 = ast.literal_eval(open("Chunks/chunk35_4.txt").read())
        self.chunk35_5 = ast.literal_eval(open("Chunks/chunk35_5.txt").read())
        self.chunk35_6 = ast.literal_eval(open("Chunks/chunk35_6.txt").read())
        self.chunk35_7 = ast.literal_eval(open("Chunks/chunk35_7.txt").read())
        self.chunk35_8 = ast.literal_eval(open("Chunks/chunk35_8.txt").read())
        self.chunk35_9 = ast.literal_eval(open("Chunks/chunk35_9.txt").read())
        self.chunk35_10 = ast.literal_eval(open("Chunks/chunk35_10.txt").read())
        self.chunk35_11 = ast.literal_eval(open("Chunks/chunk35_11.txt").read())
        self.chunk35_12 = ast.literal_eval(open("Chunks/chunk35_12.txt").read())
        self.chunk35_13 = ast.literal_eval(open("Chunks/chunk35_13.txt").read())
        self.chunk35_14 = ast.literal_eval(open("Chunks/chunk35_14.txt").read())
        self.chunk35_15 = ast.literal_eval(open("Chunks/chunk35_15.txt").read())
        self.chunk35_16 = ast.literal_eval(open("Chunks/chunk35_16.txt").read())
        self.chunk35_17 = ast.literal_eval(open("Chunks/chunk35_17.txt").read())
        self.chunk35_18 = ast.literal_eval(open("Chunks/chunk35_18.txt").read())
        self.chunk35_19 = ast.literal_eval(open("Chunks/chunk35_19.txt").read())
        self.chunk35_20 = ast.literal_eval(open("Chunks/chunk35_20.txt").read())
        self.chunk35_21 = ast.literal_eval(open("Chunks/chunk35_21.txt").read())

        self.chunk36_0 = ast.literal_eval(open("Chunks/chunk36_0.txt").read())
        self.chunk36_1 = ast.literal_eval(open("Chunks/chunk36_1.txt").read())
        self.chunk36_2 = ast.literal_eval(open("Chunks/chunk36_2.txt").read())
        self.chunk36_3 = ast.literal_eval(open("Chunks/chunk36_3.txt").read())
        self.chunk36_4 = ast.literal_eval(open("Chunks/chunk36_4.txt").read())
        self.chunk36_5 = ast.literal_eval(open("Chunks/chunk36_5.txt").read())
        self.chunk36_6 = ast.literal_eval(open("Chunks/chunk36_6.txt").read())
        self.chunk36_7 = ast.literal_eval(open("Chunks/chunk36_7.txt").read())
        self.chunk36_8 = ast.literal_eval(open("Chunks/chunk36_8.txt").read())
        self.chunk36_9 = ast.literal_eval(open("Chunks/chunk36_9.txt").read())
        self.chunk36_10 = ast.literal_eval(open("Chunks/chunk36_10.txt").read())
        self.chunk36_11 = ast.literal_eval(open("Chunks/chunk36_11.txt").read())
        self.chunk36_12 = ast.literal_eval(open("Chunks/chunk36_12.txt").read())
        self.chunk36_13 = ast.literal_eval(open("Chunks/chunk36_13.txt").read())
        self.chunk36_14 = ast.literal_eval(open("Chunks/chunk36_14.txt").read())
        self.chunk36_15 = ast.literal_eval(open("Chunks/chunk36_15.txt").read())
        self.chunk36_16 = ast.literal_eval(open("Chunks/chunk36_16.txt").read())
        self.chunk36_17 = ast.literal_eval(open("Chunks/chunk36_17.txt").read())
        self.chunk36_18 = ast.literal_eval(open("Chunks/chunk36_18.txt").read())
        self.chunk36_19 = ast.literal_eval(open("Chunks/chunk36_19.txt").read())
        self.chunk36_20 = ast.literal_eval(open("Chunks/chunk36_20.txt").read())
        self.chunk36_21 = ast.literal_eval(open("Chunks/chunk36_21.txt").read())

        self.chunk37_0 = ast.literal_eval(open("Chunks/chunk37_0.txt").read())
        self.chunk37_1 = ast.literal_eval(open("Chunks/chunk37_1.txt").read())
        self.chunk37_2 = ast.literal_eval(open("Chunks/chunk37_2.txt").read())
        self.chunk37_3 = ast.literal_eval(open("Chunks/chunk37_3.txt").read())
        self.chunk37_4 = ast.literal_eval(open("Chunks/chunk37_4.txt").read())
        self.chunk37_5 = ast.literal_eval(open("Chunks/chunk37_5.txt").read())
        self.chunk37_6 = ast.literal_eval(open("Chunks/chunk37_6.txt").read())
        self.chunk37_7 = ast.literal_eval(open("Chunks/chunk37_7.txt").read())
        self.chunk37_8 = ast.literal_eval(open("Chunks/chunk37_8.txt").read())
        self.chunk37_9 = ast.literal_eval(open("Chunks/chunk37_9.txt").read())
        self.chunk37_10 = ast.literal_eval(open("Chunks/chunk37_10.txt").read())
        self.chunk37_11 = ast.literal_eval(open("Chunks/chunk37_11.txt").read())
        self.chunk37_12 = ast.literal_eval(open("Chunks/chunk37_12.txt").read())
        self.chunk37_13 = ast.literal_eval(open("Chunks/chunk37_13.txt").read())
        self.chunk37_14 = ast.literal_eval(open("Chunks/chunk37_14.txt").read())
        self.chunk37_15 = ast.literal_eval(open("Chunks/chunk37_15.txt").read())
        self.chunk37_16 = ast.literal_eval(open("Chunks/chunk37_16.txt").read())
        self.chunk37_17 = ast.literal_eval(open("Chunks/chunk37_17.txt").read())
        self.chunk37_18 = ast.literal_eval(open("Chunks/chunk37_18.txt").read())
        self.chunk37_19 = ast.literal_eval(open("Chunks/chunk37_19.txt").read())
        self.chunk37_20 = ast.literal_eval(open("Chunks/chunk37_20.txt").read())
        self.chunk37_21 = ast.literal_eval(open("Chunks/chunk37_21.txt").read())
        
        self.chunk38_0 = ast.literal_eval(open("Chunks/chunk38_0.txt").read())
        self.chunk38_1 = ast.literal_eval(open("Chunks/chunk38_1.txt").read())
        self.chunk38_2 = ast.literal_eval(open("Chunks/chunk38_2.txt").read())
        self.chunk38_3 = ast.literal_eval(open("Chunks/chunk38_3.txt").read())
        self.chunk38_4 = ast.literal_eval(open("Chunks/chunk38_4.txt").read())
        self.chunk38_5 = ast.literal_eval(open("Chunks/chunk38_5.txt").read())
        self.chunk38_6 = ast.literal_eval(open("Chunks/chunk38_6.txt").read())
        self.chunk38_7 = ast.literal_eval(open("Chunks/chunk38_7.txt").read())
        self.chunk38_8 = ast.literal_eval(open("Chunks/chunk38_8.txt").read())
        self.chunk38_9 = ast.literal_eval(open("Chunks/chunk38_9.txt").read())
        self.chunk38_10 = ast.literal_eval(open("Chunks/chunk38_10.txt").read())
        self.chunk38_11 = ast.literal_eval(open("Chunks/chunk38_11.txt").read())
        self.chunk38_12 = ast.literal_eval(open("Chunks/chunk38_12.txt").read())
        self.chunk38_13 = ast.literal_eval(open("Chunks/chunk38_13.txt").read())
        self.chunk38_14 = ast.literal_eval(open("Chunks/chunk38_14.txt").read())
        self.chunk38_15 = ast.literal_eval(open("Chunks/chunk38_15.txt").read())
        self.chunk38_16 = ast.literal_eval(open("Chunks/chunk38_16.txt").read())
        self.chunk38_17 = ast.literal_eval(open("Chunks/chunk38_17.txt").read())
        self.chunk38_18 = ast.literal_eval(open("Chunks/chunk38_18.txt").read())
        self.chunk38_19 = ast.literal_eval(open("Chunks/chunk38_19.txt").read())
        self.chunk38_20 = ast.literal_eval(open("Chunks/chunk38_20.txt").read())
        self.chunk38_21 = ast.literal_eval(open("Chunks/chunk38_21.txt").read())

        self.chunk39_0 = ast.literal_eval(open("Chunks/chunk39_0.txt").read())
        self.chunk39_1 = ast.literal_eval(open("Chunks/chunk39_1.txt").read())
        self.chunk39_2 = ast.literal_eval(open("Chunks/chunk39_2.txt").read())
        self.chunk39_3 = ast.literal_eval(open("Chunks/chunk39_3.txt").read())
        self.chunk39_4 = ast.literal_eval(open("Chunks/chunk39_4.txt").read())
        self.chunk39_5 = ast.literal_eval(open("Chunks/chunk39_5.txt").read())
        self.chunk39_6 = ast.literal_eval(open("Chunks/chunk39_6.txt").read())
        self.chunk39_7 = ast.literal_eval(open("Chunks/chunk39_7.txt").read())
        self.chunk39_8 = ast.literal_eval(open("Chunks/chunk39_8.txt").read())
        self.chunk39_9 = ast.literal_eval(open("Chunks/chunk39_9.txt").read())
        self.chunk39_10 = ast.literal_eval(open("Chunks/chunk39_10.txt").read())
        self.chunk39_11 = ast.literal_eval(open("Chunks/chunk39_11.txt").read())
        self.chunk39_12 = ast.literal_eval(open("Chunks/chunk39_12.txt").read())
        
        self.chunk40_0 = ast.literal_eval(open("Chunks/chunk40_0.txt").read())
        self.chunk40_1 = ast.literal_eval(open("Chunks/chunk40_1.txt").read())
        self.chunk40_2 = ast.literal_eval(open("Chunks/chunk40_2.txt").read())
        self.chunk40_3 = ast.literal_eval(open("Chunks/chunk40_3.txt").read())
        self.chunk40_4 = ast.literal_eval(open("Chunks/chunk40_4.txt").read())

        self.chunk40_10 = ast.literal_eval(open("Chunks/chunk40_10.txt").read())
        self.chunk40_11 = ast.literal_eval(open("Chunks/chunk40_11.txt").read())

        self.chunk41_0 = ast.literal_eval(open("Chunks/chunk41_0.txt").read())
        self.chunk41_1 = ast.literal_eval(open("Chunks/chunk41_1.txt").read())
        self.chunk41_2 = ast.literal_eval(open("Chunks/chunk41_2.txt").read())
        self.chunk41_3 = ast.literal_eval(open("Chunks/chunk41_3.txt").read())
        self.chunk41_4 = ast.literal_eval(open("Chunks/chunk41_4.txt").read())

        self.chunk42_0 = ast.literal_eval(open("Chunks/chunk42_0.txt").read())
        self.chunk42_1 = ast.literal_eval(open("Chunks/chunk42_1.txt").read())
        self.chunk42_2 = ast.literal_eval(open("Chunks/chunk39_2.txt").read())
        self.chunk42_3 = ast.literal_eval(open("Chunks/chunk42_3.txt").read())
        self.chunk42_4 = ast.literal_eval(open("Chunks/chunk42_4.txt").read())

        self.chunk43_0 = ast.literal_eval(open("Chunks/chunk39_2.txt").read())
        self.chunk43_1 = ast.literal_eval(open("Chunks/chunk39_2.txt").read())
        self.chunk43_2 = ast.literal_eval(open("Chunks/chunk39_2.txt").read())
        self.chunk43_3 = ast.literal_eval(open("Chunks/chunk43_3.txt").read())
        self.chunk43_4 = ast.literal_eval(open("Chunks/chunk43_4.txt").read())


        self.chunk_0 = [self.chunk0_0,self.chunk0_1,self.chunk0_2,self.chunk0_3,self.chunk0_4,self.chunk0_5,self.chunk0_6,self.chunk0_7,self.chunk0_8,self.chunk0_9,self.chunk0_10,self.chunk0_11,self.chunk0_12,self.chunk0_13,self.chunk0_14,self.chunk0_15,self.chunk0_16,self.chunk0_17,self.chunk0_18,self.chunk0_19,self.chunk0_20,self.chunk0_21]
        self.chunk_1 = [self.chunk1_0,self.chunk1_1,self.chunk1_2,self.chunk1_3,self.chunk1_4,self.chunk1_5,self.chunk1_6,self.chunk1_7,self.chunk1_8,self.chunk1_9,self.chunk1_10,self.chunk1_11,self.chunk1_12,self.chunk1_13,self.chunk1_14,self.chunk1_15,self.chunk1_16,self.chunk1_17,self.chunk1_18,self.chunk1_19,self.chunk1_20,self.chunk1_21]
        self.chunk_2 = [self.chunk2_0,self.chunk2_1,self.chunk2_2,self.chunk2_3,self.chunk2_4,self.chunk2_5,self.chunk2_6,self.chunk2_7,self.chunk2_8,self.chunk2_9,self.chunk2_10,self.chunk2_11,self.chunk2_12,self.chunk2_13,self.chunk2_14,self.chunk2_15,self.chunk2_16,self.chunk2_17,self.chunk2_18,self.chunk2_19,self.chunk2_20,self.chunk2_21]
        self.chunk_3 = [self.chunk3_0,self.chunk3_1,self.chunk3_2,self.chunk3_3,self.chunk3_4,self.chunk3_5,self.chunk3_6,self.chunk3_7,self.chunk3_8,self.chunk3_9,self.chunk3_10,self.chunk3_11,self.chunk3_12,self.chunk3_13,self.chunk3_14,self.chunk3_15,self.chunk3_16,self.chunk3_17,self.chunk3_18,self.chunk3_19,self.chunk3_20,self.chunk3_21]
        self.chunk_4 = [self.chunk4_0,self.chunk4_1,self.chunk4_2,self.chunk4_3,self.chunk4_4,self.chunk4_5,self.chunk4_6,self.chunk4_7,self.chunk4_8,self.chunk4_9,self.chunk4_10,self.chunk4_11,self.chunk4_12,self.chunk4_13,self.chunk4_14,self.chunk4_15,self.chunk4_16,self.chunk4_17,self.chunk4_18,self.chunk4_19,self.chunk4_20,self.chunk4_21]
        self.chunk_5 = [self.chunk5_0,self.chunk5_1,self.chunk5_2,self.chunk5_3,self.chunk5_4,self.chunk5_5,self.chunk5_6,self.chunk5_7,self.chunk5_8,self.chunk5_9,self.chunk5_10,self.chunk5_11,self.chunk5_12,self.chunk5_13,self.chunk5_14,self.chunk5_15,self.chunk5_16,self.chunk5_17,self.chunk5_18,self.chunk5_19,self.chunk5_20,self.chunk5_21]
        self.chunk_6 = [self.chunk6_0,self.chunk6_1,self.chunk6_2,self.chunk6_3,self.chunk6_4,self.chunk6_5,self.chunk6_6,self.chunk6_7,self.chunk6_8,self.chunk6_9,self.chunk6_10,self.chunk6_11,self.chunk6_12,self.chunk6_13,self.chunk6_14,self.chunk6_15,self.chunk6_16,self.chunk6_17,self.chunk6_18,self.chunk6_19,self.chunk6_20,self.chunk6_21]
        self.chunk_7 = [self.chunk7_0,self.chunk7_1,self.chunk7_2,self.chunk7_3,self.chunk7_4,self.chunk7_5,self.chunk7_6,self.chunk7_7,self.chunk7_8,self.chunk7_9,self.chunk7_10,self.chunk7_11,self.chunk7_12,self.chunk7_13,self.chunk7_14,self.chunk7_15,self.chunk7_16,self.chunk7_17,self.chunk7_18,self.chunk7_19,self.chunk7_20,self.chunk7_21]
        self.chunk_8 = [self.chunk8_0,self.chunk8_1,self.chunk8_2,self.chunk8_3,self.chunk8_4,self.chunk8_5,self.chunk8_6,self.chunk8_7,self.chunk8_8,self.chunk8_9,self.chunk8_10,self.chunk8_11,self.chunk8_12,self.chunk8_13,self.chunk8_14,self.chunk8_15,self.chunk8_16,self.chunk8_17,self.chunk8_18,self.chunk8_19,self.chunk8_20,self.chunk8_21]
        self.chunk_9 = [self.chunk9_0,self.chunk9_1,self.chunk9_2,self.chunk9_3,self.chunk9_4,self.chunk9_5,self.chunk9_6,self.chunk9_7,self.chunk9_8,self.chunk9_9,self.chunk9_10,self.chunk9_11,self.chunk9_12,self.chunk9_13,self.chunk9_14,self.chunk9_15,self.chunk9_16,self.chunk9_17,self.chunk9_18,self.chunk9_19,self.chunk9_20,self.chunk9_21]
        self.chunk_10 = [self.chunk10_0,self.chunk10_1,self.chunk10_2,self.chunk10_3,self.chunk10_4,self.chunk10_5,self.chunk10_6,self.chunk10_7,self.chunk10_8,self.chunk10_9,self.chunk10_10,self.chunk10_11,self.chunk10_12,self.chunk10_13,self.chunk10_14,self.chunk10_15,self.chunk10_16,self.chunk10_17,self.chunk10_18,self.chunk10_19,self.chunk10_20,self.chunk10_21]
        self.chunk_11= [self.chunk11_0,self.chunk11_1,self.chunk11_2,self.chunk11_3,self.chunk11_4,self.chunk11_5,self.chunk11_6,self.chunk11_7,self.chunk11_8,self.chunk11_9,self.chunk11_10,self.chunk11_11,self.chunk11_12,self.chunk11_13,self.chunk11_14,self.chunk11_15,self.chunk11_16,self.chunk11_17,self.chunk11_18,self.chunk11_19,self.chunk11_20,self.chunk11_21]
        self.chunk_12 = [self.chunk12_0,self.chunk12_1,self.chunk12_2,self.chunk12_3,self.chunk12_4,self.chunk12_5,self.chunk12_6,self.chunk12_7,self.chunk12_8,self.chunk12_9,self.chunk12_10,self.chunk12_11,self.chunk12_12,self.chunk12_13,self.chunk12_14,self.chunk12_15,self.chunk12_16,self.chunk12_17,self.chunk12_18,self.chunk12_19,self.chunk12_20,self.chunk12_21]
        self.chunk_13 = [self.chunk13_0,self.chunk13_1,self.chunk13_2,self.chunk13_3,self.chunk13_4,self.chunk13_5,self.chunk13_6,self.chunk13_7,self.chunk13_8,self.chunk13_9,self.chunk13_10,self.chunk13_11,self.chunk13_12,self.chunk13_13,self.chunk13_14,self.chunk13_15,self.chunk13_16,self.chunk13_17,self.chunk13_18,self.chunk13_19,self.chunk13_20,self.chunk13_21]
        self.chunk_14 = [self.chunk14_0,self.chunk14_1,self.chunk14_2,self.chunk14_3,self.chunk14_4,self.chunk14_5,self.chunk14_6,self.chunk14_7,self.chunk14_8,self.chunk14_9,self.chunk14_10,self.chunk14_11,self.chunk14_12,self.chunk14_13,self.chunk14_14,self.chunk14_15,self.chunk14_16,self.chunk14_17,self.chunk14_18,self.chunk14_19,self.chunk14_20,self.chunk14_21]
        self.chunk_15 = [self.chunk15_0,self.chunk15_1,self.chunk15_2,self.chunk15_3,self.chunk15_4,self.chunk15_5,self.chunk15_6,self.chunk15_7,self.chunk15_8,self.chunk15_9,self.chunk15_10,self.chunk15_11,self.chunk15_12,self.chunk15_13,self.chunk15_14,self.chunk15_15,self.chunk15_16,self.chunk15_17,self.chunk15_18,self.chunk15_19,self.chunk15_20,self.chunk15_21]
        self.chunk_16 = [self.chunk16_0,self.chunk16_1,self.chunk16_2,self.chunk16_3,self.chunk16_4,self.chunk16_5,self.chunk16_6,self.chunk16_7,self.chunk16_8,self.chunk16_9,self.chunk16_10,self.chunk16_11,self.chunk16_12,self.chunk16_13,self.chunk16_14,self.chunk16_15,self.chunk16_16,self.chunk16_17,self.chunk16_18,self.chunk16_19,self.chunk16_20,self.chunk16_21]
        self.chunk_17 = [self.chunk17_0,self.chunk17_1,self.chunk17_2,self.chunk17_3,self.chunk17_4,self.chunk17_5,self.chunk17_6,self.chunk17_7,self.chunk17_8,self.chunk17_9,self.chunk17_10,self.chunk17_11,self.chunk17_12,self.chunk17_13,self.chunk17_14,self.chunk17_15,self.chunk17_16,self.chunk17_17,self.chunk17_18,self.chunk17_19,self.chunk17_20,self.chunk17_21]
        self.chunk_18 = [self.chunk18_0,self.chunk18_1,self.chunk18_2,self.chunk18_3,self.chunk18_4,self.chunk18_5,self.chunk18_6,self.chunk18_7,self.chunk18_8,self.chunk18_9,self.chunk18_10,self.chunk18_11,self.chunk18_12,self.chunk18_13,self.chunk18_14,self.chunk18_15,self.chunk18_16,self.chunk18_17,self.chunk18_18,self.chunk18_19,self.chunk18_20,self.chunk18_21]
        self.chunk_19 = [self.chunk19_0,self.chunk19_1,self.chunk19_2,self.chunk19_3,self.chunk19_4,self.chunk19_5,self.chunk19_6,self.chunk19_7,self.chunk19_8,self.chunk19_9,self.chunk19_10,self.chunk19_11,self.chunk19_12,self.chunk19_13,self.chunk19_14,self.chunk19_15,self.chunk19_16,self.chunk19_17,self.chunk19_18,self.chunk19_19,self.chunk19_20,self.chunk19_21]
        self.chunk_20 = [self.chunk20_0,self.chunk20_1,self.chunk20_2,self.chunk20_3,self.chunk20_4,self.chunk20_5,self.chunk20_6,self.chunk20_7,self.chunk20_8,self.chunk20_9,self.chunk20_10,self.chunk20_11,self.chunk20_12,self.chunk20_13,self.chunk20_14,self.chunk20_15,self.chunk20_16,self.chunk20_17,self.chunk20_18,self.chunk20_19,self.chunk20_20,self.chunk20_21]
        self.chunk_21 = [self.chunk21_0,self.chunk21_1,self.chunk21_2,self.chunk21_3,self.chunk21_4,self.chunk21_5,self.chunk21_6,self.chunk21_7,self.chunk21_8,self.chunk21_9,self.chunk21_10,self.chunk21_11,self.chunk21_12,self.chunk21_13,self.chunk21_14,self.chunk21_15,self.chunk21_16,self.chunk21_17,self.chunk21_18,self.chunk21_19,self.chunk21_20,self.chunk21_21]
        self.chunk_22 = [self.chunk22_0,self.chunk22_1,self.chunk22_2,self.chunk22_3,self.chunk22_4,self.chunk22_5,self.chunk22_6,self.chunk22_7,self.chunk22_8,self.chunk22_9,self.chunk22_10,self.chunk22_11,self.chunk22_12,self.chunk22_13,self.chunk22_14,self.chunk22_15,self.chunk22_16,self.chunk22_17,self.chunk22_18,self.chunk22_19,self.chunk22_20,self.chunk22_21]
        self.chunk_23 = [self.chunk23_0,self.chunk23_1,self.chunk23_2,self.chunk23_3,self.chunk23_4,self.chunk23_5,self.chunk23_6,self.chunk23_7,self.chunk23_8,self.chunk23_9,self.chunk23_10,self.chunk23_11,self.chunk23_12,self.chunk23_13,self.chunk23_14,self.chunk23_15,self.chunk23_16,self.chunk23_17,self.chunk23_18,self.chunk23_19,self.chunk23_20,self.chunk23_21]
        self.chunk_24 = [self.chunk24_0,self.chunk24_1,self.chunk24_2,self.chunk24_3,self.chunk24_4,self.chunk24_5,self.chunk24_6,self.chunk24_7,self.chunk24_8,self.chunk24_9,self.chunk24_10,self.chunk24_11,self.chunk24_12,self.chunk24_13,self.chunk24_14,self.chunk24_15,self.chunk24_16,self.chunk24_17,self.chunk24_18,self.chunk24_19,self.chunk24_20,self.chunk24_21]
        self.chunk_25 = [self.chunk25_0,self.chunk25_1,self.chunk25_2,self.chunk25_3,self.chunk25_4,self.chunk25_5,self.chunk25_6,self.chunk25_7,self.chunk25_8,self.chunk25_9,self.chunk25_10,self.chunk25_11,self.chunk25_12,self.chunk25_13,self.chunk25_14,self.chunk25_15,self.chunk25_16,self.chunk25_17,self.chunk25_18,self.chunk25_19,self.chunk25_20,self.chunk25_21]
        self.chunk_26 = [self.chunk26_0,self.chunk26_1,self.chunk26_2,self.chunk26_3,self.chunk26_4,self.chunk26_5,self.chunk26_6,self.chunk26_7,self.chunk26_8,self.chunk26_9,self.chunk26_10,self.chunk26_11,self.chunk26_12,self.chunk26_13,self.chunk26_14,self.chunk26_15,self.chunk26_16,self.chunk26_17,self.chunk26_18,self.chunk26_19,self.chunk26_20,self.chunk26_21]
        self.chunk_27 = [self.chunk27_0,self.chunk27_1,self.chunk27_2,self.chunk27_3,self.chunk27_4,self.chunk27_5,self.chunk27_6,self.chunk27_7,self.chunk27_8,self.chunk27_9,self.chunk27_10,self.chunk27_11,self.chunk27_12,self.chunk27_13,self.chunk27_14,self.chunk27_15,self.chunk27_16,self.chunk27_17,self.chunk27_18,self.chunk27_19,self.chunk27_20,self.chunk27_21]
        self.chunk_28 = [self.chunk28_0,self.chunk28_1,self.chunk28_2,self.chunk28_3,self.chunk28_4,self.chunk28_5,self.chunk28_6,self.chunk28_7,self.chunk28_8,self.chunk28_9,self.chunk28_10,self.chunk28_11,self.chunk28_12,self.chunk28_13,self.chunk28_14,self.chunk28_15,self.chunk28_16,self.chunk28_17,self.chunk28_18,self.chunk28_19,self.chunk28_20,self.chunk28_21]
        self.chunk_29 = [self.chunk29_0,self.chunk29_1,self.chunk29_2,self.chunk29_3,self.chunk29_4,self.chunk29_5,self.chunk29_6,self.chunk29_7,self.chunk29_8,self.chunk29_9,self.chunk29_10,self.chunk29_11,self.chunk29_12,self.chunk29_13,self.chunk29_14,self.chunk29_15,self.chunk29_16,self.chunk29_17,self.chunk29_18,self.chunk29_19,self.chunk29_20,self.chunk29_21]
        self.chunk_30 = [self.chunk30_0,self.chunk30_1,self.chunk30_2,self.chunk30_3,self.chunk30_4,self.chunk30_5,self.chunk30_6,self.chunk30_7,self.chunk30_8,self.chunk30_9,self.chunk30_10,self.chunk30_11,self.chunk30_12,self.chunk30_13,self.chunk30_14,self.chunk30_15,self.chunk30_16,self.chunk30_17,self.chunk30_18,self.chunk30_19,self.chunk30_20,self.chunk30_21]
        self.chunk_31 = [self.chunk31_0,self.chunk31_1,self.chunk31_2,self.chunk31_3,self.chunk31_4,self.chunk31_5,self.chunk31_6,self.chunk31_7,self.chunk31_8,self.chunk31_9,self.chunk31_10,self.chunk31_11,self.chunk31_12,self.chunk31_13,self.chunk31_14,self.chunk31_15,self.chunk31_16,self.chunk31_17,self.chunk31_18,self.chunk31_19,self.chunk31_20,self.chunk31_21]
        self.chunk_32 = [self.chunk32_0,self.chunk32_1,self.chunk32_2,self.chunk32_3,self.chunk32_4,self.chunk32_5,self.chunk32_6,self.chunk32_7,self.chunk32_8,self.chunk32_9,self.chunk32_10,self.chunk32_11,self.chunk32_12,self.chunk32_13,self.chunk32_14,self.chunk32_15,self.chunk32_16,self.chunk32_17,self.chunk32_18,self.chunk32_19,self.chunk32_20,self.chunk32_21]
        self.chunk_33 = [self.chunk33_0,self.chunk33_1,self.chunk33_2,self.chunk33_3,self.chunk33_4,self.chunk33_5,self.chunk33_6,self.chunk33_7,self.chunk33_8,self.chunk33_9,self.chunk33_10,self.chunk33_11,self.chunk33_12,self.chunk33_13,self.chunk33_14,self.chunk33_15,self.chunk33_16,self.chunk33_17,self.chunk33_18,self.chunk33_19,self.chunk33_20,self.chunk33_21]
        self.chunk_34 = [self.chunk34_0,self.chunk34_1,self.chunk34_2,self.chunk34_3,self.chunk34_4,self.chunk34_5,self.chunk34_6,self.chunk34_7,self.chunk34_8,self.chunk34_9,self.chunk34_10,self.chunk34_11,self.chunk34_12,self.chunk34_13,self.chunk34_14,self.chunk34_15,self.chunk34_16,self.chunk34_17,self.chunk34_18,self.chunk34_19,self.chunk34_20,self.chunk34_21]
        self.chunk_35 = [self.chunk35_0,self.chunk35_1,self.chunk35_2,self.chunk35_3,self.chunk35_4,self.chunk35_5,self.chunk35_6,self.chunk35_7,self.chunk35_8,self.chunk35_9,self.chunk35_10,self.chunk35_11,self.chunk35_12,self.chunk35_13,self.chunk35_14,self.chunk35_15,self.chunk35_16,self.chunk35_17,self.chunk35_18,self.chunk35_19,self.chunk35_20,self.chunk35_21]
        self.chunk_36 = [self.chunk36_0,self.chunk36_1,self.chunk36_2,self.chunk36_3,self.chunk36_4,self.chunk36_5,self.chunk36_6,self.chunk36_7,self.chunk36_8,self.chunk36_9,self.chunk36_10,self.chunk36_11,self.chunk36_12,self.chunk36_13,self.chunk36_14,self.chunk36_15,self.chunk36_16,self.chunk36_17,self.chunk36_18,self.chunk36_19,self.chunk36_20,self.chunk36_21]
        self.chunk_37 = [self.chunk37_0,self.chunk37_1,self.chunk37_2,self.chunk37_3,self.chunk37_4,self.chunk37_5,self.chunk37_6,self.chunk37_7,self.chunk37_8,self.chunk37_9,self.chunk37_10,self.chunk37_11,self.chunk37_12,self.chunk37_13,self.chunk37_14,self.chunk37_15,self.chunk37_16,self.chunk37_17,self.chunk37_18,self.chunk37_19,self.chunk37_20,self.chunk37_21]
        self.chunk_38 = [self.chunk38_0,self.chunk38_1,self.chunk38_2,self.chunk38_3,self.chunk38_4,self.chunk38_5,self.chunk38_6,self.chunk38_7,self.chunk38_8,self.chunk38_9,self.chunk38_10,self.chunk38_11,self.chunk38_12,self.chunk38_13,self.chunk38_14,self.chunk38_15,self.chunk38_16,self.chunk38_17,self.chunk38_18,self.chunk38_19,self.chunk38_20,self.chunk38_21]
        self.chunk_39 = [self.chunk39_0,self.chunk39_1,self.chunk39_2,self.chunk39_3,self.chunk39_4,self.chunk39_5,self.chunk39_6,self.chunk39_7,self.chunk39_8,self.chunk39_9,self.chunk39_10,self.chunk39_11,self.chunk39_12]
        self.chunk_40 = [self.chunk40_0,self.chunk40_1,self.chunk40_2,self.chunk40_3,self.chunk40_4,self.chunk39_5,self.chunk39_6,self.chunk39_7,self.chunk39_8,self.chunk39_9,self.chunk40_10,self.chunk40_11]
        self.chunk_41 = [self.chunk41_0,self.chunk41_1,self.chunk41_2,self.chunk41_3,self.chunk41_4]
        self.chunk_42 = [self.chunk42_0,self.chunk42_1,self.chunk42_2,self.chunk42_3,self.chunk42_4]
        self.chunk_43 = [self.chunk43_0,self.chunk43_1,self.chunk43_2,self.chunk43_3,self.chunk43_4]
        
        self.world = [self.chunk_0,self.chunk_1,self.chunk_2,self.chunk_3,self.chunk_4,self.chunk_5,self.chunk_6,self.chunk_7,self.chunk_8,self.chunk_9,self.chunk_10,self.chunk_11,self.chunk_12,self.chunk_13,self.chunk_14,self.chunk_15,self.chunk_16,self.chunk_17,self.chunk_18,self.chunk_19,self.chunk_20,self.chunk_21,self.chunk_22,self.chunk_23,self.chunk_24,self.chunk_25,self.chunk_26,self.chunk_27,self.chunk_28,self.chunk_29,self.chunk_30,self.chunk_31,self.chunk_32,self.chunk_33,self.chunk_34,self.chunk_35,self.chunk_36,self.chunk_37,self.chunk_38,self.chunk_39,self.chunk_40,self.chunk_41,self.chunk_42,self.chunk_43]
        print("All Chunks loaded")
        self.ende = time.time()
        print('{:5.3f}s'.format(self.ende-self.start), end='  ')
        self.water_sea = Water_Sea()
        self.water_fluss = Water_Fluss()
        self.grass = Grass()
        self.Bergwand = Bergwand()
        self.Bergweg_Oben = Bergweg_Oben()
        self.Zaun = Zaun()
        self.Tree = Tree()
        self.Temple = Temple()
        self.StadtWeg = StatdtWeg()
        self.Schild = Schild()
        self.Sand = Sand()
        self.Questboard = questboard()
        self.QuestionMark = QuestionMark()
        self.PalastWandTop = Palast_Wand_Top()
        self.PalastWand = Palast_Wand()
        self.PalastTreppe = Palast_Treppe()
        self.PalastTor = Palast_Tor()
        self.Palast = Palast()
        self.House1 = House1()
        self.House2 = House2()
        self.House3 = House3()
        self.House4 = House4()
        self.Höhleneingang = Höhleneingang()
        self.Firtree = Firtree()
        self.Exclamationmark = Exclamation_Mark()
        self.Durchsichtig = Durchsichtig()
        self.Dummy = Dummy()
        self.Door4 = Door4()
        self.Door3 = Door3()
        self.Door2 = Door2()
        self.Door1 = Door1()
        self.Dirtweg = Dirt_Weg()
        self.Brücke = Brucke()
        self.BergwegZenter = Bergweg_Zenter()
        self.Bergwegunten = Bergweg_unten()
        self.Stein = Stein()

        self.Altar = Altar()
        self.Fackel = Fackel()
        self.Schwarzes_Rechteck = Schwarzes_Rechteck()
        self.Haus_innen_Wand_Ecke_links_oben_Final = Haus_innen_Wand_Ecke_links_oben_Final()
        self.Haus_innen_Wand_Ecke_links_unten_Final = Haus_innen_Wand_Ecke_links_unten_Final()
        self.Haus_innen_Wand_Ecke_rechts_oben_Final = Haus_innen_Wand_Ecke_rechts_oben_Final()
        self.Haus_innen_Wand_Ecke_recht_unten_Final = Haus_innen_Wand_Ecke_recht_unten_Final()
        self.Haus_innen_Wand_links_Final = Haus_innen_Wand_links_Final()
        self.Haus_innen_Wand_oben_FInal = Haus_innen_Wand_oben_FInal()
        self.Haus_innen_Wand_rechts_Final = Haus_innen_Wand_rechts_Final()
        self.Haus_innen_Wand_unten_Final = Haus_innen_Wand_unten_Final()
        self.Haus_Wand_Visible__Front__Final = Haus_Wand_Visible__Front__Final()
        self.Palast_Boden = Palast_Boden()
        self.Palast_Wand_Ecke_Links_Oben = Palast_Wand_Ecke_Links_Oben()
        self.Palast_Wand_Ecke_Links_Unten = Palast_Wand_Ecke_Links_Unten()
        self.Fountain = fountain()
        self.Palast_Wand_Ecke_Rechts_Oben = Palast_Wand_Ecke_Rechts_Oben()
        self.Palast_Wand_Ecke_Rechts_Unten = Palast_Wand_Ecke_Rechts_Unten()
        self.Palast_Wand_Front_Rest = Palast_Wand_Front_Rest()
        self.Palast_Wand_Front_Verbindung_Zum_Boden = Palast_Wand_Front_Verbindung_Zum_Boden()
        self.Palast_Wand_Links = Palast_Wand_Links()
        self.Palast_Wand_Oben = Palast_Wand_Oben()
        self.Palast_Wand_Rechts = Palast_Wand_Rechts()
        self.Palast_Wand_unten = Palast_Wand_unten()
        self.Regal_Final_ = Regal_Final_()
        self.Stuhl_Final_links_schauend = Stuhl_Final_links_schauend()
        self.Stuhl_Final_rechts_schauend = Stuhl_Final_rechts_schauend()
        self.Tempel_Boden = Tempel_Boden()
        self.Tempel_Wand_Ecke_Links_Oben = Tempel_Wand_Ecke_Links_Oben()
        self.Tempel_Wand_Ecke_Links_Unten = Tempel_Wand_Ecke_Links_Unten()
        self.Tempel_Wand_Ecke_Rechts_Oben = Tempel_Wand_Ecke_Rechts_Oben()
        self.Tempel_Wand_Ecke_Rechts_Unten = Tempel_Wand_Ecke_Rechts_Unten()
        self.Tempel_Wand_Front_Rest = Tempel_Wand_Front_Rest()
        self.Tempel_Wand_Front_Verbindung_Zum_Boden = Tempel_Wand_Front_Verbindung_Zum_Boden()
        self.Tempel_Wand_Links = Tempel_Wand_Links()
        self.Tempel_Wand_Oben = Tempel_Wand_Oben()
        self.Tempel_Wand_Rechts = Tempel_Wand_Rechts()
        self.Tempel_Wand_Unten = Tempel_Wand_Unten()
        self.Tisch_Final = Tisch_Final()
        self.Schwarzes_Rechteck = Schwarzes_Rechteck()

        self.cave_bottommiddle = cave_bottommiddle()
        self.Cave_floor = Cave_floor()
        self.cave_leftwall = cave_leftwall()
        self.cave_rightwall = cave_rightwall()
        self.cave_topmiddle = cave_topmiddle()

    def update_world(self,screen,chunkx,chunky):
        actual_chunk = self.world[chunkx]
        actual_chunk = actual_chunk[chunky]
        for a in actual_chunk:
            if a[0] == "Gras_Kuste":
                self.grass.paint(screen,a[1],a[2])
            if a[0] == "Wasser_Ozean":
                self.water_sea.paint(screen,a[1],a[2])
            if a[0] == "Wasser_Fluss":
                self.water_fluss.paint(screen,a[1],a[2])
            if a[0] == "Baum1":
                self.Tree.paint(screen,a[1],a[2])
            if a[0] == "Baum2":
                self.Firtree.paint(screen,a[1],a[2])
            if a[0] == "Durchsichtig":
                self.Durchsichtig.paint(screen,a[1],a[2])
            if a[0] == "Dirt_Weg":
                self.Dirtweg.paint(screen,a[1],a[2])
            if a[0] == "Stadt_Weg":
                self.StadtWeg.paint(screen,a[1],a[2])
            if a[0] == "Bergweg_oben":
                self.Bergweg_Oben.paint(screen,a[1],a[2])

            if a[0] == "Bergweg_mitte":
                self.BergwegZenter.paint(screen,a[1],a[2])
            if a[0] == "Bergweg_unten":
                self.Bergwegunten.paint(screen,a[1],a[2])
            if a[0] == "Berg":
                self.Bergwand.paint(screen,a[1],a[2])
            if a[0] == "Hoehleneingang":
                self.Höhleneingang.paint(screen,a[1],a[2])

            if a[0] == "Sand":
                self.Sand.paint(screen,a[1],a[2])
            if a[0] == "House_1":
                self.House1.paint(screen,a[1],a[2])
            if a[0] == "House_2":
                self.House2.paint(screen,a[1],a[2])
            if a[0] == "House_3":
                self.House3.paint(screen,a[1],a[2])
            if a[0] == "House_4":
                self.House4.paint(screen,a[1],a[2])

            if a[0] == "Temple":
                self.Temple.paint(screen,a[1],a[2])
            if a[0] == "Palast_Außen_Tor":
                self.PalastTor.paint(screen,a[1],a[2])
            if a[0] == "Palast_Außen_Wand":
                self.PalastWand.paint(screen,a[1],a[2])
            if a[0] == "Palast_Außen_Wand_Top":
                self.PalastWandTop.paint(screen,a[1],a[2])

            if a[0] == "Palast_Außen":
                self.Palast.paint(screen,a[1],a[2])
            if a[0] == "Palast_Außen_Treppe":
                self.PalastTreppe.paint(screen,a[1],a[2])
            if a[0] == "Zaun":
                self.Zaun.paint(screen,a[1],a[2])
            if a[0] == "Stein":
                self.Stein.paint(screen,a[1],a[2])

            if a[0] == "Schwarzes_Rechteck":
                self.Schwarzes_Rechteck.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Boden":
                self.Tempel_Boden.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Ecke_Links_Oben":
                self.Tempel_Wand_Ecke_Links_Oben.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Ecke_Links_Unten":
                self.Tempel_Wand_Ecke_Links_Unten.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Ecke_Rechts_Oben":
                self.Tempel_Wand_Ecke_Rechts_Oben.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Ecke_Rechts_Unten":
                self.Tempel_Wand_Ecke_Rechts_Unten.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Front_Rest":
                self.Tempel_Wand_Front_Rest.paint(screen,a[1],a[2])


            if a[0] == "Tempel_Wand_Front_Verbindung_Zum_Boden":
                self.Tempel_Wand_Front_Verbindung_Zum_Boden.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Links":
                self.Tempel_Wand_Links.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Rechts":
                self.Tempel_Wand_Rechts.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Oben":
                self.Tempel_Wand_Oben.paint(screen,a[1],a[2])
            if a[0] == "Tempel_Wand_Unten":
                self.Tempel_Wand_Unten.paint(screen,a[1],a[2])


            if a[0] == "Altar":
                self.Altar.paint(screen,a[1],a[2])
            if a[0] == "Fackel":
                self.Fackel.paint(screen,a[1],a[2])
            if a[0] == "Fountain":
                self.Fountain.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_Ecke_links_oben_Final":
                self.Haus_innen_Wand_Ecke_links_oben_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_Ecke_links_unten_Final":
                self.Haus_innen_Wand_Ecke_links_unten_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_Ecke_recht_unten_Final":
                self.Haus_innen_Wand_Ecke_recht_unten_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_Ecke_rechts_oben_Final":
                self.Haus_innen_Wand_Ecke_rechts_oben_Final.paint(screen,a[1],a[2])


            if a[0] == "Haus_innen_Wand_links_Final":
                self.Haus_innen_Wand_links_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_oben_FInal":
                self.Haus_innen_Wand_oben_FInal.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_rechts_Final":
                self.Haus_innen_Wand_rechts_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_innen_Wand_unten_Final":
                self.Haus_innen_Wand_unten_Final.paint(screen,a[1],a[2])
            if a[0] == "Haus_Wand_Visible__Front__Final":
                self.Haus_Wand_Visible__Front__Final.paint(screen,a[1],a[2])


            if a[0] == "Palast_Boden":
                self.Palast_Boden.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Ecke_Links_Oben":
                self.Palast_Wand_Ecke_Links_Oben.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Ecke_Links_Unten":
                self.Palast_Wand_Ecke_Links_Unten.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Ecke_Rechts_Oben":
                self.Palast_Wand_Ecke_Rechts_Oben.paint(screen,a[1],a[2])

            if a[0] == "Palast_Wand_Ecke_Rechts_Unten":
                self.Palast_Wand_Ecke_Rechts_Unten.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Front_Rest":
                self.Palast_Wand_Front_Rest.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Front_Verbindung_Zum_Boden":
                self.Palast_Wand_Front_Verbindung_Zum_Boden.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Links":
                self.Palast_Wand_Links.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Rechts":
                self.Palast_Wand_Rechts.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_Oben":
                self.Palast_Wand_Oben.paint(screen,a[1],a[2])
            if a[0] == "Palast_Wand_unten":
                self.Palast_Wand_unten.paint(screen,a[1],a[2])
            if a[0] == "Regal_Final_":
                self.Regal_Final_.paint(screen,a[1],a[2])
            if a[0] == "Stuhl_Final_links_schauend":
                self.Stuhl_Final_links_schauend.paint(screen,a[1],a[2])


            if a[0] == "Stuhl_Final_rechts_schauend":
                self.Stuhl_Final_rechts_schauend.paint(screen,a[1],a[2])
            if a[0] == "Tisch_Final":
                self.Tisch_Final.paint(screen,a[1],a[2])

            if a[0] == "Schwarzes_Rechteck":
                self.Schwarzes_Rechteck.paint(screen,a[1],a[2])
            if a[0] == "Cave_Floor":
                self.Cave_floor.paint(screen,a[1],a[2])
            if a[0] == "Cave_leftwall":
                self.cave_leftwall.paint(screen,a[1],a[2])
            if a[0] == "cave_rightwall":
                self.cave_rightwall.paint(screen,a[1],a[2])
            if a[0] == "cave_topmiddle":
                self.cave_topmiddle.paint(screen,a[1],a[2])
            if a[0] == "cave_bottommiddle":
                self.cave_bottommiddle.paint(screen,a[1],a[2])

    def give_me_my_chunk(self,chunkx,chunky):
        actual_chunk = self.world[chunkx]
        actual_chunk = actual_chunk[chunky]
        return(actual_chunk)
            

#myWolrd = gameworld()
#myWolrd.update_world(3,15)
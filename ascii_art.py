#!/usr/bin/env python
# -*- coding: utf-8 -*-

dragon_ascii = """\

11111111111111111111111111111111111111001111111111111111111111111
11111111111111111111111111111111111100011111111111111111111111111
11111111111111111111111111111111100001111111111111111111111111111
11111111111111111111111111111110000111111111111111111111111111111
11111111111111111111111111111000000111111111111111111111111111111
11111111111111111111111111100000011110001100000000000000011111111
11111111111111111100000000000000000000000000000000011111111111111
11111111111111110111000000000000000000000000000011111111111111111
11111111111111111111111000000000000000000000000000000000111111111
11111111111111111110000000000000000000000000000000111111111111111
11111111111111111100011100000000000000000000000000000111111111111
11111111111111100000110000000000011000000000000000000011111111111
11111111111111000000000000000100111100000000000001100000111111111
11111111110000000000000000001110111110000000000000111000011111111
11111111000000000000000000011111111100000000000000011110001111111
11111110000000011111111111111111111100000000000000001111100111111
11111111000001111111111111111111110000000000000000001111111111111
11111111110111111111111111111100000000000000000000000111111111111
11111111111111110000000000000000000000000000000000000111111111111
11111111111111111100000000000000000000000000001100000111111111111
11111111111111000000000000000000000000000000111100000111111111111
11111111111000000000000000000000000000000001111110000111111111111
11111111100000000000000000000000000000001111111110000111111111111
11111110000000000000000000000000000000111111111110000111111111111
11111100000000000000000001110000001111111111111110001111111111111
11111000000000000000011111111111111111111111111110011111111111111
11110000000000000001111111111111111100111111111111111111111111111
11100000000000000011111111111111111111100001111111111111111111111
11100000000001000111111111111111111111111000001111111111111111111
11000000000001100111111111111111111111111110000000111111111111111
11000000000000111011111111111100011111000011100000001111111111111
11000000000000011111111111111111000111110000000000000011111111111
11000000000000000011111111111111000000000000000000000000111111111
11001000000000000000001111111110000000000000000000000000001111111
11100110000000000001111111110000000000000000111000000000000111111
11110110000000000000000000000000000000000111111111110000000011111
11111110000000000000000000000000000000001111111111111100000001111
11111110000010000000000000000001100000000111011111111110000001111
11111111000111110000000000000111110000000000111111111110110000111
11111110001111111100010000000001111100000111111111111111110000111
11111110001111111111111110000000111111100000000111111111111000111
11111111001111111111111111111000000111111111111111111111111100011
11111111101111111111111111111110000111111111111111111111111001111
11111111111111111111111111111110001111111111111111111111100111111
11111111111111111111111111111111001111111111111111111111001111111
11111111111111111111111111111111100111111111111111111111111111111
11111111111111111111111111111111110111111111111111111111111111111

"""
mind = """\

01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101

"""

level_one_ascii = """\

*    ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗    ████████╗██████╗     ██╗    █████████╗   ███████████╗          ██████╗███╗   █████████╗
 *    ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝    ╚══██╔══██╔═══██╗    ██║    ██╔════██║   ████╔════██║         ██╔═══██████╗  ████╔════╝
 *    ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗         ██║  ██║   ██║    ██║    █████╗ ██║   ███████╗ ██║         ██║   ████╔██╗ ███████╗
 *    ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝         ██║  ██║   ██║    ██║    ██╔══╝ ╚██╗ ██╔██╔══╝ ██║         ██║   ████║╚██╗████╔══╝
 *    ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗       ██║  ╚██████╔╝    ██████████████╗╚████╔╝██████████████╗    ╚██████╔██║ ╚███████████╗
 *     ╚══╝╚══╝╚══════╚══════╝╚═════╝╚═════╝╚═╝     ╚═╚══════╝       ╚═╝   ╚═════╝     ╚══════╚══════╝ ╚═══╝ ╚══════╚══════╝     ╚═════╝╚═╝  ╚═══╚══════╝
 *

"""


end_level_one_ascii = """\

*    ██████████╗   ████████╗     ██╗    █████████╗   ███████████╗          ██████╗███╗   █████████╗
 *    ██╔════████╗  ████╔══██╗    ██║    ██╔════██║   ████╔════██║         ██╔═══██████╗  ████╔════╝
 *    █████╗ ██╔██╗ ████║  ██║    ██║    █████╗ ██║   ███████╗ ██║         ██║   ████╔██╗ ███████╗
 *    ██╔══╝ ██║╚██╗████║  ██║    ██║    ██╔══╝ ╚██╗ ██╔██╔══╝ ██║         ██║   ████║╚██╗████╔══╝
 *    █████████║ ╚██████████╔╝    ██████████████╗╚████╔╝██████████████╗    ╚██████╔██║ ╚███████████╗
 *    ╚══════╚═╝  ╚═══╚═════╝     ╚══════╚══════╝ ╚═══╝ ╚══════╚══════╝     ╚═════╝╚═╝  ╚═══╚══════╝
 *

"""

level_two_ascii = """\

 *    ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗    ████████╗██████╗     ██╗    █████████╗   ███████████╗         ██████████╗    ██╗██████╗
 *    ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝    ╚══██╔══██╔═══██╗    ██║    ██╔════██║   ████╔════██║         ╚══██╔══██║    ████╔═══██╗
 *    ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗         ██║  ██║   ██║    ██║    █████╗ ██║   ███████╗ ██║            ██║  ██║ █╗ ████║   ██║
 *    ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝         ██║  ██║   ██║    ██║    ██╔══╝ ╚██╗ ██╔██╔══╝ ██║            ██║  ██║███╗████║   ██║
 *    ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗       ██║  ╚██████╔╝    ██████████████╗╚████╔╝██████████████╗       ██║  ╚███╔███╔╚██████╔╝
 *     ╚══╝╚══╝╚══════╚══════╝╚═════╝╚═════╝╚═╝     ╚═╚══════╝       ╚═╝   ╚═════╝     ╚══════╚══════╝ ╚═══╝ ╚══════╚══════╝       ╚═╝   ╚══╝╚══╝ ╚═════╝
 *

"""

level_three_ascii = """\

*    ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗    ████████╗██████╗     ██╗    █████████╗   ███████████╗         ██████████╗  ████████╗██████████████╗
 *    ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝    ╚══██╔══██╔═══██╗    ██║    ██╔════██║   ████╔════██║         ╚══██╔══██║  ████╔══████╔════██╔════╝
 *    ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗         ██║  ██║   ██║    ██║    █████╗ ██║   ███████╗ ██║            ██║  █████████████╔█████╗ █████╗
 *    ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝         ██║  ██║   ██║    ██║    ██╔══╝ ╚██╗ ██╔██╔══╝ ██║            ██║  ██╔══████╔══████╔══╝ ██╔══╝
 *    ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗       ██║  ╚██████╔╝    ██████████████╗╚████╔╝██████████████╗       ██║  ██║  ████║  ████████████████╗
 *     ╚══╝╚══╝╚══════╚══════╝╚═════╝╚═════╝╚═╝     ╚═╚══════╝       ╚═╝   ╚═════╝     ╚══════╚══════╝ ╚═══╝ ╚══════╚══════╝       ╚═╝  ╚═╝  ╚═╚═╝  ╚═╚══════╚══════╝
 *

 """

SPACE_SMALL_ASCII = """\
\n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
"""
SPACE_LARGE_ASCII = """\
        \n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
        \n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
        \n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
        \n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
        \n . . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .. . . . .
        \n"""
HASH_ACSII = "############################################################"

def dragon():
    print dragon_ascii

def level_one_text():
    print level_one_ascii

def end_level_one_text():
    print end_level_one_ascii

def level_two_text():
    print level_two_ascii

def level_three_text():
    print level_three_ascii

def small_space():
    print SPACE_SMALL_ASCII

def large_space():
    print SPACE_LARGE_ASCII

def hash():
    print HASH_ACSII

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWords(RPackage):
	"""List of English Words from the Scrabble Dictionary

	List of english scrabble words as listed in the OTCWL2014
    <https://www.scrabbleplayers.org/w/Official_Tournament_and_Club_Word_List_2014_Edition>.
    Words are collated from the 'Word Game Dictionary' <https://www.wordgamedictionary.com/word-lists/>.
	"""
	
	cran = "words" 

	version("1.0.1", md5="eb49514ad9b75df72ac3aea82ba6a22f")

	depends_on("r@2.10:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemnetdictionaries(RPackage):
	"""Dictionaries for the 'SemNetCleaner' Package

	Implements dictionaries that can be used in the 'SemNetCleaner' package. Also includes several functions aimed at facilitating the text cleaning analysis in the 'SemNetCleaner' package. This package is designed to integrate and update word lists and dictionaries based on each user's individual needs by allowing users to store and save their own dictionaries. Dictionaries can be added to the 'SemNetDictionaries' package by submitting user-defined dictionaries to <https://github.com/AlexChristensen/SemNetDictionaries>.
	"""
	
	homepage = "https://github.com/AlexChristensen/SemNetDictionaries"
	cran = "SemNetDictionaries" 

	version("0.2.0", md5="f528667c308bed12ce2593b6286d5521")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-easycsv", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))

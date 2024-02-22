# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterlinear(RPackage):
	"""Importing Interlinearized Corpora and Dictionaries as Produced
by Descriptive Linguistics Software

	Interlinearized glossed texts (IGT) are used in descriptive linguistics for
 representing a morphological analysis of a text through a morpheme-by-morpheme gloss.
 'InterlineaR' provide a set of functions that targets several popular formats of IGT
 ('SIL Toolbox', 'EMELD XML') and that turns an IGT into a set of data frames following
 a relational model (the tables represent the different linguistic units: texts,
 sentences, word, morphems).
 The same pieces of software ('SIL FLEX', 'SIL Toolbox') typically produce dictionaries
 of the morphemes used in the glosses. 'InterlineaR' provide a function for turning
 the LIFT XML dictionary format into a set of data frames following a relational model
 in order to represent the dictionary entries, the sense(s) attached to the entries,
 the example(s) attached to senses, etc.
	"""
	
	homepage = "https://github.com/sylvainloiseau/interlineaR"
	cran = "interlineaR" 

	version("1.0", md5="dd556b03d7b5099b0341e9558cd79b0c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArabicstemr(RPackage):
	"""Arabic Stemmer for Text Analysis

	Allows users to stem Arabic texts for text analysis.
	"""
	
	cran = "arabicStemR" 

	version("1.3", md5="5fb4d93c4a82fd6a37d5e9e09432e949")


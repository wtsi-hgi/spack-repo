# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersianstemmer(RPackage):
	"""Persian Stemmer for Text Analysis

	Allows users to stem Persian texts for text analysis.
	"""
	
	cran = "PersianStemmer" 

	version("1.0", md5="eea6d2a84cacc3138064496e8c6688be")


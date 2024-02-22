# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexicon(RPackage):
	"""Lexicons for Text Analysis

	A collection of lexical hash tables, dictionaries, and word lists.
	"""
	
	homepage = "https://github.com/trinker/lexicon"
	cran = "lexicon" 

	version("1.2.1", md5="60310140e40295a076b5f281237128e9")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-syuzhet@1.0.1:", type=("build", "run"))

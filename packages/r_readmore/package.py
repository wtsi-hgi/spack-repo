# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmore(RPackage):
	"""Utilities for Importing and Manipulating Biomedical Data Files

	Tools to read various file types into one list of data structures, usually, but not limited to, data frames.
  Excel files are read sheet-wise, i.e., all or a selection of sheets can be read. Field delimiters and decimal
  separators are determined automatically.
	"""
	
	cran = "readmoRe" 

	version("0.2-12", md5="a938f6320e58a7c321b9d47262d6edba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

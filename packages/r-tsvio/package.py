# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsvio(RPackage):
	"""Simple Utilities for Tab-Separated-Value (TSV) Files

	Utilities for rapidly loading specified rows and/or columns of data from large tab-separated value (tsv) files (large: e.g. 1 GB file of 10000 x 10000 matrix). 'tsvio' is an R wrapper to 'C' code that creates an index file for the rows of the tsv file, and uses that index file to collect rows and/or columns from the tsv file without reading the whole file into memory.
	"""
	
	homepage = "https://github.com/MD-Anderson-Bioinformatics/tsvio"
	cran = "tsvio" 

	version("1.0.6", md5="8b0fbfb5ed1bf8ededc94e02d8eb97cd")

	depends_on("r@3.4:", type=("build", "run"))

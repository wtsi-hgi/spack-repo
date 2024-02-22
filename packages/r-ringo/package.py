# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRingo(RPackage):
	"""R Investigation of ChIP-chip Oligoarrays

	The package Ringo facilitates the primary analysis of ChIP-chip data. The main functionalities of the package are data read-in, quality assessment, data visualisation and identification of genomic regions showing enrichment in ChIP-chip. The package has functions to deal with two-color oligonucleotide microarrays from NimbleGen used in ChIP-chip projects, but also contains more general functions for ChIP-chip data analysis, given that the data is supplied as RGList (raw) or ExpressionSet (pre- processed). The package employs functions from various other packages of the Bioconductor project and provides additional ChIP-chip-specific and NimbleGen-specific functionalities.
	"""
	
	bioc = "Ringo" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Ringo_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Ringo/Ringo_1.66.0.tar.gz"]

	version("1.66.0", md5="2aa9ffb65c3d24fed5141f139f8721ab")

	depends_on("r-biobase@1.14.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.11:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))

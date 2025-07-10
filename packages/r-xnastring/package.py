# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXnastring(RPackage):
	"""Efficient Manipulation of Modified Oligonucleotide Sequences

	The XNAString package allows for description of base sequences and associated chemical modifications in a single object. XNAString is able to capture single stranded, as well as double stranded molecules. Chemical modifications are represented as independent strings associated with different features of the molecules (base sequence, sugar sequence, backbone sequence, modifications) and can be read or written to a HELM notation. It also enables secondary structure prediction using RNAfold from ViennaRNA. XNAString is designed to be efficient representation of nucleic-acid based therapeutics, therefore it stores information about target sequences and provides interface for matching and alignment functions from Biostrings package.
	"""
	
	bioc = "XNAString" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/XNAString_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/XNAString/XNAString_1.10.0.tar.gz"]

	version("1.10.0", sha256="c44309572ddb39a3ee070c747fcb7ce08acd226e133c8bc3e9f9eefb5673873c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))

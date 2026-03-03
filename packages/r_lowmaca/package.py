# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowmaca(RPackage):
	"""LowMACA - Low frequency Mutation Analysis via Consensus Alignment

	The LowMACA package is a simple suite of tools to investigate and analyze the mutation profile of several proteins or pfam domains via consensus alignment. You can conduct an hypothesis driven exploratory analysis using our package simply providing a set of genes or pfam domains of your interest.
	"""
	
	bioc = "LowMACA" 

	version("1.31.0", commit="717c5ece3d6724f166f6a1ed95a6665627515a0b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cbioportaldata", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lowmacaannotation", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("ghostscript", type=("build", "link", "run"))
	depends_on("perl", type=("build", "link", "run"))

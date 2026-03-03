# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenehapr(RPackage):
	"""Gene Haplotype Statistics, Phenotype Association and
Visualization

	Import genome variants data and perform gene haplotype Statistics, 
  visualization and phenotype association with 'R'. 
	"""
	
	cran = "geneHapR" 

	version("1.2.4", md5="452941a2419edb095fd9166725da7657")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-genetics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-lolliplot", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))

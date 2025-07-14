# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComapr(RPackage):
	"""Crossover analysis and genetic map construction

	comapr detects crossover intervals for single gametes from their haplotype states sequences and stores the crossovers in GRanges object. The genetic distances can then be calculated via the mapping functions using estimated crossover rates for maker intervals. Visualisation functions for plotting interval-based genetic map or cumulative genetic distances are implemented, which help reveal the variation of crossovers landscapes across the genome and across individuals.
	"""
	
	bioc = "comapr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/comapr_1.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/comapr/comapr_1.6.1.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.1", sha256="ac101714233d406338b6ac5022d3547b6ba65939806bad7bae4744948952718e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))

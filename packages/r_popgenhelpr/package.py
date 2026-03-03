# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopgenhelpr(RPackage):
	"""Streamline Population Genomic and Genetic Analyses

	Estimate commonly used population genomic statistics and generate publication quality figures. The current version of 'PopGenHelpR' uses vcf and csv files to generate output, however, future implementations will expand the input file type options.
	"""
	
	homepage = "https://kfarleigh.github.io/PopGenHelpR/"
	cran = "PopGenHelpR" 

	version("1.2.1", md5="c0a26ac50f020d7ea6d38a7deed17517")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-dartr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-hierfstat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-poppr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scatterpie", type=("build", "run"))
	depends_on("r-stampp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))

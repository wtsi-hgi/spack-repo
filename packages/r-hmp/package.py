# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmp(RPackage):
	"""Hypothesis Testing and Power Calculations for Comparing
Metagenomic Samples from HMP

	Using Dirichlet-Multinomial distribution to provide several functions for formal hypothesis testing, power and sample size calculations for human microbiome experiments.
	"""
	
	cran = "HMP" 

	version("2.0.1", md5="d1d223ac3be1acfbca5ee9ee7222d9e1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))

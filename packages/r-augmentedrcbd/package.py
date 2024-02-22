# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAugmentedrcbd(RPackage):
	"""Analysis of Augmented Randomised Complete Block Designs

	Functions for analysis of data generated from experiments in
    augmented randomised complete block design according to Federer, W.T.
    (1961) <doi:10.2307/2527837>. Computes analysis of variance, adjusted
    means, descriptive statistics, genetic variability statistics etc.
    Further includes data visualization and report generation functions.
	"""
	
	homepage = "https://github.com/aravind-j/augmentedRCBD"
	cran = "augmentedRCBD" 

	version("0.1.7", md5="ac6fb34aa96c1ec2d8401cfe66ce8128")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-numform", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))

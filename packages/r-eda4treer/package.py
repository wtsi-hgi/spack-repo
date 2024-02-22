# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REda4treer(RPackage):
	"""Experimental Design and Analysis for Tree Improvement

	Provides data sets and R Codes for E.R. Williams, C.E. Harwood and A.C. Matheson (2023). Experimental Design and Analysis for Tree Improvement, CSIRO Publishing.
	"""
	
	homepage = "https://github.com/MYaseen208/eda4treeR"
	cran = "eda4treeR" 

	version("0.6.0", md5="a8760b2b91a4f77d5a41fa0c7b979e2e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-predictmeans", type=("build", "run"))
	depends_on("r-supernova", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurger(RPackage):
	"""Inbreeding-Purging Estimation in Pedigreed Populations

	Inbreeding-purging analysis of pedigreed populations, including the computation of the inbreeding coefficient, partial, ancestral and purged inbreeding coefficients, and measures of the opportunity of purging related to the individual reduction of inbreeding load.
    In addition, functions to calculate the effective population size and other parameters relevant to population genetics are included.
    See López-Cortegano E. (2021) <doi:10.1093/bioinformatics/btab599>.
	"""
	
	homepage = "https://gitlab.com/elcortegano/purgeR/"
	cran = "purgeR" 

	version("1.8.2", md5="c3da8a6e4c68faf2256736597e7ae801")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dosnow@1.0.19:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))

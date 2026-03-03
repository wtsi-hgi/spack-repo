# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REurosarcbayes(RPackage):
	"""Bayesian Single Arm Sample Size Calculation Software

	Bayesian sample size calculation software and examples for EuroSARC
    clinical trials which utilise Bayesian methodology. These trials rely on
    binomial based endpoints so the majority of programs found here relate to this
    sort of endpoint. Developed as part of the EuroSARC FP7 grant.
	"""
	
	cran = "EurosarcBayes" 

	version("1.1", md5="4605730c55c78d456e129def542d012d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))

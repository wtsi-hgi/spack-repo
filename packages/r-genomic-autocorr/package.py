# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicAutocorr(RPackage):
	"""Models Dealing with Spatial Dependency in Genomic Data

	Local structure in genomic data often induces dependence between observations taken at different genomic locations.  Ignoring this dependence leads to underestimation of the standard error of parameter estimates.  This package uses block bootstrapping to estimate asymptotically correct standard errors of parameters from any standard generalised linear model that may be fit by the glm() function.
	"""
	
	homepage = "https://github.com/chr1swallace/genomic.autocorr"
	cran = "genomic.autocorr" 

	version("1.0-1", md5="01bfdf59daf0452f3a5b52de4996c5ae")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))

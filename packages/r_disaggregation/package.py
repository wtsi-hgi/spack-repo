# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisaggregation(RPackage):
	"""Disaggregation Modelling

	Fits disaggregation regression models using 'TMB' ('Template Model
    Builder'). When the response data are aggregated to polygon level but
    the predictor variables are at a higher resolution, these models can be
    useful. Regression models with spatial random fields. The package is 
    described in detail in Nandi et al. (2023) <doi:10.18637/jss.v106.i11>.
	"""
	
	cran = "disaggregation" 

	version("0.3.0", md5="7cc8be0776390573e33b54197dce6140")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-sparsemvn", type=("build", "run"))
	depends_on("r-fmesher", type=("build", "run"))
	depends_on("r-tidyterra", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDid2s(RPackage):
	"""Two-Stage Difference-in-Differences Following Gardner (2021)

	Estimates Two-way Fixed Effects difference-in-differences/event-study models using the approach proposed by Gardner (2021) <doi:10.48550/arXiv.2207.05943>. To avoid the problems caused by OLS estimation of the Two-way Fixed Effects model, this function first estimates the fixed effects and covariates using untreated observations and then in a second stage, estimates the treatment effects.
	"""
	
	homepage = "https://kylebutts.github.io/did2s/"
	cran = "did2s" 

	version("1.0.2", md5="5ec81203159f657e95c127791eee746c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fixest@0.10.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-matrixextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-did", type=("build", "run"))
	depends_on("r-staggered", type=("build", "run"))
	depends_on("r-didimputation", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarked(RPackage):
	"""Mark-Recapture Analysis for Survival and Abundance Estimation

	Functions for fitting various models to capture-recapture data
    including mixed-effects Cormack-Jolly-Seber(CJS) and multistate models and
    the multi-variate state model structure for survival
    estimation and POPAN structured Jolly-Seber models for abundance estimation.
    There are also Hidden Markov model (HMM) implementations of CJS and multistate
    models with and without state uncertainty and a simulation capability for HMM
    models.
	"""
	
	cran = "marked" 

	version("1.2.8", md5="30ef969f265bafce563026fc22f37e4b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-r2admb", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-optimx@2013.8.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))

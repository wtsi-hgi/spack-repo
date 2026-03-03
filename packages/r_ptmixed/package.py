# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtmixed(RPackage):
	"""Poisson-Tweedie Generalized Linear Mixed Model

	Fits the Poisson-Tweedie generalized linear mixed model
    described in Signorelli et al. (2021, <doi:10.1177/1471082X20936017>).
    Likelihood approximation based on adaptive Gauss Hermite quadrature
    rule.
	"""
	
	homepage = "https://mirkosignorelli.github.io/r"
	cran = "ptmixed" 

	version("1.1.3", md5="7ee3b58f1a5f9115be350de1d4b15a01")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmmadaptive", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-tweedeseq", type=("build", "run"))

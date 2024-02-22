# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgcomp(RPackage):
	"""Quantile G-Computation

	G-computation for a set of time-fixed exposures with
    quantile-based basis functions, possibly under linearity and
    homogeneity assumptions. This approach estimates a regression line
    corresponding to the expected change in the outcome (on the link
    basis) given a simultaneous increase in the quantile-based category
    for all exposures. Works with continuous, binary, and right-censored
    time-to-event outcomes.  Reference: Alexander P. Keil, Jessie P.
    Buckley, Katie M. OBrien, Kelly K. Ferguson, Shanshan Zhao, and
    Alexandra J. White (2019) A quantile-based g-computation approach to
    addressing the effects of exposure mixtures; <doi:10.1289/EHP5838>.
	"""
	
	homepage = "https://github.com/alexpkeil1/qgcomp/"
	cran = "qgcomp" 

	version("2.15.2", md5="c622b0a37429564ca0988369bb8c2f43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

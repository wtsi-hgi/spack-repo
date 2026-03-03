# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAf(RPackage):
	"""Model-Based Estimation of Confounder-Adjusted Attributable
Fractions

	Estimates the attributable fraction in different sampling designs
    adjusted for measured confounders using logistic regression (cross-sectional
    and case-control designs), conditional logistic regression (matched case-control
    design), Cox proportional hazard regression (cohort design with time-to-
    event outcome), gamma-frailty model with a Weibull baseline hazard and instrumental variables analysis.
    An exploration of the AF with a genetic exposure can be found in the package 'AFheritability' Dahlqwist E et al. (2019) <doi:10.1007/s00439-019-02006-8>.
	"""
	
	cran = "AF" 

	version("0.1.5", md5="81a26d4dae290b6a04403e3ad7dcaea1")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-drgee", type=("build", "run"))
	depends_on("r-stdreg", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ivtools", type=("build", "run"))

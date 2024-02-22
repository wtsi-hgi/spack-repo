# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR0(RPackage):
	"""Estimation of R0 and Real-Time Reproduction Number from
Epidemics

	Estimation of reproduction numbers for disease outbreak, based on
    incidence data. The R0 package implements several documented methods. It is
    therefore possible to compare estimations according to the methods used.
    Depending on the methods requested by user, basic reproduction number
    (commonly denoted as R0) or real-time reproduction number (referred to as
    R(t)) is computed, along with a 95% Confidence Interval. Plotting outputs
    will give different graphs depending on the methods requested : basic
    reproductive number estimations will only show the epidemic curve
    (collected data) and an adjusted model, whereas real-time methods will also
    show the R(t) variations throughout the outbreak time period. Sensitivity
    analysis tools are also provided, and allow for investigating effects of
    varying Generation Time distribution or time window on estimates.
	"""
	
	homepage = "https://github.com/tobadia/R0"
	cran = "R0" 

	version("1.3-1", md5="ff315fff249234e05453367423098f8d", url="https://cran.r-project.org/src/contrib/R0_1.3-1.tar.gz")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

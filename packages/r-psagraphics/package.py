# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsagraphics(RPackage):
	"""Propensity Score Analysis Graphics

	A collection of functions that primarily produce graphics to
    aid in a Propensity Score Analysis (PSA).  Functions include: cat.psa
    and box.psa to test balance within strata of categorical and
    quantitative covariates, circ.psa for a representation of the
    estimated effect size by stratum, loess.psa that provides a graphic
    and loess based effect size estimate, and various balance functions
    that provide measures of the balance achieved via a PSA in a
    categorical covariate.
	"""
	
	homepage = "https://jbryer.github.io/PSAgraphics/"
	cran = "PSAgraphics" 

	version("2.1.3", md5="295545057aee42064456c3aba0776e16")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))

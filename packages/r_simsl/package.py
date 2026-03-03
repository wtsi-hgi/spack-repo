# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsl(RPackage):
	"""Single-Index Models with a Surface-Link

	An implementation of a single-index regression for optimizing individualized dose rules from an observational study. To model interaction effects between baseline covariates and a treatment variable defined on a continuum, we employ two-dimensional penalized spline regression on an index-treatment domain, where the index is defined as a linear combination of the covariates (a single-index). An unspecified main effect for the covariates is allowed, which can also be modeled through a parametric model. A unique contribution of this work is in the parsimonious single-index parametrization specifically defined for the interaction effect term. We refer to Park, Petkova, Tarpey, and Ogden (2020) <doi:10.1111/biom.13320> (for the case of a discrete treatment) and Park, Petkova, Tarpey, and Ogden (2021) "A single-index model with a surface-link for optimizing individualized dose rules" <arXiv:2006.00267v2> for detail of the method. The model can take a member of the exponential family as a response variable and can also take an ordinal categorical response. The main function of this package is simsl(). 
	"""
	
	cran = "simsl" 

	version("0.2.1", md5="1a214f4f16bec196c3b7da4bb47f4fff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))

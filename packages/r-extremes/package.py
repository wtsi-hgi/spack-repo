# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremes(RPackage):
	"""Extreme Value Analysis

	General functions for performing extreme value analysis.  In particular, allows for inclusion of covariates into the parameters of the extreme-value distributions, as well as estimation through MLE, L-moments, generalized (penalized) MLE (GMLE), as well as Bayes.  Inference methods include parametric normal approximation, profile-likelihood, Bayes, and bootstrapping.  Some bivariate functionality and dependence checking (e.g., auto-tail dependence function plot, extremal index estimation) is also included.  For a tutorial, see Gilleland and Katz (2016) <doi: 10.18637/jss.v072.i08> and for bootstrapping, please see Gilleland (2020) <doi: 10.1175/JTECH-D-20-0070.1>.
	"""
	
	homepage = "https://staff.ral.ucar.edu/ericg/extRemes/"
	cran = "extRemes" 

	version("2.1-4", md5="e6b2b6df1dc2a940db1bd5b405fd133e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lmoments", type=("build", "run"))
	depends_on("r-distillery@1.0.4:", type=("build", "run"))

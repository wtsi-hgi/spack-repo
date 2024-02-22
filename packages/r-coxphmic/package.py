# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxphmic(RPackage):
	"""Sparse Estimation of Cox Proportional Hazards Models via
Approximated Information Criterion

	Sparse estimation for Cox PH models is done via
    Minimum approximated Information Criterion (MIC) by Su, Wijayasinghe, 
    Fan, and Zhang (2016) <DOI:10.1111/biom.12484>. MIC mimics the best 
    subset selection using a penalized likelihood approach yet with no need 
    of a tuning parameter. The problem is further reformulated with a 
    re-parameterization step so that it reduces to one unconstrained non-convex
    yet smooth programming problem, which can be solved efficiently. Furthermore,
    the re-parameterization tactic yields an additional advantage in terms of
    circumventing post-selection inference.
	"""
	
	cran = "coxphMIC" 

	version("0.1.0", md5="2775e5875ba04e18fa1143c348e7fb8d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival@2.38:", type=("build", "run"))
	depends_on("r-numderiv@2014.2.1:", type=("build", "run"))

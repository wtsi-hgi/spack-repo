# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcobw(RPackage):
	"""Bandwidth Selector with Penalized Comparison to Overfitting
Criterion

	Bandwidth selector according to the Penalised Comparison to Overfitting (P.C.O.) 
             criterion as described in Varet, S., Lacour, C., Massart, P., Rivoirard, V., (2019)
             <https://hal.archives-ouvertes.fr/hal-02002275>. 
             It can be used with univariate and multivariate data. 
	"""
	
	cran = "PCObw" 

	version("0.0.1", md5="62d7ab54f39d1341f72be6fab0f75612")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

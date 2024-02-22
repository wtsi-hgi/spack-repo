# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesbp(RPackage):
	"""Bayesian Estimation using Bernstein Polynomial Fits Rate Matrix

	Smoothed lexis diagrams with Bayesian method specifically tailored to cancer 
             incidence data. Providing to calculating slope and constructing credible interval.
             LC Chien et al. (2015) <doi:10.1080/01621459.2015.1042106>. 
             LH Chien et al. (2017) <doi:10.1002/cam4.1102>.
	"""
	
	cran = "BayesBP" 

	version("1.1", md5="db61b06d952fa74059ea3340fea00f04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))

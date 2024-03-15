# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzysimres(RPackage):
	"""Simulation and Resampling Methods for Epistemic Fuzzy Data

	Random simulations of fuzzy numbers are still a challenging problem. The aim of this package is to provide the respective 
 procedures to simulate fuzzy random variables, especially in the case of the piecewise linear fuzzy numbers (PLFNs, 
 see Coroianua et al. (2013) <doi:10.1016/j.fss.2013.02.005> for the further details).
 Additionally, the special resampling algorithms known as the epistemic bootstrap are provided (see Grzegorzewski and Romaniuk
 (2022) <doi:10.34768/amcs-2022-0021>, Grzegorzewski and Romaniuk (2022) <doi:10.1007/978-3-031-08974-9_39>)
 together with the functions to apply statistical tests and estimate various characteristics based on the epistemic bootstrap.
 The package also includes a real-life data set of epistemic fuzzy triangular numbers.
 The fuzzy numbers used in this package are consistent with the 'FuzzyNumbers' package.
	"""
	
	cran = "FuzzySimRes" 

	version("0.4.0", md5="781ce0992df73b888f3467520c28da77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-palasso", type=("build", "run"))

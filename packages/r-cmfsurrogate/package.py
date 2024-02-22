# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmfsurrogate(RPackage):
	"""Calibrated Model Fusion Approach to Combine Surrogate Markers

	Uses a calibrated model fusion approach to optimally combine multiple surrogate markers. Specifically, two initial estimates of optimal composite scores of the markers are obtained; the optimal calibrated combination of the two estimated scores is then constructed which ensures both validity of the final combined score and optimality with respect to the proportion of treatment effect explained (PTE) by the final combined score. The primary function, pte.estimate.multiple(), estimates the PTE of the identified combination of multiple surrogate markers. Details are described in Wang et al (2022) <doi:10.1111/biom.13677>. 
	"""
	
	cran = "CMFsurrogate" 

	version("1.0", md5="dfa695b4676482d81129da9c6041ec71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

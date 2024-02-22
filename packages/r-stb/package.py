# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStb(RPackage):
	"""Simultaneous Tolerance Bounds

	Provides an implementation of simultaneous tolerance bounds (STB), useful for checking whether a numeric vector fits to a hypothetical null-distribution or not.
             Furthermore, there are functions for computing STB (bands, intervals) for random variates of linear mixed models fitted with package 'VCA'. All kinds of, possibly transformed 
             (studentized, standardized, Pearson-type transformed) random variates (residuals, random effects), can be assessed employing STB-methodology. 
	"""
	
	cran = "STB" 

	version("0.6.5", md5="fbb738f6dc1b6ff48c915b98cfd92294")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vca@1.3.1:", type=("build", "run"))

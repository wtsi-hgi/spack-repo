# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCronbach(RPackage):
	"""Cronbach's Alpha

	Cronbach's alpha and various formulas for confidence intervals. The relevant paper is Tsagris M., Frangos C.C. and Frangos C.C. (2013). "Confidence intervals for Cronbach's reliability coefficient". Recent Techniques in Educational Science, 14-16 May, Athens, Greece. 
	"""
	
	cran = "Cronbach" 

	version("0.1", md5="6d461802aa237ceedcf015ca82bb6f04")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))

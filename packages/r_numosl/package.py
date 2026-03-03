# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumosl(RPackage):
	"""Numeric Routines for Optically Stimulated Luminescence Dating

	Optimizing regular numeric problems in optically stimulated luminescence dating, 
        such as: equivalent dose calculation, dose rate determination, growth curve fitting, decay 
        curve decomposition, statistical age model optimization, and statistical plot visualization.
	"""
	
	homepage = "https://CRAN.R-project.org/package=numOSL"
	cran = "numOSL" 

	version("2.8", md5="a68fff5b29e4713296f6499bd9daa8cc")

	depends_on("r@2.15.3:", type=("build", "run"))

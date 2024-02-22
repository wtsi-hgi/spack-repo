# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptdesignslopeint(RPackage):
	"""Optimal Designs for Estimating the Slope Divided by the
Intercept

	Aids practitioners to optimally design experiments
    that measure the slope divided by the intercept and provides confidence intervals for the ratio.
	"""
	
	cran = "optDesignSlopeInt" 

	version("1.1.1", md5="285fb40537290044c546a4e3f0a2d5a4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbmeanfd(RPackage):
	"""Simultaneous Confidence Bands for the Mean of Functional Data

	Statistical methods for estimating and inferring the mean of functional data. The methods include simultaneous confidence bands, local polynomial fitting,  bandwidth selection by plug-in and cross-validation, goodness-of-fit tests for parametric models, equality tests for two-sample problems, and plotting functions.   
	"""
	
	homepage = "https://CRAN.R-project.org/package=SCBmeanfd"
	cran = "SCBmeanfd" 

	version("1.2.2", md5="a2944c329d95cf69218a76c3d0535543")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))

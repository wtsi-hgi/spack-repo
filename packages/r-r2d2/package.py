# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2d2(RPackage):
	"""Bivariate (Two-Dimensional) Confidence Region and Frequency
Distribution

	Generic functions to analyze the distribution of two continuous
  variables: 'conf2d' to calculate a smooth empirical confidence region, and
  'freq2d' to calculate a frequency distribution.
	"""
	
	cran = "r2d2" 

	version("1.0.1", md5="20f6a47ad3fa4d65a01d6b01de8f2865", url="https://cran.r-project.org/src/contrib/r2d2_1.0.1.tar.gz")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))

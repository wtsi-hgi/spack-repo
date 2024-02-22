# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrcregression(RPackage):
	"""Modified Poisson Regression of Grouped and Right-Censored Counts

	Implement maximum likelihood estimation for Poisson generalized
  linear models with grouped and right-censored count data. Intended to be used
  for analyzing grouped and right-censored data, which is widely applied in
  many branches of social sciences. The algorithm implemented is described
  in Fu et al., (2021) <doi:10.1111/rssa.12678>.
	"""
	
	cran = "GRCRegression" 

	version("1.0", md5="748b6ad1fc39100fa50d638048bb5cac")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))

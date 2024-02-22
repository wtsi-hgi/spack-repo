# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormallaplace(RPackage):
	"""The Normal Laplace Distribution

	Functions for the normal Laplace distribution.  Currently, it
 provides limited functionality.  Density, distribution and quantile
 functions, random number generation, and moments are provided.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "NormalLaplace" 

	version("0.3-1", md5="1ed616df2a320c7f3c5372e6e3b24e1c")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))

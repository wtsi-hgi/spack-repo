# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmer(RPackage):
	"""History Matching and Emulation Package

	A set of objects and functions for Bayes Linear emulation and history matching.
  Core functionality includes automated training of emulators to data, diagnostic functions
  to ensure suitability, and a variety of proposal methods for generating 'waves' of points.
  For details on the mathematical background, there are many papers available on the topic
  (see references attached to function help files); for details of the functions in this package,
  consult the manual or help files.
	"""
	
	homepage = "https://github.com/andy-iskauskas/hmer"
	cran = "hmer" 

	version("1.5.6", md5="ca2eccd5f1d4ec5b4ff6e4ac2a2a1fda")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))

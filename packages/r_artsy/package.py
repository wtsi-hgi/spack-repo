# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtsy(RPackage):
	"""Generative Art with 'ggplot2'

	Provides algorithms for creating artworks in the 'ggplot2' language that incorporate some form of randomness.
	"""
	
	homepage = "https://koenderks.github.io/aRtsy/"
	cran = "aRtsy" 

	version("0.2.4", md5="5b52d81a31a0f3fb850f6eeea3a6fcea")

	depends_on("r-ambient", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

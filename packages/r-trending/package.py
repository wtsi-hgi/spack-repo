# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrending(RPackage):
	"""Model Temporal Trends

	Provides a coherent interface to multiple modelling tools for
  fitting trends along with a standardised approach for generating confidence
  and prediction intervals.
	"""
	
	homepage = "https://github.com/reconverse/trending"
	cran = "trending" 

	version("0.1.0", md5="44a14e56bb58f47e86ded08537f47b79")

	depends_on("r-citools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))

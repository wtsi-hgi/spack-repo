# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedistmetrics(RPackage):
	"""Redistricting Metrics

	Reliable and flexible tools for scoring redistricting plans using 
  common measures and metrics. These functions provide key direct access to 
  tools useful for non-simulation analyses of redistricting plans, such as for 
  measuring compactness or partisan fairness. Tools are designed to work with 
  the 'redist' package seamlessly.
	"""
	
	homepage = "http://alarm-redist.org/redistmetrics/"
	cran = "redistmetrics" 

	version("1.0.7", md5="07543b0d6bbb6c6ef8d6f3ca4c5304e1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-geos", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))

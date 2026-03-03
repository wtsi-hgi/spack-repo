# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChanges(RPackage):
	"""S-Curve Fit for Changepoint Analysis

	Estimation of changepoints using an "S-curve"
   approximation. Formation of confidence intervals for changepoint
   locations and magnitudes. Both abrupt and gradual changes can be
   modeled.
	"""
	
	homepage = "https://github.com/matloff/changeS"
	cran = "changeS" 

	version("1.0.1", md5="b84e1d101678da0c0b52bf2478ddc08d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nls-multstart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

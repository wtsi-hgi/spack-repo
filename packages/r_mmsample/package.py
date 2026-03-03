# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmsample(RPackage):
	"""Multivariate Matched Sampling

	Subset a control group to match an intervention group on a set of features using multivariate matching and propensity score calipers. Based on methods in Rosenbaum and Rubin (1985).
	"""
	
	cran = "mmsample" 

	version("0.1", md5="15d802db4fd8cf966a53957ee1a96741")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsnp(RPackage):
	"""Tools for Multivariate Nonparametrics

	Tools for multivariate nonparametrics, as location tests based on marginal ranks, spatial median and spatial signs computation, Hotelling's T-test, estimates of shape are implemented.
	"""
	
	cran = "ICSNP" 

	version("1.1-2", md5="7253a768ad69baa23cdf61eac5468510")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ics", type=("build", "run"))

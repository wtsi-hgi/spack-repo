# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAds(RPackage):
	"""Spatial Point Patterns Analysis

	Perform first- and second-order multi-scale analyses derived from Ripley K-function (Ripley B. D. (1977) <doi:10.1111/j.2517-6161.1977.tb01615.x>), for univariate,
 multivariate and marked mapped data in rectangular, circular or irregular shaped sampling windows, with tests of 
 statistical significance based on Monte Carlo simulations.
	"""
	
	homepage = "https://forge.ird.fr/amap/ads"
	cran = "ads" 

	version("1.5-10", md5="23bddff5f39ec8d0b09ab047fc7066de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))

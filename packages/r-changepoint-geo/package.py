# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointGeo(RPackage):
	"""Geometrically Inspired Multivariate Changepoint Detection

	Implements the high-dimensional changepoint detection method GeomCP and the related mappings used for changepoint detection. These methods view the changepoint problem from a geometrical viewpoint and aim to extract relevant geometrical features in order to detect changepoints. The geomcp() function should be your first point of call. References: Grundy et al. (2020) <doi:10.1007/s11222-020-09940-y>. 
	"""
	
	homepage = "https://github.com/grundy95/changepoint.geo/"
	cran = "changepoint.geo" 

	version("1.0.2", md5="1e2e222cd5236ba537250f8c97ea5e3e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-changepoint-np", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))

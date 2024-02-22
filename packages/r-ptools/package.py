# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtools(RPackage):
	"""Tools for Poisson Data

	Functions used for analyzing count data, mostly crime counts. Includes checking difference in two Poisson counts (e-test), checking the fit for a Poisson distribution, small sample tests for counts in bins, Weighted Displacement Difference test (Wheeler and Ratcliffe, 2018) <doi:10.1186/s40163-018-0085-5>, to evaluate crime changes over time in treated/control areas. Additionally includes functions for aggregating spatial data and spatial feature engineering.
	"""
	
	homepage = "https://github.com/apwheele/ptools"
	cran = "ptools" 

	version("2.0.0", md5="886e97e2e85ab0b315cddcd89084fcad")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))

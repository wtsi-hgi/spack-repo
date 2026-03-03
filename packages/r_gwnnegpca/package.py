# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwnnegpca(RPackage):
	"""Geographically Weighted Non-Negative Principal Components
Analysis

	Implements a geographically weighted non-negative principal components analysis, which consists of the fusion of geographically weighted and sparse non-negative principal components analyses <doi:10.17608/k6.auckland.9850826.v1>.
	"""
	
	cran = "GWnnegPCA" 

	version("0.0.4", md5="ed6e38d7a2d52fc74b920a532a346c8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-nsprcomp", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))

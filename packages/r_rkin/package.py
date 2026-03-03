# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkin(RPackage):
	"""(Kernel) Isotope Niche Estimation

	Applies methods used to estimate animal homerange, but
    instead of geospatial coordinates, we use isotopic coordinates. The estimation
    methods include: 1) 2-dimensional bivariate normal kernel utilization density
    estimator, 2) bivariate normal ellipse estimator, and 3) minimum convex polygon
    estimator, all applied to stable isotope data. Additionally, functions to
    determine niche area, polygon overlap between groups and levels (confidence
    contours) and plotting capabilities.
	"""
	
	homepage = "https://github.com/salbeke/rKIN"
	cran = "rKIN" 

	version("1.0.2", md5="dd6f4b11d870c92857e42e72c1aace32")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-shades", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

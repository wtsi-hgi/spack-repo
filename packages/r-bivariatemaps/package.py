# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivariatemaps(RPackage):
	"""Creates Bivariate Maps

	Contains functions to plot bivariate maps and to generate grids from shapefiles based on area coverage. For more info, see: Hidasi-Neto, J (2015) <https://rfunctions.blogspot.com/2015/03/bivariate-maps-bivariatemap-function.html>, Hidasi-Neto, J (2014) <https://rfunctions.blogspot.com/2014/12/gridfilter-intersect-grid-with-shape.html>.
	"""
	
	cran = "bivariatemaps" 

	version("1.2", md5="bc933b211dc341146ebf74a30dbe6928")

	depends_on("r-classint", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))

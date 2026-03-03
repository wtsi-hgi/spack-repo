# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwpcor(RPackage):
	"""Geographically Weighted Partial Correlation Coefficient

	Implements a geographically weighted partial correlation which is an extension from gwss() function in the 'GWmodel' package (Percival and Tsutsumida (2017) <doi:10.1553/giscience2017_01_s36>).
	"""
	
	cran = "GWpcor" 

	version("0.1.7", md5="bdf264a7b6c877c392dbe5a21dc54adf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGecko(RPackage):
	"""Geographical Ecology and Conservation Knowledge Online

	Includes a collection of geographical analysis functions aimed primarily at ecology and conservation science studies, allowing processing of both point and raster data. Future versions will integrate species threat datasets developed by the authors.
	"""
	
	cran = "gecko" 

	version("1.0.0", md5="b87af16cef4d69b5027e9c5d6b8603d8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-red", type=("build", "run"))
	depends_on("r-biomod2", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))

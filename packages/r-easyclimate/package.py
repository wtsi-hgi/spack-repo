# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyclimate(RPackage):
	"""Easy Access to High-Resolution Daily Climate Data for Europe

	Get high-resolution (1 km) daily climate data (precipitation,
    minimum and maximum temperatures) for points and polygons within
    Europe.
	"""
	
	homepage = "https://github.com/VeruGHub/easyclimate"
	cran = "easyclimate" 

	version("0.2.1", md5="7ead1e4ece8ba32af3f68bcf89a45183")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-terra@1.2.13:", type=("build", "run"))

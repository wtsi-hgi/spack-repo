# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsom(RPackage):
	"""New Data Visualisations for SOMs Networks

	The aim of this package is to offer more variability of graphics based on the self-organizing maps.
	"""
	
	homepage = "https://github.com/oldlipe/ggsom"
	cran = "ggsom" 

	version("0.4.0", md5="62a12226d34ea94f2dc02d04acab5de8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

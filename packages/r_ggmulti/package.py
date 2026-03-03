# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmulti(RPackage):
	"""High Dimensional Data Visualization

	It provides materials (i.e. 'serial axes' objects, Andrew's plot, various glyphs for scatter plot) to visualize high dimensional data. 
	"""
	
	cran = "ggmulti" 

	version("1.0.6", md5="605081b459df3a04e002707cd4a042b6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))

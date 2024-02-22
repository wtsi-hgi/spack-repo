# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindviews(RPackage):
	"""A View Generator for Multidimensional Data

	A tool to explore wide data sets, by detecting, ranking
    and plotting groups of statistically dependent columns.
	"""
	
	homepage = "https://github.com/tsellam/findviews"
	cran = "findviews" 

	version("0.1.3", md5="ea74db5ef9954a50231bb7d0e8d424fa")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

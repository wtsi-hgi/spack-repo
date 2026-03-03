# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgcviz(RPackage):
	"""Visualisations for Generalized Additive Models

	Extension of the 'mgcv' package, providing visual tools for Generalized Additive Models that exploit the additive structure of such models, scale to large data sets and can be used in conjunction with a wide range of response distributions. The focus is providing visual methods for better understanding the model output and for aiding model checking and development beyond simple exponential family regression. The graphical framework is based on the layering system provided by 'ggplot2'.
	"""
	
	homepage = "https://github.com/mfasiolo/mgcViz"
	cran = "mgcViz" 

	version("0.1.11", md5="8b1f6454bc0d2d2a91f638ed6a25cfa6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv@1.8.28:", type=("build", "run"))
	depends_on("r-qgam@1.2.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))

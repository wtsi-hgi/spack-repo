# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDad(RPackage):
	"""Three-Way / Multigroup Data Analysis Through Densities

	The data consist of a set of variables measured on several groups of individuals. To each group is associated an estimated probability density function. The package provides tools to create or manage such data and functional methods (principal component analysis, multidimensional scaling, cluster analysis, discriminant analysis...) for such probability densities.
	"""
	
	homepage = "https://forgemia.inra.fr/dad/dad"
	cran = "dad" 

	version("4.1.2", md5="61eecbcced4534bfbd6a58bdc6f47d06")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))

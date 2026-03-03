# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrelplot(RPackage):
	"""A Collection of Functions for Graphing Correlation Matrices

	Routines for the graphical representation of correlation matrices by means of correlograms, MDS maps and biplots obtained by PCA, PFA or WALS (weighted alternating least squares); See Graffelman & De Leeuw (2023) <doi: 10.1080/00031305.2023.2186952>. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "Correlplot" 

	version("1.1.0", md5="fdba1529f4130cb4bb1a8ac8dfed7baa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lsei", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

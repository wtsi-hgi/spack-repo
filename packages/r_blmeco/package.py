# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlmeco(RPackage):
	"""Data Files and Functions Accompanying the Book "Bayesian Data
Analysis in Ecology using R, BUGS and Stan"

	Data files and functions accompanying the book Korner-Nievergelt, Roth, von Felten, Guelat, Almasi, Korner-Nievergelt (2015) "Bayesian Data Analysis in Ecology using R, BUGS and Stan", Elsevier, New York.
	"""
	
	cran = "blmeco" 

	version("1.4", md5="a263b85a3ea6c1fa1405316f896999dd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))

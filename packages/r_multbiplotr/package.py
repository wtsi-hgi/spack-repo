# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultbiplotr(RPackage):
	"""Multivariate Analysis Using Biplots in R

	Several multivariate techniques from a biplot perspective. It is the translation (with many improvements) into R of the previous package developed in 'Matlab'. The package contains some of the main developments of my team during the last 30 years together with some more standard techniques. Package includes: Classical Biplots, HJ-Biplot, Canonical Biplots, MANOVA Biplots, Correspondence Analysis, Canonical Correspondence Analysis, Canonical STATIS-ACT, Logistic Biplots for binary and ordinal data, Multidimensional Unfolding, External Biplots for Principal Coordinates Analysis or Multidimensional Scaling, among many others. References can be found in the help of each procedure.
	"""
	
	cran = "MultBiplotR" 

	version("23.11.0", md5="e865efd25b971d5bc8458f9941b40f4b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-threeway", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))

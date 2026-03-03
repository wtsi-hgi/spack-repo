# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJewel(RPackage):
	"""Graphical Models Estimation from Multiple Sources

	Estimates networks of conditional dependencies (Gaussian graphical models) from multiple classes of data (similar but not exactly, i.e. measurements on different equipment, in different locations or for various sub-types). Package also allows to generate simulation data and evaluate the performance. Implementation of the method described in Angelini, De Canditiis and Plaksienko (2022) <doi:10.3390/math10213983>.
	"""
	
	homepage = "https://github.com/annaplaksienko/jewel"
	cran = "jewel" 

	version("2.0.1", md5="6e34eb04ec11af397f664642f0ed3e4c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-smut", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraminerextras(RPackage):
	"""TraMineR Extension

	Collection of ancillary functions and utilities to be used in conjunction with the 'TraMineR' package for sequence data exploration. Includes, among others, specific functions such as state survival plots, position-wise group-typical states, dynamic sequence indicators, and dissimilarities between event sequences. Also includes contributions by non-members of the TraMineR team such as the relative frequency plot and methods for polyadic data.
	"""
	
	homepage = "http://traminer.unige.ch/"
	cran = "TraMineRextras" 

	version("0.6.7", md5="c4cfc05d63b66ab7e56b2503e7f2ea23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-traminer@2.2.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))

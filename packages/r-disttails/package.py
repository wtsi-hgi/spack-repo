# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisttails(RPackage):
	"""A Collection of Full Defined Distribution Tails

	A full definition for Weibull tails and Full-Tails Gamma and tools for fitting these distributions to empirical tails. This package build upon the paper by del Castillo, Joan & Daoudi, Jalila & Serra, Isabel. (2012) <doi:10.1017/asb.2017.9>.
	"""
	
	homepage = "https://github.com/SergiVilardell/distTails"
	cran = "distTails" 

	version("0.1.2", md5="6718762a4b9faaad3874f805307472d2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ercv", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

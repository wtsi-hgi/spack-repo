# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffluenceindex(RPackage):
	"""Affluence (Richness) Indices

	Enables to compute the statistical indices of affluence (richness) with bootstrap errors, and inequality and polarization indices. Moreover, gives the possibility of calculation of Medeiros affluence line. In 2.1 version some simple errors are fixed.
	"""
	
	cran = "affluenceIndex" 

	version("2.1", md5="49322e454db0516342eb28c189c2e8f2")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))

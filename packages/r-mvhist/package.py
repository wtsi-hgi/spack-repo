# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvhist(RPackage):
	"""Multivariate Histograms

	Tabulate and plot directional and other multivariate histograms.
	"""
	
	cran = "mvhist" 

	version("1.1", md5="d57e120425470e8fd90a3fb5df17aa73")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mvmesh", type=("build", "run"))
	depends_on("r-simplicialcubature", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))

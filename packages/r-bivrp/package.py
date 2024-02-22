# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivrp(RPackage):
	"""Bivariate Residual Plots with Simulation Polygons

	Generates bivariate residual plots with simulation polygons for any diagnostics and bivariate model from which functions to extract the desired diagnostics, simulate new data and refit the models are available.
	"""
	
	cran = "bivrp" 

	version("1.2-2", md5="f21693f71f6125b6db037a68e28cf903")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass@7.3.35:", type=("build", "run"))

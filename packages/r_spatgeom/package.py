# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatgeom(RPackage):
	"""Geometric Spatial Point Analysis

	The implementation to perform the geometric spatial point analysis developed in Hernández & Solís (2022) <doi:10.1007/s00180-022-01244-1>. It estimates the geometric goodness-of-fit index for a set of variables against a response one based on the 'sf' package. The package has methods to print and plot the results.
	"""
	
	homepage = "https://github.com/maikol-solis/spatgeom"
	cran = "spatgeom" 

	version("0.3.0", md5="5fa840afdfcddcde417c18f1fd0b4cfa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))

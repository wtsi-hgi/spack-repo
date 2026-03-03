# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmapfit(RPackage):
	"""Fit Statistic for Binary Dependent Variable Models

	Generates a fit plot for diagnosing misspecification in models of
    binary dependent variables, and calculates the related heatmap fit
    statistic described in Esarey and Pierce (2012) <DOI:10.1093/pan/mps026>.
	"""
	
	cran = "heatmapFit" 

	version("2.0.4", md5="fabd082c5fb6f649b6e4952e277d4dc7")

	depends_on("r@3.1.1:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnidom(RPackage):
	"""Inferring Dominance Hierarchies and Estimating Uncertainty

	Provides: (1) Tools to infer dominance hierarchies based on calculating Elo scores, but with custom functions to improve estimates in animals with relatively stable dominance ranks. (2) Tools to plot the shape of the dominance hierarchy and estimate the uncertainty of a given data set.
	"""
	
	cran = "aniDom" 

	version("0.1.5", md5="55143da20b17f4987ad24c613c7d4a4f")

	depends_on("r-rptr", type=("build", "run"))

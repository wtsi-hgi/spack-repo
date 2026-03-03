# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViolinplotter(RPackage):
	"""Plotting and Comparing Means with Violin Plots

	Produces violin plots with optional nonparametric (Mann-Whitney test) and parametric (Tukey's honest significant difference) mean comparison and linear regression. This package aims to be a simple and quick visualization tool for comparing means and assessing trends of categorical factors.
	"""
	
	cran = "violinplotter" 

	version("3.0.1", md5="2598880406b00e187088d3123954b79d")

	depends_on("r@3.5:", type=("build", "run"))

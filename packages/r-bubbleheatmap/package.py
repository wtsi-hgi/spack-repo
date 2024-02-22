# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBubbleheatmap(RPackage):
	"""Produces 'bubbleHeatmap' Plots for Visualising Metabolomics Data

	Plotting package based on the grid system, combining elements of 
    a bubble plot and heatmap to conveniently display two numerical variables, 
    (represented by color and size) grouped by categorical variables on the x 
    and y axes. This is a useful alternative to a forest plot when the data can 
    be grouped in two dimensions, such as predictors x outcomes. It has 
    particular advantages for visualising the metabolic measures produced by 
    the 'Nightingale Health' metabolomics platform, and templates are included 
    for automatically generating figures from these datasets.
	"""
	
	cran = "bubbleHeatmap" 

	version("0.1.1", md5="d37d88153b43296a6c638da53e540646")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))

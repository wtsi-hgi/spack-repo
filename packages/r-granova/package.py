# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGranova(RPackage):
	"""Graphical Analysis of Variance

	This small collection of functions provides what we call elemental graphics for display of analysis of variance
    results, David C. Hoaglin, Frederick Mosteller and John W. Tukey (1991, ISBN:978-0-471-52735-0), Paul R. Rosenbaum (1989) 
    <doi:10.2307/2684513>, Robert M. Pruzek and James E. Helmreich <https://jse.amstat.org/v17n1/helmreich.html>. 
    The term elemental derives from the fact that each function is aimed at construction of
    graphical displays that afford direct visualizations of data with respect to the fundamental 
    questions that drive the particular analysis of variance methods. These functions can be 
    particularly helpful for students and non-statistician analysts. But these methods should be
    quite generally helpful for work-a-day applications of all kinds, as they can help to identify
    outliers, clusters or patterns, as well as highlight the role of non-linear transformations of data.
	"""
	
	cran = "granova" 

	version("2.2", md5="712a8d3afbc2b3262772c714ebe9e764")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-car@2.0.21:", type=("build", "run"))

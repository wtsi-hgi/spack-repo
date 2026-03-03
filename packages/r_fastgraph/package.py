# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastgraph(RPackage):
	"""Fast Drawing and Shading of Graphs of Statistical Distributions

	Provides functionality to produce graphs of probability density functions and cumulative distribution functions with few keystrokes, allows shading under the curve of the probability density function to illustrate concepts such as p-values and critical values, and fits a simple linear regression line on a scatter plot with the equation as the main title.
	"""
	
	cran = "fastGraph" 

	version("2.1", md5="c9f083f2f177b8b430f6e76ab3e7d102")

	depends_on("r@2:", type=("build", "run"))

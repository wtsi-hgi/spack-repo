# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcorrplot(RPackage):
	"""Visualization of a Correlation Matrix using 'ggplot2'

	The 'ggcorrplot' package can be used to visualize easily a
    correlation matrix using 'ggplot2'. It provides a solution for
    reordering the correlation matrix and displays the significance level
    on the plot. It also includes a function for computing a matrix of
    correlation p-values.
	"""
	
	homepage = "http://www.sthda.com/english/wiki/ggcorrplot-visualization-of-a-correlation-matrix-using-ggplot2"
	cran = "ggcorrplot" 

	version("0.1.4.1", md5="62fab7931481cecd3eee71db7dda9cd8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

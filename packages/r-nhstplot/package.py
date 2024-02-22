# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhstplot(RPackage):
	"""Plot Null Hypothesis Significance Tests

	Illustrate graphically the most common Null Hypothesis Significance Testing procedures. More specifically, this package provides functions to plot Chi-Squared, F, t (one- and two-tailed) and z (one- and two-tailed) tests, by plotting the probability density under the null hypothesis as a function of the different test statistic values. Although highly flexible (color theme, fonts, etc.), only the minimal number of arguments (observed test statistic, degrees of freedom) are necessary for a clear and useful graph to be plotted, with the observed test statistic and the p value, as well as their corresponding value labels. The axes are automatically scaled to present the relevant part and the overall shape of the probability density function. This package is especially intended for education purposes, as it provides a helpful support to help explain the Null Hypothesis Significance Testing process, its use and/or shortcomings.
	"""
	
	cran = "nhstplot" 

	version("1.2.0", md5="22dc433485451943f4ad947539df4024")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))

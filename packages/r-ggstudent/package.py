# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstudent(RPackage):
	"""Continuous Confidence Interval Plots using t-Distribution

	Provides an extension to 'ggplot2' (Wickham, 2016, <doi:10.1007/978-3-319-24277-4>) for creating two 
    types of continuous confidence interval plots (Violin CI and Gradient CI plots), typically for the sample mean.
    These plots contain multiple user-defined confidence areas with varying colours, 
    defined by the underlying t-distribution used to compute standard confidence intervals for 
    the mean of the normal distribution when the variance is unknown.
    Two types of plots are available, a gradient plot with rectangular areas, and a violin plot where the 
    shape (horizontal width) is defined by the probability density function of the t-distribution.
	"""
	
	cran = "ggstudent" 

	version("0.1.1-1", md5="17f4a639c6d71df3d179d3c872b69a81")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

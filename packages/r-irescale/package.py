# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrescale(RPackage):
	"""Calculate and Rectify Moran's I

	Provides a scaling method to obtain a standardized Moran's I measure. Moran's I is a measure for the spatial autocorrelation of a data set, it gives a measure of similarity between data and its surrounding. The range of this value must be [-1,1], but this does not happen in practice. This package scale the Moran's I value and map it into the theoretical range of [-1,1]. Once the Moran's I value is rescaled, it facilitates the comparison between projects, for instance, a researcher can calculate Moran's I in a city in China, with a sample size of n1 and area of interest a1. Another researcher runs a similar experiment in a city in Mexico with different sample size, n2, and an area of interest a2. Due to the differences between the conditions, it is not possible to compare Moran's I in a straightforward way. In this version of the package, the spatial autocorrelation Moran's I is calculated as proposed in Chen(2013) <arXiv:1606.03658>.
	"""
	
	homepage = "https://github.tamu.edu/jivfur/rectifiedI"
	cran = "Irescale" 

	version("2.3.0", md5="fc1b4460996b1d58aa6b08726b89af4a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

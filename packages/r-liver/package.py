# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiver(RPackage):
	""""Eating the Liver of Data Science"

	Offers a suite of helper functions to simplify various data science techniques for non-experts. This package aims to enable individuals with only a minimal level of coding knowledge to become acquainted with these techniques in an accessible manner. Inspired by an ancient Persian idiom, we liken this process to "eating the liver of data science," suggesting a deep and intimate engagement with the field of data science. This package includes functions for tasks such as data partitioning for out-of-sample testing, calculating Mean Squared Error (MSE) to assess prediction accuracy, and data transformations (z-score and min-max). In addition to these helper functions, the 'liver' package also features several intriguing datasets valuable for multivariate analysis.
	"""
	
	homepage = "https://www.uva.nl/profile/a.mohammadi"
	cran = "liver" 

	version("1.15", md5="8134a1b707fb34291aadb548873ae4a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

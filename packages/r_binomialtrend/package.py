# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinomialtrend(RPackage):
	"""Calculates the Statistical Significance of a Trend in a Set of
Measurements

	Detection of a statistically significant trend in the data provided by the user.
    This is based on the a signed test based on the binomial distribution.
    The package returns a trend test value, T, and also a p-value. A T value 
    close to 1 indicates a rising trend, whereas a T value close to -1 indicates a decreasing
    trend. A T value close to 0 indicates no trend. There is also a command to visualize
    the trend. A test data set called gtsa_data is also available, which has global mean 
    temperatures for January, April, July, and October for the years 1851 to 2022.
    Reference: Walpole, Myers, Myers, Ye. (2007, ISBN: 0-13-187711-9).
	"""
	
	cran = "binomialtrend" 

	version("0.0.0.3", md5="6c9190643d70552231a42c3d9fb479b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))

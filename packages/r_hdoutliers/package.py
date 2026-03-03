# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdoutliers(RPackage):
	"""Leland Wilkinson's Algorithm for Detecting Multidimensional
Outliers

	An implementation of an algorithm for outlier detection that can handle a) data with a mixed categorical and continuous variables, b) many columns of data, c) many rows of data, d) outliers that mask other outliers, and e) both unidimensional and multidimensional datasets. Unlike ad hoc methods found in many machine learning papers, HDoutliers is based on a distributional model that uses probabilities to determine outliers.
	"""
	
	cran = "HDoutliers" 

	version("1.0.4", md5="518fab9a700144a7d1c7a3e3e031eb21")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))

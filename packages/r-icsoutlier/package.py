# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsoutlier(RPackage):
	"""Outlier Detection Using Invariant Coordinate Selection

	Multivariate outlier detection is performed using invariant coordinates where the package offers different methods to choose the appropriate components. ICS is a general multivariate technique with many applications in multivariate analysis. ICSOutlier offers a selection of functions for automated detection of outliers in the data based on a fitted ICS object or by specifying the dataset and the scatters of interest. The current implementation targets data sets with only a small percentage of outliers. 
	"""
	
	cran = "ICSOutlier" 

	version("0.4-0", md5="5f3a2b02876603f8cd642c593295a7bf")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ics@1.4.0:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

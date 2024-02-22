# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiskew(RPackage):
	"""Measures, Tests and Removes Multivariate Skewness

	Computes the third multivariate cumulant of either the raw, centered or standardized data. Computes the main measures of multivariate skewness, together with their bootstrap distributions. Finally, computes the least skewed linear projections of the data.
	"""
	
	cran = "MultiSkew" 

	version("1.1.1", md5="552b4efdc0cd4ea35b8f474c974c03ec")

	depends_on("r-maxskew", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpandist(RPackage):
	"""Statistical Functions for the Censored and Uncensored
Epanechnikov Distribution

	Analyzing censored variables usually requires the use of optimization algorithms. This package provides an alternative algebraic approach to the task of determining the expected value of a random censored variable with a known censoring point. Likewise this approach allows for the determination of the censoring point if the expected value is known. These results are derived under the assumption that the variable follows an Epanechnikov kernel distribution with known mean and range prior to censoring. Statistical functions related to the uncensored Epanechnikov distribution are also provided by this package.
	"""
	
	cran = "epandist" 

	version("1.1.1", md5="37d9f9e1ecde3ae99f4117777a05d583")

	depends_on("r@3:", type=("build", "run"))

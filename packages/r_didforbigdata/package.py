# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDidforbigdata(RPackage):
	"""A Big Data Implementation of Difference-in-Differences
Estimation with Staggered Treatment

	Provides a big-data-friendly and memory-efficient difference-in-differences estimator for staggered (and non-staggered) treatment contexts. 
	"""
	
	homepage = "https://setzler.github.io/DiDforBigData/"
	cran = "DiDforBigData" 

	version("1.0", md5="048f050612ec6983803f23b13b3cecec")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))

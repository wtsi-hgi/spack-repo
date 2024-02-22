# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensus2016(RPackage):
	"""Data from the Australian Census 2016

	Contains selected variables from the time series profiles for statistical areas level 2 from the 2006, 2011, and 2016 censuses of population and housing, Australia. Also provides methods for viewing the questions asked for convenience during analysis.
	"""
	
	cran = "Census2016" 

	version("0.2.0", md5="1a12a18eefa46e5e2ebd5de4bee5f134", url="https://cran.r-project.org/src/contrib/Census2016_0.2.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

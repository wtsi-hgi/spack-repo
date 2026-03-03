# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissdeaths(RPackage):
	"""Simulating and Analyzing Time to Event Data in the Presence of
Population Mortality

	Implements two methods: a nonparametric risk adjustment and a
    data imputation method that use general population mortality tables to allow a
    correct analysis of time to disease recurrence. Also includes a powerful set of
    object oriented survival data simulation functions.
	"""
	
	cran = "missDeaths" 

	version("2.7", md5="a1e76479a79731c756bbb672c7d0518f")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-relsurv", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mitools", type=("build", "run"))

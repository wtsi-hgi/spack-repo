# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpstring(RPackage):
	"""Patterns and Statistical Differences Between Two Groups of
Strings

	Methods include converting series of event names to strings, finding common patterns
    in a group of strings, discovering featured patterns when comparing two groups of strings as well
    as the number and starting position of each pattern in each string, obtaining transition matrix, 
    computing transition entropy, statistically comparing the difference between two groups of strings,
    and clustering string groups. Event names can be any action names or labels such as events in log
    files or areas of interest (AOIs) in eye tracking research.
	"""
	
	cran = "GrpString" 

	version("0.3.2", md5="00f432c16dc3100e488f77c03572dc71")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerccalc(RPackage):
	"""Estimate Percentiles from an Ordered Categorical Variable

	An implementation of two functions that estimate values for percentiles from an ordered categorical variable as described by Reardon (2011, isbn:978-0-87154-372-1). One function estimates percentile differences from two percentiles while the other returns the values for every percentile from 1 to 100.
	"""
	
	homepage = "https://cimentadaj.github.io/perccalc/"
	cran = "perccalc" 

	version("1.0.5", md5="01816c30fd5005a1a935a921763e02c9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))

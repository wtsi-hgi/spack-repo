# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncidental(RPackage):
	"""Implements Empirical Bayes Incidence Curves

	Make empirical Bayes incidence curves from reported case data using a specified delay distribution.
	"""
	
	cran = "incidental" 

	version("0.1", md5="27e941303a00f0961f6708315ce7c807")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-dlnm", type=("build", "run"))

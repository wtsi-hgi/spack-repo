# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmetalog(RPackage):
	"""The Metalog Distribution

	Implementation of the metalog distribution in R.
    The metalog distribution is a modern, highly flexible, data-driven distribution. 
    Metalogs are developed by Keelin (2016) <doi:10.1287/deca.2016.0338>.
    This package provides functions to build these distributions from raw data. 
    Resulting metalog objects are then useful for exploratory and probabilistic analysis.
	"""
	
	cran = "rmetalog" 

	version("1.0.3", md5="4a860e8a75c4733bb19343f0783888c9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

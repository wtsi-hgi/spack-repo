# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtainterfacetrendanalysis(RPackage):
	"""Temporal Trend Analysis Graphical Interface

	This interface was created to develop a standard procedure 
 to analyse temporal trend in the framework of the OSPAR convention.
 The analysis process run through 4 successive steps : 1) manipulate your data, 2)
 select the parameters you want to analyse, 3) build your regulated 
 time series, 4) perform diagnosis and analysis and 5) read the results. 
 Statistical analysis call other package function such as Kendall tests
 or cusum() function.
	"""
	
	homepage = "https://CRAN.R-project.org/package=TTAinterfaceTrendAnalysis"
	cran = "TTAinterfaceTrendAnalysis" 

	version("1.5.10", md5="68fba15d5bbac55d0236d1ac9f2e53bd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-relimp", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-rkt", type=("build", "run"))
	depends_on("r-stlplus", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-wql", type=("build", "run"))

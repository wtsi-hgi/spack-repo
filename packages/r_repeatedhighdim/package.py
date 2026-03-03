# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepeatedhighdim(RPackage):
	"""Methods for High-Dimensional Repeated Measures Data

	A toolkit for the analysis of high-dimensional repeated measurements, providing functions 
    for outlier detection, differential expression analysis, gene-set tests, and binary random data generation.
	"""
	
	cran = "RepeatedHighDim" 

	version("2.2.0", md5="a06edbf7bd1d536eb9850f3dcd458c42")

	depends_on("r-ddalpha", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))

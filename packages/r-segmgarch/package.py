# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmgarch(RPackage):
	"""Multiple Change-Point Detection for High-Dimensional GARCH
Processes

	Implements a segmentation algorithm for multiple change-point detection in high-dimensional GARCH processes. It simultaneously segments GARCH processes by identifying 'common' change-points, each of which can be shared by a subset or all of the component time series as a change-point in their within-series and/or cross-sectional correlation structure. 
	"""
	
	cran = "segMGarch" 

	version("1.2", md5="7ca64fcfc2dbd1023098c00419f227ee")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

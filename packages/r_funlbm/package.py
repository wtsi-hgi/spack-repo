# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunlbm(RPackage):
	"""Model-Based Co-Clustering of Functional Data

	The funLBM algorithm allows to simultaneously cluster the rows and the columns of a data matrix where each entry of the matrix is a function or a time series.
	"""
	
	cran = "funLBM" 

	version("2.3", md5="1c30677e8817d64a50bbc49174c3d770")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-funfem", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))

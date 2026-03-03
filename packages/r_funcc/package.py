# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuncc(RPackage):
	"""Functional Cheng and Church Bi-Clustering

	The FunCC algorithm allows to apply the FunCC algorithm to simultaneously cluster the rows and the columns of a data matrix whose inputs are functions. 
	"""
	
	cran = "FunCC" 

	version("1.0", md5="5d0d3b4efc4e4e0840b1469ca17f2a4a")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-narray", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

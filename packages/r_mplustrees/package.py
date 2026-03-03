# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMplustrees(RPackage):
	"""Decision Trees with Structural Equation Models Fit in 'Mplus'

	Uses recursive partitioning to create homogeneous subgroups based on structural equation models 
             fit in 'Mplus', a stand-alone program developed by Muthen and Muthen.
	"""
	
	cran = "MplusTrees" 

	version("0.2.2", md5="d9769f9565386d725bc2efeff3a0116c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))

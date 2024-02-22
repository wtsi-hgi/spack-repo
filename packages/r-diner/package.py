# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiner(RPackage):
	"""Differential Network Estimation in R

	An efficient and convenient set of functions to perform differential network estimation through the use of alternating direction method of multipliers optimization with a variety of loss functions. 
	"""
	
	homepage = "https://github.com/RicSalgado/dineR"
	cran = "dineR" 

	version("1.0.1", md5="7b7e4ec6a25679af358d2a03f561109d")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

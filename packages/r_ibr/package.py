# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbr(RPackage):
	"""Iterative Bias Reduction

	Multivariate smoothing using iterative bias reduction with kernel, thin plate splines, Duchon splines or low rank splines. 
	"""
	
	cran = "ibr" 

	version("2.0-4", md5="43eaf7e684214642c708c469f5ba922f")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))

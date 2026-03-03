# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhd(RPackage):
	"""Metric Halfspace Depth

	Metric halfspace depth for object data, generalizing Tukey's depth for Euclidean data. Implementing the method described in Dai and Lopez-Pintado (2022) <doi:10.1080/01621459.2021.2011298>.
	"""
	
	cran = "MHD" 

	version("0.1.2", md5="01740778c9a3a43e9ce48f9493758af6")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-manifold", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-distory", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

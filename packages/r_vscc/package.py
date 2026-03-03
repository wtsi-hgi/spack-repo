# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVscc(RPackage):
	"""Variable Selection for Clustering and Classification

	Performs variable selection/feature reduction under a clustering or 
  classification framework. In particular, it can be used in an automated fashion 
  using mixture model-based methods ('teigen' and 'mclust' are currently supported).
  Can account for mixtures of non-Gaussian distributions via Manly transform (via 'ManlyMix').
  See Andrews and McNicholas (2014) <doi:10.1007/s00357-013-9139-2> and Neal and McNicholas (2023)
  <doi:10.48550/arXiv.2305.16464>. 
	"""
	
	cran = "vscc" 

	version("0.7", md5="02fa6836f4f9cf96483cc5d3f9d158cf")

	depends_on("r-manlymix", type=("build", "run"))
	depends_on("r-teigen", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mixghd", type=("build", "run"))

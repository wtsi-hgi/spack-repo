# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowboot(RPackage):
	"""Bootstrap Methods for Network Inference

	Functions for analysis of network objects, which are imported or simulated by the package. The non-parametric methods of analysis center on snowball and bootstrap sampling for estimating functions of network degree distribution. For other parameters of interest, see, e.g., 'bootnet' package.
	"""
	
	cran = "snowboot" 

	version("1.0.2", md5="68e614977a47a9f6d737528e0ad00cfa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))

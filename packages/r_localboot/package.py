# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalboot(RPackage):
	"""Local Bootstrap Methods for Various Networks

	Network analysis usually requires estimating the uncertainty of
    graph statistics. Through this package, we provide tools to bootstrap 
    various networks via local bootstrap procedure. Additionally, it includes 
    functions for generating probability matrices, creating network adjacency 
    matrices from probability matrices, and plotting network structures. 
    The reference will be updated soon.
	"""
	
	cran = "localboot" 

	version("0.9.2", md5="425b7035ac4f1ff2f3dea027da5a87de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcpp@1.0.11:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

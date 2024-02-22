# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphkernels(RPackage):
	"""Graph Kernels

	A fast C++ implementation for computing various graph kernels including (1) simple kernels between vertex and/or edge label histograms, (2) graphlet kernels, (3) random walk kernels (popular baselines), and (4) the Weisfeiler-Lehman graph kernel (state-of-the-art).
	"""
	
	cran = "graphkernels" 

	version("1.6.1", md5="3bfe902dc0913e9d6100776258e77fc9")

	depends_on("r-igraph@1.1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

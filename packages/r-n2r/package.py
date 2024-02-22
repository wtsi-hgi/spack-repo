# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RN2r(RPackage):
	"""Fast and Scalable Approximate k-Nearest Neighbor Search Methods
using 'N2' Library

	Implements methods to perform fast approximate K-nearest neighbor search on input matrix. Algorithm based on the 'N2' implementation of an approximate nearest neighbor search using hierarchical  Navigable Small World (NSW) graphs. The original algorithm is described in "Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs", Y. Malkov and D. Yashunin, <doi:10.1109/TPAMI.2018.2889473>, <arXiv:1603.09320>.
	"""
	
	homepage = "https://github.com/kharchenkolab/N2R"
	cran = "N2R" 

	version("1.0.1", md5="931b8afd448f79b6f5379adbab62905e")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppspdlog", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

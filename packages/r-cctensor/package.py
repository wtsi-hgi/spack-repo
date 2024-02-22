# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCctensor(RPackage):
	"""CUR/CX Tensor Decomposition

	CUR/CX decomposition factorizes a matrix into two factor matrices and Multidimensional CX Decomposition factorizes a tensor into a core tensor and some factor matrices. See the reference section of GitHub README.md <https://github.com/rikenbit/ccTensor>, for details of the methods.
	"""
	
	homepage = "https://github.com/rikenbit/ccTensor"
	cran = "ccTensor" 

	version("1.0.2", md5="d9eac287068c7f5517ed4a9cc6776bde")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))

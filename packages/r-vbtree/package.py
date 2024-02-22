# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbtree(RPackage):
	"""Vector Binary Tree to Make Your Data Management More Efficient

	Vector binary tree provides a new data structure, to
 make your data visiting and management more efficient. If the
 data has structured column names, it can read these names and
 factorize them through specific split pattern, then build the mappings
 within double list, vector binary tree, array and tensor mutually, through
 which the batched data processing is achievable easily. The methods of
 array and tensor are also applicable. Detailed methods are described in
 Chen Zhang et al. (2020) <doi:10.35566/isdsa2019c8>.
	"""
	
	homepage = "https://github.com/CubicZebra/VBTree"
	cran = "VBTree" 

	version("0.1.1", md5="35c3f2de3fde1ac67a83530898310fd0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))

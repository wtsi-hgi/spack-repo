# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdsvd(RPackage):
	"""Block Structure Detection Using Singular Vectors

	Performs block diagonal covariance matrix detection using singular vectors (BD-SVD), which can be extended to hierarchical variable clustering (HC-SVD). The methods are described in Bauer (202Xa) <arXiv:2211.16155> and Bauer (202Xb) <arXiv:2308.06820>.
	"""
	
	cran = "bdsvd" 

	version("0.1-0", md5="d4719cd1f89e80a0bc9c47af3a92d014")

	depends_on("r-irlba", type=("build", "run"))

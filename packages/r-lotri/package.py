# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLotri(RPackage):
	"""A Simple Way to Specify Symmetric, Block Diagonal Matrices

	Provides a simple mechanism to specify a symmetric block
    diagonal matrices (often used for covariance matrices).  This is based
    on the domain specific language implemented in 'nlmixr2' but expanded
    to create matrices in R generally instead of specifying parts of
    matrices to estimate.
	"""
	
	homepage = "https://github.com/nlmixr2/lotri"
	cran = "lotri" 

	version("0.4.3", md5="f38b66bd9eb9a28d39d2dc7c33958a53")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))

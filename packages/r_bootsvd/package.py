# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootsvd(RPackage):
	"""Fast, Exact Bootstrap Principal Component Analysis for High
Dimensional Data

	Implements fast, exact bootstrap Principal Component Analysis and
    Singular Value Decompositions for high dimensional data, as described in
    <doi:10.1080/01621459.2015.1062383> (see also <arXiv:1405.0922> ). For data matrices that are too large to operate
    on in memory, users can input objects with class 'ff' (see the 'ff'
    package), where the actual data is stored on disk. In response, this
    package will implement a block matrix algebra procedure for calculating the
    principal components (PCs) and bootstrap PCs. Depending on options set by
    the user, the 'parallel' package can be used to parallelize the calculation of
    the bootstrap PCs.
	"""
	
	homepage = "http://arxiv.org/abs/1405.0922"
	cran = "bootSVD" 

	version("1.1", md5="50557d934ac7126023685d1b155c4466")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfficientmaxeigenpair(RPackage):
	"""Efficient Initials for Computing the Maximal Eigenpair

	An implementation for using efficient initials to compute the
    maximal eigenpair in R. It provides three algorithms to find the efficient
    initials under two cases: the tridiagonal matrix case and the general matrix
    case. Besides, it also provides two algorithms for the next to the maximal eigenpair under
    these two cases.
	"""
	
	homepage = "http://github.com/mxjki/EfficientMaxEigenpair"
	cran = "EfficientMaxEigenpair" 

	version("0.1.4", md5="f69e765f0b7b4e8caf9830902c215e46")

	depends_on("r@3.3.2:", type=("build", "run"))

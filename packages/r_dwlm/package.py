# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwlm(RPackage):
	"""Doubly Weighted Linear Model

	This linear model solution is useful when both predictor and response have associated uncertainty. The doubly weights linear model solution is invariant on which quantity is used as predictor or response. Based on the results by Reed(1989) <doi:10.1119/1.15963> and Ripley & Thompson(1987) <doi:10.1039/AN9871200377>.
	"""
	
	cran = "dwlm" 

	version("0.1.0", md5="fb8f01308579ffdb451ab0031e7e2d11")

	depends_on("r@3.4:", type=("build", "run"))

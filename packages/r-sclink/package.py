# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSclink(RPackage):
	"""Inferring Functional Gene Co-Expression Networks from Single
Cell Data

	Uses statistical network modeling to understand the co-expression relationships among genes and to construct sparse gene co-expression networks from single-cell gene expression data.
	"""
	
	cran = "scLink" 

	version("1.0.1", md5="21fdbe750481b96141b3a42d7f7c12be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))

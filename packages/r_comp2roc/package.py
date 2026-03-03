# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComp2roc(RPackage):
	"""Compare Two ROC Curves that Intersect

	Comparison of two ROC curves through the methodology proposed by Ana C. Braga.
	"""
	
	cran = "Comp2ROC" 

	version("1.1.4", md5="b118fc5842e342d04f7b08d2b257a1be")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))

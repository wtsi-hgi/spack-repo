# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarnet(RPackage):
	"""Stacked Elastic Net

	Implements stacked elastic net regression (Rauschenberger 2020, <doi:10.1093/bioinformatics/btaa535>). The elastic net generalises ridge and lasso regularisation (Zou 2005, <doi:10.1111/j.1467-9868.2005.00503.x>). Instead of fixing or tuning the mixing parameter alpha, we combine multiple alpha by stacked generalisation (Wolpert 1992 <doi:10.1016/S0893-6080(05)80023-1>).
	"""
	
	homepage = "https://github.com/rauschenberger/starnet"
	cran = "starnet" 

	version("0.0.6", md5="ac8fec17d5f5147aeed871ea3e5d36ef")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cornet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

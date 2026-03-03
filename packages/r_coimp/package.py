# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoimp(RPackage):
	"""Copula Based Imputation Method

	Copula based imputation method. A semiparametric imputation procedure for missing multivariate data based on conditional copula specifications.
	"""
	
	cran = "CoImp" 

	version("1.0", md5="399a8fb0aca50c73e04486f09e1f3fe6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))

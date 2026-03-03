# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbal(RPackage):
	"""Hierarchically Regularized Entropy Balancing

	Implements hierarchically regularized entropy balancing proposed by Xu and Yang (2022) <doi:10.1017/pan.2022.12>. The method adjusts the covariate distributions of the control group to match those of the treatment group. 'hbal' automatically expands the covariate space to include higher order terms and uses cross-validation to select variable penalties for the balancing conditions.
	"""
	
	homepage = "https://yiqingxu.org/packages/hbal/"
	cran = "hbal" 

	version("1.2.12", md5="8642c22383597b6a896fe76c30bfc29f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

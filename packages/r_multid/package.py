# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultid(RPackage):
	"""Multivariate Difference Between Two Groups

	Estimation of multivariate differences between two groups (e.g., multivariate sex differences) with regularized regression methods and predictive approach. See Lönnqvist & Ilmarinen (2021) <doi:10.1007/s11109-021-09681-2> and Ilmarinen et al. (2023) <doi:10.1177/08902070221088155>.
    Includes tools that help in understanding difference score reliability, predictions of difference score variables, conditional intra-class correlations, and heterogeneity of variance estimates. Package development was supported by the Academy of Finland research grant 338891.
	"""
	
	cran = "multid" 

	version("1.0.0", md5="5ad1187614a21e3a29f723ed9e47c865")

	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-glmnet@4.1.2:", type=("build", "run"))
	depends_on("r-proc@1.18:", type=("build", "run"))
	depends_on("r-lavaan@0.6.9:", type=("build", "run"))
	depends_on("r-emmeans@1.6.3:", type=("build", "run"))
	depends_on("r-lme4@1.1.27.1:", type=("build", "run"))
	depends_on("r-quantreg@5.88:", type=("build", "run"))
	depends_on("r-lmertest@3.1.3:", type=("build", "run"))
	depends_on("r-ggpubr@0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))

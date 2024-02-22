# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdmaadmm(RPackage):
	"""ADMM for High-Dimensional Mediation Models

	We use the Alternating Direction Method of Multipliers (ADMM) for parameter estimation in high-dimensional, single-modality mediation models. To improve the sensitivity and specificity of estimated mediation effects, we offer the sure independence screening (SIS) function for dimension reduction. The available penalty options include Lasso, Elastic Net, Pathway Lasso, and Network-constrained Penalty. The methods employed in the package are based on Boyd, S., Parikh, N., Chu, E., Peleato, B., & Eckstein, J. (2011). <doi:10.1561/2200000016>, Fan, J., & Lv, J. (2008) <doi:10.1111/j.1467-9868.2008.00674.x>, Li, C., & Li, H. (2008) <doi:10.1093/bioinformatics/btn081>, Tibshirani, R. (1996) <doi:10.1111/j.2517-6161.1996.tb02080.x>, Zhao, Y., & Luo, X. (2022) <doi:10.4310/21-sii673>, and Zou, H., & Hastie, T. (2005) <doi:10.1111/j.1467-9868.2005.00503.x>. 
	"""
	
	homepage = "https://github.com/psyen0824/HDMAADMM"
	cran = "HDMAADMM" 

	version("0.0.1", md5="d49b1b40e67e62d1e0c3a042a79b98fb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

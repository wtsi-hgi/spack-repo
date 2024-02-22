# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJico(RPackage):
	"""Joint and Individual Regression

	Implements the JICO algorithm [Wang, P., Wang, H., Li, Q., Shen, D., & Liu, Y. (2022). <arXiv:2209.12388>], which solves the multi-group regression problem. The algorithm decomposes the responses from multiple groups into shared and group-specific
        components, which are driven by low-rank approximations of joint and individual structures from the covariates respectively. It provides the implementation of
        the algorithm so solve the iterative continuum regression problem with fixed rank selection, as well as the cross-validation function to perform hyperparameter tuning.
	"""
	
	cran = "JICO" 

	version("0.0", md5="460daaf74d1a36f5272741dd6550347b")

	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKspm(RPackage):
	"""Kernel Semi-Parametric Models

	To fit the kernel semi-parametric model and its extensions. It allows multiple kernels and unlimited interactions in the same model. Coefficients are estimated by maximizing a penalized log-likelihood; penalization terms and hyperparameters are estimated by minimizing leave-one-out error. It includes predictions with confidence/prediction intervals, statistical tests for the significance of each kernel, a procedure for variable selection and graphical tools for diagnostics and interpretation of covariate effects. Currently it is implemented for continuous dependent variables. The package is based on the paper of Liu et al. (2007), <doi:10.1111/j.1541-0420.2007.00799.x>.
	"""
	
	cran = "KSPM" 

	version("0.2.1", md5="f5e4d0c6294cbc78c9b8f7af7762f929")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))

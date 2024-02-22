# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlr(RPackage):
	"""Gamma Lasso Regression

	The gamma lasso algorithm provides regularization paths corresponding to a range of non-convex cost functions between L0 and L1 norms.  As much as possible, usage for this package is analogous to that for the glmnet package (which does the same thing for penalization between L1 and L2 norms).  For details see: Taddy (2017 JCGS), 'One-Step Estimator Paths for Concave Regularization', <arXiv:1308.5623>.
	"""
	
	homepage = "https://github.com/TaddyLab/gamlr"
	cran = "gamlr" 

	version("1.13-8", md5="5b1ba8474ace04732ec9917929f2e457")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

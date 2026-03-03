# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeecure(RPackage):
	"""Marginal Proportional Hazards Mixture Cure Models with
Generalized Estimating Equations

	Features the marginal parametric and semi-parametric proportional hazards mixture cure models for analyzing clustered survival data with a possible cure fraction. A reference is Yi Niu and Yingwei Peng (2014) <doi:10.1016/j.jmva.2013.09.003>.
	"""
	
	cran = "geecure" 

	version("1.0-6", md5="2803317750d09bede2310c28d13607e8")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))

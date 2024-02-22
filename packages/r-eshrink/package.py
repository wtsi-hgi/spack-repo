# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REshrink(RPackage):
	"""Shrinkage for Effect Estimation

	Computes shrinkage estimators for regression problems. Selects
    penalty parameter by minimizing bias and variance in the effect estimate, where bias and variance are estimated from the posterior predictive distribution. See Keller and Rice (2017) <doi:10.1093/aje/kwx225> for more details.
	"""
	
	cran = "eshrink" 

	version("0.1.2", md5="e048b2a84d7cfb59962375b3e363f21e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))

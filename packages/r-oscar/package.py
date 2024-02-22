# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROscar(RPackage):
	"""Optimal Subset Cardinality Regression (OSCAR) Models Using the
L0-Pseudonorm

	Optimal Subset Cardinality Regression (OSCAR) models offer
    regularized linear regression using the L0-pseudonorm, conventionally
    known as the number of non-zero coefficients. The package estimates an
    optimal subset of features using the L0-penalization via
    cross-validation, bootstrapping and visual diagnostics. Effective
    Fortran implementations are offered along the package for finding
    optima for the DC-decomposition, which is used for transforming the
    discrete L0-regularized optimization problem into a continuous
    non-convex optimization task. These optimization modules include DBDC
    ('Double Bundle method for nonsmooth DC optimization' as described in
    Joki et al. (2018) <doi:10.1137/16M1115733>) and LMBM ('Limited
    Memory Bundle Method for large-scale nonsmooth optimization' as
    in Haarala et al. (2004) <doi:10.1080/10556780410001689225>). The
    OSCAR models are comprehensively exemplified in Halkola et al. (2023) 
    <doi:10.1371/journal.pcbi.1010333>). Multiple regression model families
    are supported: Cox, logistic, and Gaussian.
	"""
	
	homepage = "https://github.com/Syksy/oscar"
	cran = "oscar" 

	version("1.2.1", md5="4993700a191196e141aa84875e71c7da")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hamlet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))

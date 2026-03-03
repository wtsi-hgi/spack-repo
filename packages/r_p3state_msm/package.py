# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RP3stateMsm(RPackage):
	"""Analyzing Survival Data from an Illness-Death Model

	Contains functions for data preparation,
	prediction of transition probabilities,
	estimating semi-parametric regression models
	and for implementing nonparametric estimators
	for other quantities. See Meira-Machado and
	Roca-Pardiñas (2011) <doi:10.18637/jss.v038.i03>.
	"""
	
	cran = "p3state.msm" 

	version("1.3.2", md5="cfa205982df890d12a3fde099be0a75f")

	depends_on("r@2.8.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

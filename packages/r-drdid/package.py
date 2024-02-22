# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrdid(RPackage):
	"""Doubly Robust Difference-in-Differences Estimators

	Implements the locally efficient doubly robust difference-in-differences (DiD)
    estimators for the average treatment effect proposed by Sant'Anna and Zhao (2020)
    <doi:10.1016/j.jeconom.2020.06.003>. The estimator combines inverse probability weighting and outcome
    regression estimators (also implemented in the package) to form estimators with
    more attractive statistical properties. Two different estimation methods can be used
    to estimate the nuisance functions.
	"""
	
	homepage = "https://psantanna.com/DRDID/"
	cran = "DRDID" 

	version("1.0.6", md5="ce070bd4f5e71469e282fe86d781dd99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-bmisc@1.4.1:", type=("build", "run"))

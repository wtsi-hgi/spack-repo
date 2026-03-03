# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodalm(RPackage):
	"""Transformation-Free Linear Regression for Compositional Outcomes
and Predictors

	Implements the expectation-maximization (EM) algorithm as described in Fiksel et al. (2021) <doi:10.1111/biom.13465>
    for transformation-free linear regression for compositional outcomes and predictors.
	"""
	
	homepage = "https://github.com/jfiksel/codalm"
	cran = "codalm" 

	version("0.1.2", md5="a3dd6c622c515b6511f3fb87e96913c8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-squarem@2020.3:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))

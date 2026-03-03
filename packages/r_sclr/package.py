# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSclr(RPackage):
	"""Scaled Logistic Regression

	
    Maximum likelihood estimation of the scaled logit model parameters
    proposed in Dunning (2006) <doi:10.1002/sim.2282>.
	"""
	
	homepage = "https://khvorov45.github.io/sclr/"
	cran = "sclr" 

	version("0.3.1", md5="0d0ffa5ac68db63ce583d82425f8f762")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))

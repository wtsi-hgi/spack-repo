# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCornet(RPackage):
	"""Elastic Net with Dichotomised Outcomes

	Implements lasso and ridge regression for dichotomised outcomes (Rauschenberger et al. 2023, <doi:10.1080/02664763.2023.2233057>). Such outcomes are not naturally but artificially binary. They indicate whether an underlying measurement is greater than a threshold.
	"""
	
	homepage = "https://github.com/rauschenberger/cornet"
	cran = "cornet" 

	version("0.0.9", md5="aa12e44721f72d6b824207764adeeffe")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-palasso", type=("build", "run"))

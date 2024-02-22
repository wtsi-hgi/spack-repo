# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClogitboost(RPackage):
	"""Boosting Conditional Logit Model

	A set of functions to fit a boosting conditional logit model.
	"""
	
	cran = "clogitboost" 

	version("1.1", md5="131f6bde88c0638fa092bcf1486f059e")

	depends_on("r-rcpp", type=("build", "run"))

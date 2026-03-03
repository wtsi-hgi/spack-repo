# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpsurv(RPackage):
	"""Nonparametric Change Point Estimation for Survival Data

	Nonparametric change point estimation for survival data based on p-values of exact binomial tests.
	"""
	
	cran = "CPsurv" 

	version("1.0.0", md5="66e4b1358b88a959b308e87735aeee74")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival@2.40.1:", type=("build", "run"))
	depends_on("r-muhaz@1.2.6:", type=("build", "run"))

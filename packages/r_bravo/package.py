# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBravo(RPackage):
	"""Bayesian Screening and Variable Selection

	Performs Bayesian variable screening and selection for ultra-high dimensional linear regression models.
	"""
	
	cran = "bravo" 

	version("2.3.1", md5="fa2af1ec3313eef3d2ec3fc677743228")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrailtyhl(RPackage):
	"""Frailty Models via Hierarchical Likelihood

	Implements the h-likelihood estimation procedures for general frailty models including competing-risk models and joint models.
	"""
	
	cran = "frailtyHL" 

	version("2.3", md5="36e4cfd4c65f0f30d915faabc190f7b7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHazarddiff(RPackage):
	"""Conditional Treatment Effect for Competing Risks

	The conditional treatment effect for competing risks data in observational studies is estimated. While it is described as a constant difference between the hazard functions given the covariates, we do not assume specific functional forms for the covariates. Rava, D. and Xu, R. (2021) <arXiv:2112.09535>.
	"""
	
	cran = "HazardDiff" 

	version("0.1.0", md5="6df4cc3eb08efd034e20237c5dfd8d0a")

	depends_on("r-ahaz", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))

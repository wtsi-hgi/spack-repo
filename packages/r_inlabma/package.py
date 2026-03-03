# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlabma(RPackage):
	"""Bayesian Model Averaging with INLA

	Fit Spatial Econometrics models using Bayesian model averaging 
  on models fitted with INLA. The INLA package can be obtained from 
  <https://www.r-inla.org>. 
	"""
	
	cran = "INLABMA" 

	version("0.1-12", md5="7250ed51c9c602580ea2dd26e16a9ec1")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))

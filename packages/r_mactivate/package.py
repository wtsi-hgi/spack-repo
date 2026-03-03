# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMactivate(RPackage):
	"""Multiplicative Activation

	Provides methods and classes for adding m-activation ("multiplicative activation") layers to MLR or multivariate logistic regression models.  M-activation layers created in this library detect and add input interaction (polynomial) effects into a predictive model.  M-activation can detect high-order interactions -- a traditionally non-trivial challenge.  Details concerning application, methodology, and relevant survey literature can be found in this library's vignette, "About."
	"""
	
	cran = "mactivate" 

	version("0.6.6", md5="045239fb29890c6d42af432f47671880")

	depends_on("r@3.5:", type=("build", "run"))

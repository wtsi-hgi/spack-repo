# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlogitbma(RPackage):
	"""Bayesian Model Averaging for Multinomial Logit Models

	Provides a modified function bic.glm of the BMA package that can be applied to multinomial logit (MNL) data. The data is converted to binary logit using the Begg & Gray approximation. The package also contains functions for maximum likelihood estimation of MNL. 
	"""
	
	cran = "mlogitBMA" 

	version("0.1-7", md5="c21fcc430436fc9e1439880b3855c764")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-bma", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))

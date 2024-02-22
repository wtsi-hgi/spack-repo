# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlgf(RPackage):
	"""Bayesian Model Selection with Suspected Latent Grouping Factors

	Implements the Bayesian model selection method with suspected latent 
    grouping factor methodology of Metzger and Franck (2020), 
    <doi:10.1080/00401706.2020.1739561>. SLGF detects latent 
    heteroscedasticity or group-based regression effects based on the levels of a 
    user-specified categorical predictor. 
	"""
	
	cran = "slgf" 

	version("2.0.0", md5="d2fc0904dd47261d8c2d1b8682c7b45b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))

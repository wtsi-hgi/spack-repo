# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomark(RPackage):
	"""Find Biomarkers in Two-Class Discrimination Problems

	Variable selection methods are provided for several classification methods: the lasso/elastic net, PCLDA, PLSDA, and several t-tests. Two approaches for selecting cutoffs can be used, one based on the stability of model coefficients under perturbation, and the other on higher criticism.
	"""
	
	cran = "BioMark" 

	version("0.4.5", md5="4ed86d631e3921baa543764f4374e195")

	depends_on("r-pls", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-st@1.1.6:", type=("build", "run"))

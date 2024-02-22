# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REben(RPackage):
	"""Empirical Bayesian Elastic Net

	Provides the Empirical Bayesian Elastic Net for handling multicollinearity in generalized linear regression models.  As a special case of the 'EBglmnet'
  package (also available on CRAN), this package encourages a grouping effects to select relevant variables and estimate the corresponding non-zero effects. 
	"""
	
	cran = "EBEN" 

	version("5.1", md5="3f7c0e0cd594121b0138c6f3e76d2612")

	depends_on("r@2.10:", type=("build", "run"))

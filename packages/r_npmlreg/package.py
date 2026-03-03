# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpmlreg(RPackage):
	"""Nonparametric Maximum Likelihood Estimation for Random Effect
Models

	Nonparametric maximum likelihood estimation or Gaussian
        quadrature for overdispersed generalized linear models and
        variance component models.
	"""
	
	cran = "npmlreg" 

	version("0.46-5", md5="247898b4ce029b7bef8e22f3e6300d91")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-statmod@1.4.20:", type=("build", "run"))

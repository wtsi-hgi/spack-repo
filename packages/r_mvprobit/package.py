# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvprobit(RPackage):
	"""Multivariate Probit Models

	Tools for estimating multivariate probit models,
   calculating conditional and unconditional expectations,
   and calculating marginal effects on conditional and unconditional
   expectations.
	"""
	
	homepage = "http://www.sampleSelection.org"
	cran = "mvProbit" 

	version("0.1-10", md5="8cfa8de069169cd06bc82977f1c9c2c7")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mvtnorm@0.9.9994:", type=("build", "run"))
	depends_on("r-maxlik@1.0.0:", type=("build", "run"))
	depends_on("r-abind@1.3.0:", type=("build", "run"))
	depends_on("r-bayesm@2.2.4:", type=("build", "run"))
	depends_on("r-misctools@0.6.11:", type=("build", "run"))

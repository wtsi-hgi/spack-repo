# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarg(RPackage):
	"""Approximate Marginal Inference for Regression-Scale Models

	Likelihood inference based on higher order approximations 
  for linear nonnormal regression models.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "marg" 

	version("1.2-2.1", md5="6fd9cd0f96e858e37d494bc8d299bd7c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

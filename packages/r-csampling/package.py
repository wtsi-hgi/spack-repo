# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsampling(RPackage):
	"""Functions for Conditional Simulation in Regression-Scale Models

	Monte Carlo conditional inference for the parameters of a
  linear nonnormal regression model.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "csampling" 

	version("1.2-2.1", md5="ec2e9ed5a675c2e57a31837004f4f82d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-marg", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

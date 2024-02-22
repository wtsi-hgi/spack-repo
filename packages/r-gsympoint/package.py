# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsympoint(RPackage):
	"""Estimation of the Generalized Symmetry Point, an Optimal
Cutpoint in Continuous Diagnostic Tests

	Estimation of the cutpoint defined by the Generalized Symmetry point in a binary classification setting based on a continuous diagnostic test or marker. Two methods have been implemented to construct confidence intervals for this optimal cutpoint, one based on the Generalized Pivotal Quantity and the other based on Empirical Likelihood. Numerical and graphical outputs for these two methods are easily obtained.
	"""
	
	cran = "GsymPoint" 

	version("1.1.2", md5="7d74b8bfe30a3ed846155b8167b081d0")

	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))

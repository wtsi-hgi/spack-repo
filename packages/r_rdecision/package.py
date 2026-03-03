# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdecision(RPackage):
	"""Decision Analytic Modelling in Health Economics

	Classes and functions for modelling health care interventions 
  using decision trees and semi-Markov models. Mechanisms are provided for 
  associating an uncertainty distribution with each source variable and for
  ensuring transparency of the mathematical relationships between variables.
  The package terminology follows Briggs "Decision Modelling for Health
  Economic Evaluation" (2006, ISBN:978-0-19-852662-9).
	"""
	
	cran = "rdecision" 

	version("1.2.0", md5="b18a4783362c87c0895cca6f3fb3aec4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidatetools(RPackage):
	"""Checking and Simplifying Validation Rule Sets

	Rule sets with validation rules may contain redundancies or contradictions. 
  Functions for finding redundancies and problematic rules are provided, 
  given a set a rules formulated with 'validate'.
	"""
	
	homepage = "https://github.com/data-cleaning/validatetools"
	cran = "validatetools" 

	version("0.5.2", md5="31cd2f80828dde8f119a3f4a42b671f0")

	depends_on("r-validate", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVartest(RPackage):
	"""Tests for Variance Homogeneity

	Performs 20 omnibus tests for testing the composite hypothesis of variance homogeneity.
	"""
	
	cran = "vartest" 

	version("1.0", md5="5c761436bdd2be2f019a976d6608fac9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))

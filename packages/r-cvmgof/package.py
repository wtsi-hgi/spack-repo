# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvmgof(RPackage):
	"""Cramer-von Mises Goodness-of-Fit Tests

	It is devoted to Cramer-von Mises goodness-of-fit tests.
    It implements three statistical methods based on Cramer-von Mises statistics to estimate and test a regression model.
	"""
	
	cran = "cvmgof" 

	version("1.0.3", md5="309ca82fb63b24734c0d956eec4bb108")

	depends_on("r-lattice", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImtest(RPackage):
	"""Information Matrix Test for Generalized Partial Credit Models

	Implementation of the information matrix test for generalized partial credit models.
	"""
	
	cran = "IMTest" 

	version("1.0.0", md5="80fff7adb26cc990c298d824124e03aa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralhoslem(RPackage):
	"""Goodness of Fit Tests for Logistic Regression Models

	Functions to assess the goodness of fit of binary, multinomial and ordinal logistic models. Included are the Hosmer-Lemeshow tests (binary, multinomial and ordinal) and the Lipsitz and Pulkstenis-Robinson tests (ordinal).
	"""
	
	cran = "generalhoslem" 

	version("1.3.4", md5="fd7d2050a913793e25a7e196a02722d6")

	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.3.1:", type=("build", "run"))

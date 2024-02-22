# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReghelper(RPackage):
	"""Helper Functions for Regression Analysis

	A set of functions used to automate commonly used methods in
    regression analysis. This includes plotting interactions, and calculating
    simple slopes, standardized coefficients, regions of significance
    (Johnson & Neyman, 1936; cf. Spiller et al., 2012), etc. See the reghelper
    documentation for more information, documentation, and examples.
	"""
	
	homepage = "https://github.com/jeff-hughes/reghelper"
	cran = "reghelper" 

	version("1.1.2", md5="878a08bb616e62c7499d0e6f9e2f1a94")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

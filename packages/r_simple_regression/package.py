# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpleRegression(RPackage):
	"""Multiple Regression and Moderated Regression Made Simple

	Provides SPSS- and SAS-like output for least squares multiple 
    regression and moderated regression, as well as interaction plots and 
    Johnson-Neyman regions of significance for interactions. The output 
    includes standardized coefficients, partial and semi-partial correlations, 
    collinearity diagnostics, plots of residuals, and detailed information 
    about simple slopes for interactions. There are numerous options for 
    designing interaction plots, including plots of interactions for both lm
    and lme models.
	"""
	
	cran = "SIMPLE.REGRESSION" 

	version("0.1.6", md5="7881e3341cd6953c4fa56a2f8ee98217")

	depends_on("r-nlme", type=("build", "run"))
